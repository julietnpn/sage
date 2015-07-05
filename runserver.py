from models import *

import time
from sandman import app, db
from sandman.model import activate, register, Model
from sqlalchemy import inspect
from sqlalchemy.orm.attributes import get_history, instance_state
#from sqlalchemy.ext.associationproxy import association_proxy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:plants@localhost/plants'

properties_1_to_1 = ['genus',
                     'species',
                     'common_name',
                     'drought_tol_id',
                     'flood_tol_id',
                     'humidity_tol_id',
                     'salt_tol_id',
                     'toxin_removal_id',
                     'wind_tol_id',
                     'minimum_temperature_tol',
                     'pH',
                     'innoculant',
                     'variety',
                     'fire_tol_id',
                     'livestock_bloat_id',
                     'toxicity',
                     'lifespan',
                     'allelopathic']

properties_many_with_region = ['active_growth_period',
                               'animal_attractor',
                               'animal_regulator',
                               'canopy_density',
                               'duration',
                               'endemic_status',
                               'erosion_control',
                               'fertility_needs',
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

properties_1_to_many = ['family',
                        'family_common_name',
                        'url_tags']

properties_many_to_many = ['biochemical_material_prod',
                           'cultural_and_amenity_prod'
                           'flower_color',
                           'foliage_color',
                           'food_prod',
                           'fruit_color',
                           'layer',
                           'medicinals_prod',
                           'mineral_nutrients_prod',
                           'raw_materials_prod']

register((Actions,
          ActiveGrowthPeriod,
          Allelopathic,
          Animals,
          BiochemicalMaterialProd,
          CanopyDensity,
          CulturalAndAmenityProd,
          DroughtTol,
          EndemicStatus,
          ErosionControl,
          Family,
          FloodTol,
          FoodProd,
          FlowerColor,
          FoliageColor,
          FruitColor,
          HarvestPeriod,
          HumidityTol,
          Insects,
          Layer,
          Lifespan,
          LeafRetention,
          MedicinalsProd,
          MineralNutrientsProd,
          Plants,
          RawMaterialsProd,
          Regions,
          SaltTol,
          ShadeTol,
          SunNeeds,
          ToxinRemoval,
          Toxicity,
          Transactions,
          Users,
          WaterNeeds,
          WindTol))


def delete_plants():
  Plants.query.delete()
  db.session.commit()

def process_transactions():
  for transaction in Transactions.query.filter_by(ignore=False).order_by(Transactions.id).all():
    print 'transaction_type = ' + transaction.transaction_type
    print 'plant_id = ' + str(transaction.plants_id)
    if transaction.transaction_type == 'INSERT':
      new_plant = Plants()
      transaction.plant = new_plant
      db.session.add(new_plant)
    elif transaction.transaction_type == 'DELETE':
      if transaction.plant is None:
        db.session.rollback()
        raise ValueError("Can't delete plant == None")
      db.session.delete(transaction.plant)
      db.session.commit()
      continue
    elif transaction.transaction_type == 'UPDATE':
      pass
    else:
      db.session.rollback()
      raise ValueError("Invalid transaction type = " + transaction.transaction_type)

    for action in transaction.actions:
      if action.property in properties_1_to_1:
        print 'T_id={0}, property={1}, value={2}'.format(transaction.id, action.property, action.value)
        setattr(transaction.plant, action.property, action.value)
      elif action.property in properties_many_with_region or action.property in properties_1_to_many or action.property in properties_many_to_many:
        print 'T_id={0}, property={1}, region={2}, value={3}'.format(transaction.id, action.property, action.region, action.value)
        if action.property in properties_many_to_many:
          class_name = 'Plants' + action.property.title().replace('_', '')
        elif action.property in properties_many_with_region:
          class_name = 'Plants' + action.property.title().replace('_', '') + 'ByRegion'
        else:
          class_name = action.property.title().replace('_', '')
        cls = globals()[class_name]
        if action.action_type == 'INSERT':
          cls_instance = cls(transaction.plant, action.region, action.value)
          db.session.add(cls_instance)
        elif action.action_type == 'DELETE':
          # when action_type is DELETE, the action value tells you the ID of the row to delete in the 1-to-many or many-to-many table
          cls_instance = cls.query.get(action.value)
          db.session.delete(cls_instance)
        elif action.action_type == 'UPDATE':
          db.session.rollback()
          raise ValueError("Support for updating values hasn't been implemented yet."
                         + "Either implement updating in the code, or do a delete followed by an insert.")
        else:
          db.session.rollback()
          raise ValueError("Invalid action type = " + action.action_type)
      else:
        db.session.rollback()
        raise ValueError("Invalid property name = " + action.property)

    db.session.commit()
    #time.sleep(30)

#delete_plants()
#process_transactions()


print('ACTIVATE')
activate(browser=True)
print('RUN')
app.run(debug=False)
