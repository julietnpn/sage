from rest_framework import serializers
from plants.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    get_scientific_name = serializers.ReadOnlyField()
    common_name = serializers.CharField(required=False, allow_blank="True", max_length=300)
    endemic_status = serializers.StringRelatedField(many=True)
    
    #---------- Characteristics
    duration = serializers.StringRelatedField(many=True)
    life_span = serializers.DecimalField(max_digits=6, decimal_places=2)
    time_to_first_harvest = serializers.DecimalField(max_digits=6, decimal_places=2)
    #height =
    #spread = 
    #rootdepth =
    region= serializers.StringRelatedField(many=True)
    layer= serializers.StringRelatedField(many=True)
    canopy_density = serializers.StringRelatedField(many=True)
    active_growth_period = serializers.StringRelatedField(many=True)
    harvest_period = serializers.StringRelatedField(many=True)
    leaf_retention= serializers.StringRelatedField(many=True)
    flower_color= serializers.StringRelatedField(many=True)
    foliage_color= serializers.StringRelatedField(many=True)
    fruit_color= serializers.StringRelatedField(many=True)
    degree_of_serotiny = serializers.StringRelatedField(many=False)
    
    #---------- Tolerances
    shade_tol = serializers.StringRelatedField(many=True)
    salt_tol = serializers.StringRelatedField(many=False)
    flood_tol = serializers.StringRelatedField(many=False)
    drought_tol = serializers.StringRelatedField(many=False)
    humidity_tol = serializers.StringRelatedField(many=False)
    wind_tol = serializers.StringRelatedField(many=False)
    soil_drainage_tol = serializers.StringRelatedField(many=True)
    fire_tol = serializers.StringRelatedField(many=False)
    minimum_temperature_tol = serializers.IntegerField()
    heat_tol = serializers.IntegerField()
    
    #---------- Needs
    nutrient_requirements = serializers.StringRelatedField(many=True)
    water_needs = serializers.StringRelatedField(many=True)
    #inoculant
    sun_needs = serializers.StringRelatedField(many=True)
    serotiny = serializers.StringRelatedField(many=False)
    
    #---------- Products
    #allelochemicals
    food_prod = serializers.StringRelatedField(many=True)
    animal_food = serializers.StringRelatedField(many=True)
    raw_materials_prod = serializers.StringRelatedField(many=True)
    medicinals_prod = serializers.StringRelatedField(many=True)
    biochemical_material_prod = serializers.StringRelatedField(many=True)
    cultural_and_amenity_prod = serializers.StringRelatedField(many=True)
    mineral_nutrients_prod = serializers.StringRelatedField(many=True)
    
        #---------- Behaviors
    barrier = serializers.StringRelatedField(many=True)
    erosion_control = serializers.StringRelatedField(many=True)
    plants_insect_attractor = serializers.StringRelatedField(many=True)
    plants_insect_regulator = serializers.StringRelatedField(many=True)
    plants_animal_regulator = serializers.StringRelatedField(many=True)
    plants_animal_attractor = serializers.StringRelatedField(many=True)
    livestock_bloat = serializers.StringRelatedField(many=False)
    toxicity = serializers.StringRelatedField(many=False)
    toxin_removal = serializers.StringRelatedField(many=False)
    allelopathic = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Plant
        exclude = ["scientific_name"]


# class PlantSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     scientific_name = serializers.CharField(required=False, allow_blank="True")
#     common_name = serializers.CharField(required=False, allow_blank="True", max_length=300)
#     #endemic_status = serializers.ManyToManyField()
#     
#     #------- Characteristics ---------#
#     #duration = 
#     life_span = serializers.DecimalField(max_digits=6, decimal_places=2)
#     time_to_first_harvest = serializers.DecimalField(max_digits=6, decimal_places=2)
#     #region
#     pH_min = serializers.DecimalField(max_digits=3, decimal_places=2)
#     pH_max = serializers.DecimalField(max_digits=3, decimal_places=2)
#     ''' These are all many to many or foreignkey...
#     layer
#     canopy_density
#     active_growth_period
#     harvest_period
#     leaf_retention
#     flower_color
#     foliage_color
#     fruit_color
#     degree_of_serotiny
#     '''
#     
#     #--------- Tolerances ---------#
#     
#     
#     
#     
#     
#     
#     def create(self, validated_data):
#         return Plant.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.common_name = validated_data.get('common_name', instance.common_name)
#         instance.save()
#         return instance

