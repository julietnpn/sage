from flask.ext.admin.contrib.sqla import ModelView
from sandman import db

class ModelViewAddToTransactions(ModelView):
    def create_model(self, form):
        return self._handle_edits(form, self.model(), 'INSERT')


    def update_model(self, form, model):
        return self._handle_edits(self, form, model, 'UPDATE')


    def _handle_edits(self, form, model, edit_type):
        try:
            print 'handling edits...'
            transaction = Transactions(users_id=1, transaction_type=edit_type, ignore=False)
            self.session.add(transaction)
            form.populate_obj(model)
                       
            #for attr in sorted(inspect(model).attrs, key=lambda a: a.key):
            #    print str(attr.key) + ': ' + str(attr.history)
            for prop_name in properties_1_to_1:
                history = get_history(model, prop_name)
                if history.added and history.added[0]:
                    # action type could be 'DELETE' if, for example, a value for a one-to-many property is being removed
                    action = Actions(transaction=transaction, action_type='UPDATE', property=prop_name, value=history.added[0])
                    self.session.add(action)
            self.session.commit()
            return True
        except Exception as ex:
            print 'EXCEPTION!!!'
            print ex
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to create record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to create record.')
            self.session.rollback()
            return False

    def delete_model(self, model):
        try:
            transaction = Transactions(users_id=1, transaction_type='DELETE', plants_id=model.id, ignore=False)
            self.session.add(transaction)
            self.session.commit()
            return True
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to delete record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to delete record.')

            self.session.rollback()

            return False

class Actions(db.Model):
    __tablename__ = 'actions'

    id = db.Column(db.Integer, primary_key=True)
    transactions_id = db.Column(db.Integer, db.ForeignKey(u'transactions.id'))
    action_type = db.Column(db.String)
    regions_id = db.Column(db.Integer, db.ForeignKey(u'regions.id'))
    property = db.Column(db.String)
    value = db.Column(db.String)
    citation = db.Column(db.String)

    region = db.relationship('Regions')

    def __str__(self):
        return str(self.id)

class ActiveGrowthPeriod(db.Model):
    __tablename__ = 'active_growth_period'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class Allelopathic(db.Model):
    __tablename__ = 'allelopathic'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class Animals(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class BiochemicalMaterialProd(db.Model):
    __tablename__ = 'biochemical_material_prod'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class CanopyDensity(db.Model):
    __tablename__ = 'canopy_density'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class CulturalAndAmenityProd(db.Model):
    __tablename__ = 'cultural_and_amenity_prod'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class DroughtTol(db.Model):
    __tablename__ = 'drought_tol'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    description = db.Column(db.String)

    def __str__(self):
        return self.value

class Duration(db.Model):
    __tablename__ = 'duration'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class EndemicStatus(db.Model):
    __tablename__ = 'endemic_status'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class ErosionControl(db.Model):
    __tablename__ = 'erosion_control'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class Family(db.Model):
    __tablename__ = 'family'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, value):
        self.plant = plant
        self.value = value

    def __str__(self):
        return self.value

class FamilyCommonName(db.Model):
    __tablename__ = 'family_common_name'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, value):
        self.plant = plant
        self.value = value

    def __str__(self):
        return self.value

class FertilityNeeds(db.Model):
    __tablename__ = 'fertility_needs'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class FireTol(db.Model):
    __tablename__ = 'fire_tol'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class FloodTol(db.Model):
    __tablename__ = 'flood_tol'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    description = db.Column(db.String)

    def __str__(self):
        return self.value

class FlowerColor(db.Model):
    __tablename__ = 'flower_color'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class FoliageColor(db.Model):
    __tablename__ = 'foliage_color'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class FoodProd(db.Model):
    __tablename__ = 'food_prod'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class FruitColor(db.Model):
    __tablename__ = 'fruit_color'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class HarvestPeriod(db.Model):
    __tablename__ = 'harvest_period'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

#class HeightAtMaturity(db.Model):
#    __tablename__ = 'plants_height_at_maturity_by_region'

#    id = db.Column(db.Integer, primary_key=True)

#    def __str__(self):
#        return 'update code to make this display properly'

class HumidityTol(db.Model):
    __tablename__ = 'humidity_tol'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    description = db.Column(db.String)

    def __str__(self):
        return self.value

class Insects(db.Model):
    __tablename__ = 'insects'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class Layer(db.Model):
    __tablename__ = 'layer'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class LeafRetention(db.Model):
    __tablename__ = 'leaf_retention'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class Lifespan(db.Model):
    __tablename__ = 'lifespan'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    description = db.Column(db.String)

    def __str__(self):
        return self.value

class LivestockBloat(db.Model):
    __tablename__ = 'livestock_bloat'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class MedicinalsProd(db.Model):
    __tablename__ = 'medicinals_prod'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class MineralNutrientsProd(db.Model):
    __tablename__ = 'mineral_nutrients_prod'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class Plants(db.Model):
    __tablename__ = 'plants'
    __view__ = ModelViewAddToTransactions
    
    id = db.Column(db.Integer, primary_key=True)
    genus = db.Column(db.String)
    species = db.Column(db.String)
    common_name = db.Column(db.String)
    drought_tol_id = db.Column(db.Integer, db.ForeignKey(u'drought_tol.id'))
    flood_tol_id = db.Column(db.Integer, db.ForeignKey(u'flood_tol.id'))
    humidity_tol_id = db.Column(db.Integer, db.ForeignKey(u'humidity_tol.id'))
    salt_tol_id = db.Column(db.Integer, db.ForeignKey(u'salt_tol.id'))
    toxin_removal_id = db.Column(db.Integer, db.ForeignKey(u'toxin_removal.id'))
    wind_tol_id = db.Column(db.Integer, db.ForeignKey(u'wind_tol.id'))
    minimum_temperature_tol = db.Column(db.Integer)
    innoculant = db.Column(db.String)
    variety = db.Column(db.String)
    fire_tol_id = db.Column(db.Integer, db.ForeignKey(u'fire_tol.id'))
    livestock_bloat_id = db.Column(db.Integer, db.ForeignKey(u'livestock_bloat.id'))
    pH_min = db.Column(db.Numeric)
    pH_max = db.Column(db.Numeric)
    toxicity_id = db.Column(db.Integer, db.ForeignKey(u'toxicity.id'))
    lifespan_id = db.Column(db.Integer, db.ForeignKey(u'lifespan.id'))
    allelopathic_id = db.Column(db.Integer, db.ForeignKey(u'allelopathic.id'))

    def __str__(self):
        return '{0} {1} ({2})'.format(self.genus, self.species, self.common_name)

    biochemical_materials = db.relationship('PlantsBiochemicalMaterialProd', backref='plant')
    cultural_and_amenity_products = db.relationship('PlantsCulturalAndAmenityProd', backref='plant')
    families = db.relationship('Family', backref='plant')
    family_common_names = db.relationship('FamilyCommonName', backref='plant')
    flower_colors = db.relationship('PlantsFlowerColor', backref='plant')
    foliage_colors = db.relationship('PlantsFoliageColor', backref='plant')
    foods = db.relationship('PlantsFoodProd', backref='plant')
    fruit_colors = db.relationship('PlantsFruitColor', backref='plant')
    layers = db.relationship('PlantsLayer', backref='plant')
    medicinals = db.relationship('PlantsMedicinalsProd', backref='plant')
    mineral_nutrients = db.relationship('PlantsMineralNutrientsProd', backref='plant')
    raw_materials = db.relationship('PlantsRawMaterialsProd', backref='plant')
    url_tags = db.relationship('UrlTags', backref='plant')
    

    #endemic_statuses_proxy = association_proxy('endemic_statuses', 'endemic_status')

class PlantsActiveGrowthPeriodByRegion(db.Model):
    __tablename__ = 'plants_active_growth_period_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    active_growth_period_id = db.Column(db.Integer, db.ForeignKey('active_growth_period.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'active_growth_period_by_region')
    active_growth_period = db.relationship(ActiveGrowthPeriod)
    region = db.relationship('Regions')

    def __init__(self, plant, region, active_growth_period_id):
        self.plant = plant
        self.region = region
        self.active_growth_period_id = active_growth_period_id

class PlantsAnimalAttractorByRegion(db.Model):
    __tablename__ = 'plants_animal_attractor_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    animals_id = db.Column(db.Integer, db.ForeignKey('animals.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'animal_attractor_by_region')
    animal = db.relationship(Animals)
    region = db.relationship('Regions')

    def __init__(self, plant, region, animals_id):
        self.plant = plant
        self.region = region
        self.animals_id = animals_id

class PlantsAnimalRegulatorByRegion(db.Model):
    __tablename__ = 'plants_animal_regulator_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    animals_id = db.Column(db.Integer, db.ForeignKey('animals.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'animal_regulator_by_region')
    animal = db.relationship(Animals)
    region = db.relationship('Regions')

    def __init__(self, plant, region, animals_id):
        self.plant = plant
        self.region = region
        self.animals_id = animals_id

class PlantsBiochemicalMaterialProd(db.Model):
    __tablename__ = 'plants_biochemical_material_prod'

    id = db.Column(db.Integer, primary_key=True)
    biochemical_material_prod_id = db.Column(db.Integer, db.ForeignKey('biochemical_material_prod.id'))
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, biochemical_material_prod_id):
        self.plant = plant
        self.biochemical_material_prod_id = biochemical_material_prod_id

class PlantsCanopyDensityByRegion(db.Model):
    __tablename__ = 'plants_canopy_density_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    canopy_density_id = db.Column(db.Integer, db.ForeignKey('canopy_density.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'canopy_density_by_region')
    canopy_density = db.relationship(CanopyDensity)
    region = db.relationship('Regions')

    def __init__(self, plant, region, canopy_density_id):
        self.plant = plant
        self.region = region
        self.canopy_density_id = canopy_density_id

class PlantsCulturalAndAmenityProd(db.Model):
    __tablename__ = 'plants_cultural_and_amenity_prod'

    id = db.Column(db.Integer, primary_key=True)
    cultural_and_amenity_prod_id = db.Column(db.Integer, db.ForeignKey('cultural_and_amenity_prod.id'))
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, cultural_and_amenity_prod_id):
        self.plant = plant
        self.cultural_and_amenity_prod_id = cultural_and_amenity_prod_id

class PlantsDurationByRegion(db.Model):
    __tablename__ = 'plants_duration_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    duration_id = db.Column(db.Integer, db.ForeignKey('duration.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'duration_by_region')
    duration = db.relationship(Duration)
    region = db.relationship('Regions')

    def __init__(self, plant, region, duration_id):
        self.plant = plant
        self.region = region
        self.duration_id = duration_id

class PlantsEndemicStatusByRegion(db.Model):
    __tablename__ = 'plants_endemic_status_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    endemic_status_id = db.Column(db.Integer, db.ForeignKey('endemic_status.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'endemic_status_by_region')
    endemic_status = db.relationship(EndemicStatus)
    region = db.relationship('Regions')

    def __init__(self, plant, region, endemic_status_id):
        self.plant = plant
        self.region = region
        self.endemic_status_id = endemic_status_id

class PlantsErosionControlByRegion(db.Model):
    __tablename__ = 'plants_erosion_control_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    erosion_control_id = db.Column(db.Integer, db.ForeignKey('erosion_control.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'erosion_control_by_region')
    erosion_control = db.relationship(ErosionControl)
    region = db.relationship('Regions')

    def __init__(self, plant, region, erosion_control_id):
        self.plant = plant
        self.region = region
        self.erosion_control_id = erosion_control_id

class PlantsFertilityNeedsByRegion(db.Model):
    __tablename__ = 'plants_fertility_needs_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    fertility_needs_id = db.Column(db.Integer, db.ForeignKey('fertility_needs.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'fertility_needs_by_region')
    fertility_needs = db.relationship(FertilityNeeds)
    region = db.relationship('Regions')

    def __init__(self, plant, region, fertility_needs_id):
        self.plant = plant
        self.region = region
        self.fertility_needs_id = fertility_needs_id

class PlantsFlowerColor(db.Model):
    __tablename__ = 'plants_flower_color'

    id = db.Column(db.Integer, primary_key=True,)
    flower_color_id = db.Column(db.Integer, db.ForeignKey('flower_color.id'))
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, flower_color_id):
        self.plant = plant
        self.flower_color_id = flower_color_id

class PlantsFoliageColor(db.Model):
    __tablename__ = 'plants_foliage_color'

    id = db.Column(db.Integer, primary_key=True)
    foliage_color_id = db.Column(db.Integer, db.ForeignKey('foliage_color.id'))
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, foliage_color_id):
        self.plant = plant
        self.foliage_color_id = foliage_color_id

class PlantsFoodProd(db.Model):
    __tablename__ = 'plants_food_prod'

    id = db.Column(db.Integer, primary_key=True)
    food_prod_id = db.Column(db.Integer, db.ForeignKey('food_prod.id'))
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, food_prod_id):
        self.plant = plant
        self.food_prod_id = food_prod_id

class PlantsFruitColor(db.Model):
    __tablename__ = 'plants_fruit_color'

    id = db.Column(db.Integer, primary_key=True)
    fruit_color_id = db.Column(db.Integer, db.ForeignKey('fruit_color.id'))
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, fruit_color_id):
        self.plant = plant
        self.fruit_color_id = fruit_color_id

class PlantsHarvestPeriodByRegion(db.Model):
    __tablename__ = 'plants_harvest_period_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    harvest_period_id = db.Column(db.Integer, db.ForeignKey('harvest_period.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'harvest_period_by_region')
    harvest_period = db.relationship(HarvestPeriod)
    region = db.relationship('Regions')

    def __init__(self, plant, region, harvest_period_id):
        self.plant = plant
        self.region = region
        self.harvest_period_id = harvest_period_id

class PlantsHeightAtMaturityByRegion(db.Model):
    __tablename__ = 'plants_height_at_maturity_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    height = db.Column(db.Integer)
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'height_at_maturity_by_region')
    region = db.relationship('Regions')

    def __init__(self, plant, region, height):
        self.plant = plant
        self.region = region
        self.height = height

class PlantsInsectAttractorByRegion(db.Model):
    __tablename__ = 'plants_insect_attractor_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    insects_id = db.Column(db.Integer, db.ForeignKey('insects.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'insect_attractor_by_region')
    insect = db.relationship(Insects)
    region = db.relationship('Regions')

    def __init__(self, plant, region, insects_id):
        self.plant = plant
        self.region = region
        self.insects_id = insects_id

class PlantsInsectRegulatorByRegion(db.Model):
    __tablename__ = 'plants_insect_regulator_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    insects_id = db.Column(db.Integer, db.ForeignKey('insects.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'insect_regulator_by_region')
    insect = db.relationship(Insects)
    region = db.relationship('Regions')

    def __init__(self, plant, region, insects_id):
        self.plant = plant
        self.region = region
        self.insects_id = insects_id

class PlantsLayer(db.Model):
    __tablename__ = 'plants_layer'

    id = db.Column(db.Integer, primary_key=True)
    layer_id = db.Column(db.Integer, db.ForeignKey('layer.id'))
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, layer_id):
        self.plant = plant
        self.layer_id = layer_id

class PlantsLeafRetentionByRegion(db.Model):
    __tablename__ = 'plants_leaf_retention_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    leaf_retention_id = db.Column(db.Integer, db.ForeignKey('leaf_retention.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'leaf_retention_by_region')
    leaf_retention = db.relationship(LeafRetention)
    region = db.relationship('Regions')

    def __init__(self, plant, region, leaf_retention_id):
        self.plant = plant
        self.region = region
        self.leaf_retention_id = leaf_retention_id

class PlantsMedicinalsProd(db.Model):
    __tablename__ = 'plants_medicinals_prod'

    id = db.Column(db.Integer, primary_key=True)
    medicinals_prod_id = db.Column(db.Integer, db.ForeignKey('medicinals_prod.id'))
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, medicinals_prod_id):
        self.plant = plant
        self.medicinals_prod_id = medicinals_prod_id

class PlantsMineralNutrientsProd(db.Model):
    __tablename__ = 'plants_mineral_nutrients_prod'

    id = db.Column(db.Integer, primary_key=True)
    mineral_nutrients_prod_id = db.Column(db.Integer, db.ForeignKey('mineral_nutrients_prod.id'))
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, mineral_nutrients_prod_id):
        self.plant = plant
        self.mineral_nutrients_prod_id = mineral_nutrients_prod_id

class PlantsRawMaterialsProd(db.Model):
    __tablename__ = 'plants_raw_materials_prod'

    id = db.Column(db.Integer, primary_key=True)
    raw_materials_prod_id = db.Column(db.Integer, db.ForeignKey('raw_materials_prod.id'))
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, raw_materials_prod_id):
        self.plant = plant
        self.raw_materials_prod_id = raw_materials_prod_id

class PlantsShadeTolByRegion(db.Model):
    __tablename__ = 'plants_shade_tol_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    shade_tol_id = db.Column(db.Integer, db.ForeignKey('shade_tol.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'shade_tol_by_region')
    shade_tol = db.relationship('ShadeTol')
    region = db.relationship('Regions')

    def __init__(self, plant, region, shade_tol_id):
        self.plant = plant
        self.region = region
        self.shade_tol_id = shade_tol_id

class PlantsSoilDrainageTolByRegion(db.Model):
    __tablename__ = 'plants_soil_drainage_tol_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    soil_drainage_tol_id = db.Column(db.Integer, db.ForeignKey('soil_drainage_tol.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'soil_drainage_tol_by_region')
    soil_drainage_tol = db.relationship('SoilDrainageTol')
    region = db.relationship('Regions')

    def __init__(self, plant, region, soil_drainage_tol_id):
        self.plant = plant
        self.region = region
        self.soil_drainage_tol_id = soil_drainage_tol_id

class PlantsSpreadAtMaturityByRegion(db.Model):
    __tablename__ = 'plants_spread_at_maturity_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    spread = db.Column(db.Integer)
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'spread_at_maturity_by_region')
    region = db.relationship('Regions')

    def __init__(self, plant, region, spread):
        self.plant = plant
        self.region = region
        self.spread = spread

class PlantsSunNeedsByRegion(db.Model):
    __tablename__ = 'plants_sun_needs_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    sun_needs_id = db.Column(db.Integer, db.ForeignKey('sun_needs.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'sun_needs_by_region')
    sun_needs = db.relationship('SunNeeds')
    region = db.relationship('Regions')

    def __init__(self, plant, region, sun_needs_id):
        self.plant = plant
        self.region = region
        self.sun_needs_id = sun_needs_id

class PlantsWaterNeedsByRegion(db.Model):
    __tablename__ = 'plants_water_needs_by_region'

    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    water_needs_id = db.Column(db.Integer, db.ForeignKey('water_needs.id'))
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
    plant = db.relationship(Plants, backref = 'water_needs_by_region')
    water_needs = db.relationship('WaterNeeds')
    region = db.relationship('Regions')

    def __init__(self, plant, region, water_needs_id):
        self.plant = plant
        self.region = region
        self.water_needs_id = water_needs_id

class RawMaterialsProd(db.Model):
    __tablename__ = 'raw_materials_prod'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class Regions(db.Model):
    __tablename__ = 'regions'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class SaltTol(db.Model):
    __tablename__ = 'salt_tol'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    description = db.Column(db.String)

    def __str__(self):
        return self.value

class ShadeTol(db.Model):
    __tablename__ = 'shade_tol'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class SoilDrainageTol(db.Model):
    __tablename__ = 'soil_drainage_tol'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    description = db.Column(db.String)

    def __str__(self):
        return self.value

#class SpreadAtMaturity(db.Model):
#    __tablename__ = 'plants_spread_at_maturity_by_region'

#    id = db.Column(db.Integer, primary_key=True)

#    def __str__(self):
#        return 'update code to make this display properly'

class SunNeeds(db.Model):
    __tablename__ = 'sun_needs'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class Toxicity(db.Model):
    __tablename__ = 'toxicity'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class ToxinRemoval(db.Model):
    __tablename__ = 'toxin_removal'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class Transactions(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=False), server_default="timezone('utc'::text, now())")
    users_id = db.Column(db.Integer, db.ForeignKey(u'users.id'))
    transaction_type = db.Column(db.String)
    plants_id = db.Column(db.Integer, db.ForeignKey(u'plants.id'))
    ignore = db.Column(db.Boolean)

    actions = db.relationship(Actions, backref='transaction')
    user = db.relationship('Users')
    plant = db.relationship('Plants')

    def __str__(self):
        return str(self.id)

class UrlTags(db.Model):
    __tablename__ = 'url_tags'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))

    def __init__(self, plant, region, value):
        self.plant = plant
        self.value = value

    def __str__(self):
        return self.value

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    creation_timestamp = db.Column(db.DateTime)
    email = db.Column(db.String)
    enabled = db.Column(db.Boolean)
    real_name = db.Column(db.String)

    def __str__(self):
        return self.username

class WaterNeeds(db.Model):
    __tablename__ = 'water_needs'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)

    def __str__(self):
        return self.value

class WindTol(db.Model):
    __tablename__ = 'wind_tol'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    description = db.Column(db.String)

    def __str__(self):
        return self.value