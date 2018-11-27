from django.core.management.base import BaseCommand, CommandError
from plants.models import *
from frontend.models import Actions, Transactions
from login.models import AuthUser
import csv
import psycopg2

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-restore', nargs='?', help='Use if restoring CSV files')
        parser.add_argument('-update', nargs='?', help='use if updating new plants added through the UI or through an import')
        
    def handle(self, *args, **options):
        self.stdout.write("processing transactions!!!")
        
        print('Flushing plant table...')
        Plant.objects.all().delete()
        
        
        process_transactions()
        process_updates()
        
    
    
properties_1_to_1 = ['common_name',
                     'drought_tol_id',
                     'flood_tol_id',
                     'humidity_tol_id',
                     'salt_tol_id',
                     'toxin_removal_id',
                     'wind_tol_id',
                     'minimum_temperature_tol',
                     'inoculant',
                     'fire_tol_id',
                     'livestock_bloat_id',
                     'pH_min',
                     'pH_max',
                     'toxicity_id',
                     'lifespan_id',
                     'allelopathic_id',
                     'tags',
                     'allelochemicals',
                     'serotiny_id',
                     'degree_of_serotiny_id',# add family here?!?!
                     'family_id',
                     'family_common_name_id',
                     'time_to_first_harvest']

properties_many_with_region = ['active_growth_period',
                               'animal_attractor',
                               'animal_regulator',
                               'barrier',
                               'canopy_density',
                               'duration',
                               'endemic_status',
                               'erosion_control',
                               'nutrient_requirements',
                               'harvest_period',
                               'height_at_maturity',
                               'insect_attractor',
                               'insect_regulator',
                               'leaf_retention',
                               'shade_tol',
                               'soil_drainage_tol',
                               'spread_at_maturity',
                               'sun_needs',
                               'water_needs']
                                ######################################################
#-------------------------------------- TODO should add serotiny and degree of serotiny--------------------------
                                ######################################################
properties_1_to_many = ['family',
                        'family_common_name',#-----the_family
                        ]
                        #'tags']
properties_scientific_name = [# 'genus', #add _id for foreign keys
#                             'species',
#                             'subspecies',
#                             'variety',
#                             'form',
#                             'cutivar',
                              'scientific_name'
                             ]

properties_many_to_many = ['biochemical_material_prod',
                           'cultural_and_amenity_prod',
                           'flower_color',
                           'foliage_color',
                           'food_prod',
                           'animal_food',
                           'fruit_color',
                           'layer',
                           'medicinals_prod',
                           'mineral_nutrients_prod',
                           'raw_materials_prod'
                           ]

def get_attributes(cls):
    f = False
    attributes = cls.__doc__.split(',')[1:]
    attributes[-1] = attributes[-1][:-1]
    if "regions" in attributes[-1]:
        t = attributes[-1]
        attributes[-1]=attributes[-2]
        attributes[-2]=t
        f= True
    if "name_category" in attributes[-1]:
        t = attributes[-1]
        attributes[-1]=attributes[-2]
        attributes[-2]=t
        f= True
    attributes = [i.strip()+'_id' for i in attributes]
    return attributes, f

    

            
def process_updates():
    print("Processing Updates")
    plants={0:{}}
    for transaction in Transactions.objects.all().filter(ignore=False, transaction_type='UPDATE').order_by('id'): # if same user updates should be filtered out
        #print('transaction_type = ' + transaction.transaction_type)
        if not(transaction.plants_id):
            print('No plant_id in transaction UPDATE!')
            continue
        actions={}
        if not(transaction.plants_id in list(plants.keys())):
            plants[transaction.plants_id]={}
        # merging dictionaries so the latest update would be the result
        for action in transaction.actions_set.all():
            # actions[action.property]=[action.value, action.regions_id]
        # for property, value in actions.items():
            plants[transaction.plants_id][action.property]=[action.value, action.regions_id]

        # plants[transaction.plants_id]={**plants[transaction.plants_id],**actions}# saves the last update, not the number of votes
        # print(plants)

    for plant, updates in plants.items():
        for property, value in updates.items():
            if Plant.objects.get(pk=plant):
                the_plant = Plant.objects.get(pk=plant)
            else:
                raise ValueError("Invalid property plant id = " + plant)
            #print(property, property=='height', property in 'heightspreadroot_depth')
            if property in 'heightspreadroot_depth':
                if PlantRegion.objects.filter(plants=the_plant.id, regions=value[1]):# TODO check for region Null----------------------------------
                    plant_region = PlantRegion.objects.filter(plants=the_plant.id, regions=value[1]).first()#filter(transaction.plants_id, action.regions)
                else:
                    plant_region = PlantRegion()
                    plant_region.plants = the_plant
                    plant_region.regions = value[1]
                    plant_region.save()

                # somthing nice to learn------- how to dynamically choose the attribute that we want to set?!
                if property == 'height':
                    plant_region.height = float(value[0])
                elif property == 'spread':
                    plant_region.spread = float(value[0])
                elif property == 'root_depth':
                    plant_region.root_depth = float(value[0])
                else:
                    raise ValueError("Invalid property name = " + property)
                plant_region.save()
            elif property in properties_scientific_name:
                continue
            elif property in properties_1_to_1:
                #print('T_id={0}, property={1}, value={2}'.format(transaction.id, property, value[0]))
                setattr(the_plant, property, value[0]) # pH or ph... not being saved!
                try: 
                    the_plant.save()
                except Error as e:
                    print(e)
            elif property in properties_many_with_region:# TODO PlantBarrierByRegion
                #print('T_id={0}, property={1}, region={2}, value={3}'.format(transaction.id, property, value[1], value[0]))
                class_name = 'Plant' + property.title().replace('_', '') + 'ByRegion'
                cls = globals()[class_name]
                attributes, is_region_last = get_attributes(cls)
                filter_args = {attributes[0]:the_plant.id, attributes[2]:value[0], attributes[1]:value[1]}
                cls_instance = cls.objects.filter(**filter_args)# TODO make sure get() works instead of filter().first() which also may carry bugs
                if not(cls_instance):
                    cls_instance = cls()
                    cls_instance.save()
                else:
                    cls_instance = cls_instance.first()
                
                if is_region_last:
                    cls_instance = cls(cls_instance.id ,the_plant.id, value[0], value[1])
                else:
                    cls_instance = cls(cls_instance.id ,the_plant.id, value[1], value[0])
                cls_instance.save()
            elif property in properties_many_to_many:
                class_name = 'Plant' + property.title().replace('_', '')
                cls = globals()[class_name]
                attributes, f = get_attributes(cls)
                filter_args={attributes[0]:the_plant.id, attributes[1]:value[0]}
                cls_instance = cls.objects.filter(**filter_args)# TODO make sure get works instead of filter().firts() which also may carry bugs
                if not(cls_instance):
                    cls_instance = cls()
                    cls_instance.save()
                else:
                    cls_instance = cls_instance.first()
                cls_instance = cls(cls_instance.id ,the_plant.id, value[0])# make sure that it is rewriting....
                cls_instance.save()
            elif property in "ImageURL":
                class_name = action.property
                cls = globals()[class_name]
                cls_instance = cls()
                cls_instance.save()
                cls_instance = cls(cls_instance.id, the_plant.id, action.value)
                cls_instance.save()
                print("Process Updates image URL is " + str(action.value))
                print('T_id={0}, property={1}, value={2}'.format(transaction.id, property, value[0]))
            elif property in properties_1_to_many:
                pass
            else:
                raise ValueError("Invalid property name = " + property)
                pass

def process_transactions():
    print("Processing transactions")
    for transaction in Transactions.objects.all().filter(ignore=False).order_by('id'):
        #print('transaction_type = ' + transaction.transaction_type)
        if transaction.transaction_type == 'INSERT':# get_or_crete????????
#confirm plant isn't already in database
            
            
            
            new_plant = Plant()
            new_plant.save()
            transaction.plants_id = new_plant.id
            transaction.save()
            #print('plant_id = ' + str(transaction.plants_id))
        elif transaction.transaction_type == 'DELETE':
            if transaction.plant is None:
                print('None objects')
                pass
                # db.session.rollback()
                # raise ValueError("Can't delete plant == None")
            # db.session.delete(transaction.plant)
            Plant.objects.get(pk=transaction.plant).delete()#----------------should be tested-----
            # db.session.commit()
            continue
        elif transaction.transaction_type == 'UPDATE':
            #BECAUSE WE FLUSHED THE PLANTS TABLE, WE HAVE TO RESET THE PLANT ID FROM THE PARENT TRANSACTION (THE ORIGINAL INSERT OF THAT PLANT)
            #print("this plants related transaction id is ",transaction.parent_transaction)
            #print("user id: ", transaction.users_id, " transaction_id: ", transaction.id)
            parentTrans = Transactions.objects.get(id=transaction.parent_transaction)
            transaction.plants_id = parentTrans.plants_id
            transaction.save()              
        else:
            print('rollback')
            # db.session.rollback()
            # raise ValueError("Invalid transaction type = " + transaction.transaction_type)

        if len(transaction.actions_set.all())==0:
            print(len(transaction.actions_set.all()))

        for action in transaction.actions_set.all():# transaction.actions:
            the_plant=Plant.objects.get(pk=transaction.plants_id)
            
            
            if action.property in properties_scientific_name:
                #print('T_id={0}, property={1}, name={2}, value={3}'.format(transaction.id, action.property, action.category, action.value))
                
                sci_name_obj_id = None
                try:
                    sci_name_obj = ScientificName.objects.get(value = action.value)
                    sci_name_obj_id = sci_name_obj.id
                except:
                    sci_cls_instance = None
                    class_name = 'ScientificName'
                    sci_cls = globals()[class_name]
                    sci_cls_instance =  sci_cls()
                    sci_cls_instance = sci_cls(sci_cls_instance.id, action.value)
                    sci_name_obj_id = sci_cls_instance.id
                    sci_cls_instance.save()
                    
                class_name = 'PlantScientificName'
                cls = globals()[class_name]
                cls_instance = cls()
                cls_instance = cls(cls_instance.id ,the_plant.id, sci_name_obj_id, action.category)
                cls_instance.save()
            
            
            elif action.property in 'height spread root_depth':
                if PlantRegion.objects.filter(plants=the_plant.id, regions=action.regions):# TODO check for region Null----------------------------------
                    plant_region = PlantRegion.objects.filter(plants=the_plant.id, regions=action.regions).first()#transaction.plants_id
                else:
                    plant_region = PlantRegion()
                    plant_region.plants = the_plant
                    plant_region.regions = action.regions
                    plant_region.save()
                # somthing nice to learn------- how to dynamically choose the attribute that we want to set?!
                if action.property == 'height':
                    plant_region.height = float(action.value)
                elif action.property == 'spread':
                    plant_region.spread = float(action.value)
                elif action.property == 'root_depth':
                    plant_region.root_depth = float(action.value)
                else:
                    raise ValueError("Invalid property name = " + action.property)

                plant_region.save()

            elif action.property in properties_1_to_1:# TODO check for INSERT DELETE UPDATE??????????????????
                                                    # TODO height
                #print('T_id={0}, property={1}, value={2}'.format(transaction.id, action.property, action.value))
                setattr(the_plant, action.property, action.value)# pH or ph... not being saved!
                try: 
                    the_plant.save()
                except Error as e:
                    print(e)
            elif action.property in properties_many_with_region:# TODO height
                #print('T_id={0}, property={1}, region={2}, value={3}'.format(transaction.id, action.property, action.regions, action.value))
                class_name = 'Plant' + action.property.title().replace('_', '') + 'ByRegion'
                cls = globals()[class_name]
                attributes, is_region_last = get_attributes(cls)
                if action.action_type == 'INSERT':#CREATE
                    # temp = cls.objects.create(the_plant.id, action.regions, action.value)
                    cls_instance = cls()
                    cls_instance.save()
                    #print (cls_instance.id ,the_plant.id, action.regions, action.value)
                    if is_region_last:
                        cls_instance = cls(cls_instance.id ,the_plant.id, action.value, action.regions)# no regions added?
                    else:
                        cls_instance = cls(cls_instance.id ,the_plant.id, action.regions, action.value)
                    cls_instance.save()
            elif action.property in properties_many_to_many:
                class_name = 'Plant' + action.property.title().replace('_', '')
                cls = globals()[class_name]
                if action.action_type == 'INSERT':#CREATE
                    # temp = cls.objects.create(the_plant.id, action.value)
                    cls_instance = cls()
                    cls_instance.save()
                    #print (cls_instance.id ,the_plant.id, action.value)
                    cls_instance = cls(cls_instance.id ,the_plant.id, action.value)
                    cls_instance.save()
            elif action.property in 'ImageURL':
                class_name = action.property
                cls = globals()[class_name]
                if action.action_type == 'INSERT':
                    cls_instance = cls()
                    cls_instance.save()
                    cls_instance = cls(cls_instance.id, the_plant.id, action.value)
                    print("Process Transaction image URL is " + str(action.value))
                    cls_instance.save()
            elif action.property in properties_1_to_many: # TODO Seortiny
                pass
                # class_name = action.property.title().replace('_', '')
                # cls = globals()[class_name]
                # if action.action_type == 'INSERT':#CREATE
                #   # temp = cls.objects.create(the_plant.id, action.value)
                #   cls_instance = cls()
                #   cls_instance.save()
                #   print (cls_instance.id ,the_plant.id, action.value)
                #   cls_instance = cls(cls_instance.id ,the_plant.id, action.value)
                #   cls_instance.save()
                # temp = cls.objects.create(cls_instance.id ,the_plant.id, action.value)
                # print('calss name',class_name)
                
                # elif action.action_type == 'DELETE':
                # when action_type is DELETE, the action value tells you the ID of the row to delete in the 1-to-many or many-to-many table
                    # pass
                    # cls_instance = cls.query.get(action.value)
                    # db.session.delete(cls_instance)
                # elif action.action_type == 'UPDATE':
                    # pass
                    # db.session.rollback()
                    # raise ValueError("Support for updating values hasn't been implemented yet."
                    # + "Either implement updating in the code, or do a delete followed by an insert.")
                # else:
                    # db.session.rollback()
                    # raise ValueError("Invalid action type = " + action.action_type)
                    # pass
            else:
                # db.session.rollback()
                print('invalid property transaction id ', transaction.id)
                raise ValueError("Invalid property name = " + action.property)
                pass

#---------------------flushing tables---------------------------


