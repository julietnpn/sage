import csv
from models import *
from sandman import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:plants@localhost/plants'

def read_plants(filename):
    plants = {}
    with open(filename, 'rU') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            yield row

for plant in read_plants(r"C:\Users\John\Dropbox\research\CyberSEES\usda.orange.for_import.csv"):
    transaction = Transactions(users_id=1, transaction_type='INSERT', ignore=False)
    actions = []

    # 1. Don't import the entry if the Scientific Name is one word. (e.g., 'Ambrosia' versus 'Ambrosia acanthicarpa')
    if len(plant['Scientific Name'].split()) == 1:
        continue

    # 2. genus = first word in scientific name, species = second word in scientific name
    actions.append(Actions(transaction=transaction, action_type='UPDATE', property='genus', value=plant['Scientific Name'].split()[0]))
    actions.append(Actions(transaction=transaction, action_type='UPDATE', property='species', value=plant['Scientific Name'].split()[1]))

    # 3. add field for Family Common Name
    if plant['Family Common Name'].strip():
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='family_common_name', value=plant['Family Common Name'].strip()))

    # 4. add field for Family
    if plant['Family'].strip():
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='family', value=plant['Family'].strip()))

    # 5. duration = duration
    durations = []
    if 'Perennial' in plant['Duration']:
        durations.append('perennial')
    if 'Annual' in plant['Duration']:
        durations.append('annual')
    if 'Biennial' in plant['Duration']:
        durations.append('biennial')
    for duration in durations:
        duration_id = Duration.query.filter_by(value=duration).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='duration', value=duration_id))

    # 6. Growth Habit data is mapped to Layer (ALSO IMPLEMENTS #23)
    #    Forb/herb translates to herb
    #    Vine translates to climber
    #    Graminoid translates to ground cover
    #    Tree translates to understory and climax
    #    Subshrub translates to shrub
    growth_habit_map = {'Forb/herb': {'herb'},
                        'Vine': {'climber'},
                        'Graminoid': {'ground cover'},
                        'Tree': {'understory', 'climax'},
                        'Shrub': {'shrub'},
                        'Subshrub': {'shrub'}}
    shape_and_orientation_map = {'Prostrate': {'ground cover'},
                                 'Climbing': {'climber'},
                                 'Decumbent': {'ground cover', 'herb'}}
    values_to_store = set()
    #if plant['Growth Habit'].strip():
    #    values_to_store.union(growth_habit_map[plant['Growth Habit'].strip()])
    #if plant['Shape and Orientation'].strip():
    #    values_to_store.union(shape_and_orientation_map[plant['Shape and Orientation'].strip()])
    #for value in values_to_store:
    #    layer_id = Layer.query.filter_by(value=value).first().id
    #    actions.append(Actions(transaction=transaction, action_type='UPDATE', property='layer', value=layer_id))

    # 7. Urls found in Fact Sheets and Plant Guides should be stored into the url tags
    if plant['Fact Sheets'].strip():
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='url_tags', value=plant['Fact Sheets'].strip()))
    if plant['Plant Guides'].strip():
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='url_tags', value=plant['Plant Guides'].strip()))

    # 8. You only have to fill in the remaining data for the plant if Characteristics Data = yes
    #    (i.e., you can move on to the next entry if it does not say yes).
    if plant['Characteristics Data'].strip() != 'Yes':
        db.session.add_all(actions)
        db.session.commit()
        continue

    # 9. Cultivar translates to Variety
    if plant['Cultivar Name'].strip():
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='variety', value=plant['Cultivar Name'].strip()))

    # 10. Active growth period maps to active growth period as is.
    seasons = []
    if 'Spring' in plant['Active Growth Period']:
        seasons.append('spring')
    if 'Summer' in plant['Active Growth Period']:
        seasons.append('summer')
    if 'Fall' in plant['Active Growth Period']:
        seasons.append('autumn')
    if 'Winter' in plant['Active Growth Period']:
        seasons.append('winter')

    for season in seasons:
        active_growth_period_id = ActiveGrowthPeriod.query.filter_by(value=season).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='active_growth_period', value=active_growth_period_id))

    # 11. add livestock bloat as a behavior. Values: none, low, medium, high.
    if plant['Bloat'].strip():
        livestock_bloat_id = LivestockBloat.query.filter_by(value=plant['Bloat'].strip().lower()).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='livestock_bloat_id', value=livestock_bloat_id))

    # 12. coppice potential with value yes translates to raw materials = biomass
    if plant['Coppice Potential'].strip() == 'Yes':
        raw_materials_prod_id = RawMaterialsProd.query.filter_by(value='biomass').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='raw_materials_prod', value=raw_materials_prod_id))

    # 13. fire resistance translates with value yes translates to fire tolerance = resistant to fire,
    #     and with value no translates to fire tolerance = not resistant to fire
    if plant['Fire Resistance'].strip():
        fire_resistance_map = {'Yes': 'resistant to fire',
                               'No': 'not resistant to fire'}
        fire_tol_id = FireTol.query.filter_by(value=fire_resistance_map[plant['Fire Resistance'].strip()]).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='fire_tol_id', value=fire_tol_id))

    # 14. add flower color table with values: DONE
    #   Blue
    #   Brown
    #   Green
    #   Orange
    #   Purple
    #   Red
    #   White
    #   Yellow

    # 15. add foliage color table with values: DONE
    #   Dark Green
    #   Green
    #   Gray-Green
    #   Red
    #   White-Gray
    #   Yellow-Green
    #add fruit color table with values: DONE
    #   Black
    #   Blue
    #   Brown
    #   Green
    #   Orange
    #   Purple
    #   Red
    #   White
    #   Yellow

    # 16. flower color, fruit color, and foliage color map to our database exactly
    if plant['Flower Color'].strip():
        flower_color_id = FlowerColor.query.filter_by(value=plant['Flower Color'].strip().lower()).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='flower color', value=flower_color_id))
    if plant['Fruit Color'].strip():
        fruit_color_id = FruitColor.query.filter_by(value=plant['Fruit Color'].strip().lower()).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='fruit color', value=fruit_color_id))
    if plant['Foliage Color'].strip():
        foliage_color_id = FoliageColor.query.filter_by(value=plant['Foliage Color'].strip().lower()).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='foliage color', value=foliage_color_id))

    # 17. if flower conspicuous is yes or fruit conspicuous is yes then put it in our db as cultural and amenity = aesthetic
    if plant['Flower Conspicuous'].strip() == 'Yes' or plant['Fruit Conspicuous'].strip() == 'Yes':
        cultural_and_amenity_prod_id = CulturalAndAmenityProd.query.filter_by(value='aesthetic').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))

    # 18. foliage porosity summer maps to canopy density
    #     porous maps to sparse
    #     moderate maps to moderate
    #     dense maps to dense
    if plant['Foliage Porosity Summer'].strip():
        foliage_porosit_summer_map = {'Porous': 'sparse',
                                      'Moderate': 'moderate',
                                      'Dense': 'dense'}
        canopy_density_id = CanopyDensity.query.filter_by(value=foliage_porosit_summer_map[plant['Foliage Porosity Summer'].strip()]).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='canopy_density', value=canopy_density_id))

    # 19. Height, mature maps to height at maturity in feet (no unit change)
    if plant['Height, Mature (feet)'].strip():
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='height_at_maturity', value=float(plant['Height, Mature (feet)'].strip())))

    # 20. leaf retention yes maps to evergreen, leaf retention no maps to deciduous
    if plant['Leaf Retention'].strip():
        leaf_retention_map = {'Yes': 'evergreen',
                               'No': 'deciduous'}
        leaf_retention_id = LeafRetention.query.filter_by(value=leaf_retention_map[plant['Leaf Retention'].strip()]).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='leaf_retention', value=leaf_retention_id))

    # 21. add Allelopathic table with values yes and no
    #     add lifespan table
    #     values: short; moderate; long;
    #     descriptions: less than 100 years;  100 - 250 years; greater than 250 years
    if plant['Known Allelopath'].strip():
        allelopathic_id = Allelopathic.query.filter_by(value=plant['Known Allelopath'].strip().lower()).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='allelopathic', value=allelopathic_id))
    if plant['Lifespan'].strip():
        lifespan_id = Lifespan.query.filter_by(value=plant['Lifespan'].strip().lower()).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='lifespan', value=lifespan_id))

    # 22. if Nitrogen Fixation is low, medium, or high then it maps to mineral nutrients = nitrogen
    if plant['Nitrogen Fixation'].strip() in ['Low', 'Medium', 'High']:
        mineral_nutrients_prod_id = MineralNutrientsProd.query.filter_by(value='nitrogen').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='mineral_nutrients_prod', value=mineral_nutrients_prod_id))

    # 23. if shape and orientation is: DONE (implemented as part of #6)
    #       prostrate then layer = ground cover
    #       climbing then layer = climber
    #       decumbent = ground cover and herb


    # 24. add toxicity table with values: human and livestock toxicity
    #       none
    #       slight
    #       moderate
    #       severe
    # and map directly with usda toxicity
    if plant['Toxicity'].strip():
        toxicity_id = Toxicity.query.filter_by(value=plant['Toxicity'].strip().lower()).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='toxicity', value=toxicity_id))

    # 26. fertility requirement maps directly (NOTE FROM JOHN: 'Medium' needs to be mapped to 'Moderate')
    if plant['Fertility Requirement'].strip():
        fertility_requirement_map = {'Low': 'low',
                                     'Medium': 'moderate',
                                     'High': 'high'}
        fertility_needs_id = FertilityNeeds.query.filter_by(value=fertility_requirement_map[plant['Fertility Requirement'].strip()]).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='fertility_needs', value=fertility_needs_id))

    # 27. IGNORE

    # 28. moisture use maps to water requirements
    if plant['Moisture Use'].strip():
        moisture_use_map = {'Low': 'low',
                            'Medium': 'moderate',
                            'High': 'high'}
        water_needs_id = WaterNeeds.query.filter_by(value=moisture_use_map[plant['Moisture Use'].strip()]).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='water_needs', value=water_needs_id))

    # 29. ph Maximum and ph Minimum map directly to our db (need to create max and min values though).
    if plant['pH (Minimum)'].strip():
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='pH_min', value=float(plant['pH (Minimum)'].strip())))
    if plant['pH (Maximum)'].strip():
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='pH_max', value=float(plant['pH (Maximum)'].strip())))


    # 30. salinity tolerance maps to salt tolerance
    #     shade tolerance maps like:
    #       intolerant to no shade
    #       intermediate to partial shade and light shade
    #       tolerant to permanent deep shade, permanent shade, partial shade, and light shade
    if plant['Salinity Tolerance'].strip():
        salinity_tolerance_map = {'None': 'not salt-tolerant',
                                  'Low': 'slightly salt-tolerant',
                                  'Medium': 'moderately salt-tolerant',
                                  'High': 'salt-tolerant'}
        salt_tol_id = SaltTol.query.filter_by(value=salinity_tolerance_map[plant['Salinity Tolerance'].strip()]).first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='salt_tol_id', value=salt_tol_id))
    if plant['Shade Tolerance'].strip():
        shade_tols = []
        if plant['Shade Tolerance'].strip() == 'Intolerant':
            shade_tols.append('no shade')
        elif plant['Shade Tolerance'].strip() == 'Intermediate':
            shade_tols.append('partial shade')
            shade_tols.append('light shade')
        elif plant['Shade Tolerance'].strip() == 'Tolerant':
            shade_tols.append('permanent deep shade')
            shade_tols.append('permanent shade')
            shade_tols.append('partial shade')
            shade_tols.append('light shade')
        else:
            raise ValueError('Need to add handling for Shade Tolerance = ' + plant['Shade Tolerance'].strip())

        for shade_tol in shade_tols:
            shade_tol_id = ShadeTol.query.filter_by(value=shade_tol).first().id
            actions.append(Actions(transaction=transaction, action_type='UPDATE', property='shade_tol', value=shade_tol_id))

    # 31. fruit/seed period end maps to harvest period
    #     (year-round = spring, summer, fall and winter)
    if plant['Fruit/Seed Period End'].strip():
        seasons = []
        if plant['Fruit/Seed Period End'].strip() == 'Fall':
            seasons.append('autumn')
        elif plant['Fruit/Seed Period End'].strip() == 'Winter':
            seasons.append('winter')
        elif plant['Fruit/Seed Period End'].strip() == 'Spring':
            seasons.append('spring')
        elif plant['Fruit/Seed Period End'].strip() == 'Summer':
            seasons.append('summer')
        elif plant['Fruit/Seed Period End'].strip() == 'Year Round':
            seasons.append('autumn')
            seasons.append('winter')
            seasons.append('spring')
            seasons.append('summer')
        else:
            raise ValueError('Need to add handling for Fruit/Seed Period End = ' + plant['Fruit/Seed Period End'].strip())

        for season in seasons:
            harvest_period_id = HarvestPeriod.query.filter_by(value=season).first().id
            actions.append(Actions(transaction=transaction, action_type='UPDATE', property='harvest_period', value=harvest_period_id))

    # 32. berry/nut/seed product as yes maps to food: nuts and fruit
    if plant['Berry/Nut/Seed Product'].strip() == 'Yes':
        food_prod_id = FoodProd.query.filter_by(value='nuts').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='food_prod', value=food_prod_id))
        food_prod_id = FoodProd.query.filter_by(value='fruit').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='food_prod', value=food_prod_id))

    # 33. christmas tree product as yes maps to cultural and amenity : spiritual and religious inspiration
    if plant['Christmas Tree Product'].strip() == 'Yes':
        cultural_and_amenity_prod_id = CulturalAndAmenityProd.query.filter_by(value='spiritual and religious inspiration').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='cultural_and_amenity_prod', value=cultural_and_amenity_prod_id))

    # 34. add fodder as value to raw materials. DONE.
    # 35. fodder product as yes maps to raw materials: fodder
    if plant['Fodder Product'].strip() == 'Yes':
        raw_materials_prod_id = RawMaterialsProd.query.filter_by(value='fodder').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='raw_materials_prod', value=raw_materials_prod_id))

    # 36. fuelwood product as low, medium, or high maps to raw materials: fuel
    if plant['Fuelwood Product'].strip() in ['Low', 'Medium', 'High']:
        raw_materials_prod_id = RawMaterialsProd.query.filter_by(value='fuel').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='raw_materials_prod', value=raw_materials_prod_id))

    # 37. lumber product as yes maps to raw materials: timber
    if plant['Lumber Product'].strip() == 'Yes':
        raw_materials_prod_id = RawMaterialsProd.query.filter_by(value='timber').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='raw_materials_prod', value=raw_materials_prod_id))

    # 38. add naval store as value to raw material. DONE.
    # 39. naval store product as yes maps to raw material: naval store
    if plant['Naval Store Product'].strip() == 'Yes':
        raw_materials_prod_id = RawMaterialsProd.query.filter_by(value='naval store').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='raw_materials_prod', value=raw_materials_prod_id))

    # 40. map yes for post product to raw materials: timber
    if plant['Post Product'].strip() == 'Yes':
        raw_materials_prod_id = RawMaterialsProd.query.filter_by(value='timber').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='raw_materials_prod', value=raw_materials_prod_id))

    # 41. add pulpwood as value to raw materials. DONE.
    # 42. map yes for pulpwood as raw materials: pulpwood
    if plant['Pulpwood Product'].strip() == 'Yes':
        raw_materials_prod_id = RawMaterialsProd.query.filter_by(value='pulpwood').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='raw_materials_prod', value=raw_materials_prod_id))

    # 43. add veneer as value to raw materials. DONE.
    # 44. map yes for veneer as raw materials: veneer
    if plant['Veneer Product'].strip() == 'Yes':
        raw_materials_prod_id = RawMaterialsProd.query.filter_by(value='veneer').first().id
        actions.append(Actions(transaction=transaction, action_type='UPDATE', property='raw_materials_prod', value=raw_materials_prod_id))

    db.session.add_all(actions)
    db.session.commit()