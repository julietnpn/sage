import time
from flask.ext.admin.contrib.sqla import ModelView
from sandman import app, db
from sandman.model import activate, register, Model
from sqlalchemy import inspect
from sqlalchemy.orm.attributes import get_history, instance_state
#from sqlalchemy.ext.associationproxy import association_proxy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:plants@localhost/plants'

properties_1_to_1 = ['genus',
                     'species',
                     'common_name',
                     'biochemical_material_prod_id',
                     'cultural_and_amenity_prod_id',
                     'drought_tol_id',
                     'family_id',
                     'flood_tol_id',
                     'food_prod_id',
                     'humidity_tol_id',
                     'layer_id',
                     'medicinals_prod_id',
                     'raw_materials_prod_id',
                     'salt_tol_id',
                     'toxin_removal_id',
                     'wind_tol_id',
                     'minimum_temperature_tol',
                     'pH',
                     'innoculant',
                     'variety',
                     'mineral_nutrients_prod_id',
                     'fire_tol_id']

rel_plants_to_active_growth_period = db.Table('plants_active_growth_period_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('active_growth_period_id', db.ForeignKey(u'active_growth_period.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_animal_attractor = db.Table('plants_animal_attractor_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('animals_id', db.ForeignKey(u'animals.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_animal_regulator = db.Table('plants_animal_regulator_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('animals_id', db.ForeignKey(u'animals.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_canopy_density = db.Table('plants_canopy_density_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('canopy_density_id', db.ForeignKey(u'canopy_density.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_duration = db.Table('plants_duration_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('duration_id', db.ForeignKey(u'duration.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_endemic_status = db.Table('plants_endemic_status_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('endemic_status_id', db.ForeignKey(u'endemic_status.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_erosion_control = db.Table('plants_erosion_control_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('erosion_control_id', db.ForeignKey(u'erosion_control.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_fertility_needs = db.Table('plants_fertility_needs_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('fertility_needs_id', db.ForeignKey(u'fertility_needs.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_harvest_period = db.Table('plants_harvest_period_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('harvest_period_id', db.ForeignKey(u'harvest_period.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_height_at_maturity = db.Table('plants_height_at_maturity_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_insect_attractor = db.Table('plants_insect_attractor_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('insects_id', db.ForeignKey(u'insects.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_insect_regulator = db.Table('plants_insect_regulator_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('insects_id', db.ForeignKey(u'insects.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_leaf_retention = db.Table('plants_leaf_retention_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('leaf_retention_id', db.ForeignKey(u'leaf_retention.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_shade_tol = db.Table('plants_shade_tol_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('shade_tol_id', db.ForeignKey(u'shade_tol.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_soil_drainage_tol = db.Table('plants_soil_drainage_tol_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('soil_drainage_tol_id', db.ForeignKey(u'soil_drainage_tol.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_spread_at_maturity = db.Table('plants_spread_at_maturity_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_sun_needs = db.Table('plants_sun_needs_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('sun_needs_id', db.ForeignKey(u'sun_needs.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

rel_plants_to_water_needs = db.Table('plants_water_needs_by_region',
                                     db.Column('plants_id', db.ForeignKey(u'plants.id'), nullable=False, index=True),
                                     db.Column('water_needs_id', db.ForeignKey(u'water_needs.id'), nullable=False, index=True),
                                     db.Column('regions_id', db.ForeignKey(u'regions.id'), nullable=False, index=True))

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

    def __str__(self):
        return str(self.id)

class ActiveGrowthPeriod(db.Model):
    __view__ = ModelViewAddToTransactions
    __tablename__ = 'active_growth_period'

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

class FoodProd(db.Model):
    __tablename__ = 'food_prod'

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
    biochemical_material_prod_id = db.Column(db.Integer, db.ForeignKey(u'biochemical_material_prod.id'))
    cultural_and_amenity_prod_id = db.Column(db.Integer, db.ForeignKey(u'cultural_and_amenity_prod.id'))
    drought_tol_id = db.Column(db.Integer, db.ForeignKey(u'drought_tol.id'))
    family_id = db.Column(db.Integer, db.ForeignKey(u'family.id'))
    flood_tol_id = db.Column(db.Integer, db.ForeignKey(u'flood_tol.id'))
    food_prod_id = db.Column(db.Integer, db.ForeignKey(u'food_prod.id'))
    humidity_tol_id = db.Column(db.Integer, db.ForeignKey(u'humidity_tol.id'))
    layer_id = db.Column(db.Integer, db.ForeignKey(u'layer.id'))
    medicinals_prod_id = db.Column(db.Integer, db.ForeignKey(u'medicinals_prod.id'))
    raw_materials_prod_id = db.Column(db.Integer, db.ForeignKey(u'raw_materials_prod.id'))
    salt_tol_id = db.Column(db.Integer, db.ForeignKey(u'salt_tol.id'))
    toxin_removal_id = db.Column(db.Integer, db.ForeignKey(u'toxin_removal.id'))
    wind_tol_id = db.Column(db.Integer, db.ForeignKey(u'wind_tol.id'))
    minimum_temperature_tol = db.Column(db.Integer)
    pH = db.Column(db.Numeric)
    innoculant = db.Column(db.String)
    variety = db.Column(db.String)
    mineral_nutrients_prod_id = db.Column(db.Integer, db.ForeignKey(u'mineral_nutrients_prod.id'))
    fire_tol_id = db.Column(db.Integer, db.ForeignKey(u'fire_tol.id'))


    active_growth_period = db.relationship('ActiveGrowthPeriod', secondary=rel_plants_to_active_growth_period)
    animal_attractor = db.relationship('Animals', secondary=rel_plants_to_animal_attractor)
    animal_regulator = db.relationship('Animals', secondary=rel_plants_to_animal_regulator)
    canopy_density = db.relationship('CanopyDensity', secondary=rel_plants_to_canopy_density)
    duration = db.relationship('Duration', secondary=rel_plants_to_duration)
    endemic_status = db.relationship('EndemicStatus', secondary=rel_plants_to_endemic_status)
    erosion_control = db.relationship('ErosionControl', secondary=rel_plants_to_erosion_control)
    height_at_maturity = db.relationship('Regions', secondary=rel_plants_to_height_at_maturity)
    fertility_needs = db.relationship('FertilityNeeds', secondary=rel_plants_to_fertility_needs)
    harvest_period = db.relationship('HarvestPeriod', secondary=rel_plants_to_harvest_period)
    insect_attractor = db.relationship('Insects', secondary=rel_plants_to_insect_attractor)
    insect_regulator = db.relationship('Insects', secondary=rel_plants_to_insect_regulator)
    leaf_retention = db.relationship('LeafRetention', secondary=rel_plants_to_leaf_retention)
    shade_tol = db.relationship('ShadeTol', secondary=rel_plants_to_shade_tol)
    soil_drainage_tol = db.relationship('SoilDrainageTol', secondary=rel_plants_to_soil_drainage_tol)
    spread_at_maturity = db.relationship('Regions', secondary=rel_plants_to_spread_at_maturity)
    sun_needs = db.relationship('SunNeeds', secondary=rel_plants_to_sun_needs)
    water_needs = db.relationship('WaterNeeds', secondary=rel_plants_to_water_needs)

    def __str__(self):
      return '{0} {1} ({2})'.format(self.genus, self.species, self.common_name)

    #transactions = db.relationship('Transactions', backref='plant')

    #endemic_statuses_proxy = association_proxy('endemic_statuses', 'endemic_status')

#class PlantsEndemicStatusByRegion(db.Model):
#    __tablename__ = 'plants_endemic_status_by_region'

#    id = db.Column(db.Integer, primary_key=True)
#    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
#    endemic_status_id = db.Column(db.Integer, db.ForeignKey('endemic_status.id'))
#    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    
#    plant = db.relationship(Plants, backref = 'endemic_statuses')
#    endemic_status = db.relationship(EndemicStatus)

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

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

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

register((Actions,
          ActiveGrowthPeriod,
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
          HarvestPeriod,
          HumidityTol,
          Insects,
          Layer,
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
          Transactions,
          Users,
          WaterNeeds,
          WindTol))


def delete_plants():
  Plants.query.delete()
  db.session.commit()

def process_transactions():
  for transaction in Transactions.query.filter_by(ignore=False).order_by(Transactions.id).all():
    print 'transaction type=' + transaction.transaction_type
    print 'transaction type=' + str(transaction.plants_id)
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
      if action.property not in properties_1_to_1:
        db.session.rollback()
        raise ValueError("Invalid property = " + action.property)
      print('T_id={0}, property={1}, value={2}'.format(transaction.id, action.property, action.value))
      setattr(transaction.plant, action.property, action.value)
    db.session.commit()
    #time.sleep(30)

#delete_plants()
process_transactions()


print('ACTIVATE')
activate(browser=True)
print('RUN')
app.run(debug=False)
