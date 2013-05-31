//use pfa_ca;
var library_list = [ "general_lib", "intrinsics_lib", "needs_lib", "products_lib", "behaviors_lib"];
var property_list = [];


//general

	property_list.push(["nutrients", "nutrients"]);
	v = [{value: "nitrogen"}, {value: "potassium"}, {value: "calcium"}, {value: "magnesium"}, {value: "sulfur"}, {value: "manganese"}, {value: "phosphorus"}, {value: "boron"}, {value: "zinc"}];
	db.nutrients.save(v);
	
	property_list.push(["animals", "animals"]);
	v=[{ value:"armadillos"}, {value:"possums"}, {value:"deer"}, {value:"squirrels"}, {value:"rabbits"}, {value:"black bear"}];
	db.animals.save(v);
	
	property_list.push(["insects", "insects"]);
	v=[{ value:"lady bug"}, {value:"ambrosia beetle"}, {value:"nematode"}, {value:"scales"}];
	db.insects.save(v);
	
	property_list.push(["endemic status", "endemic_status"]);
	v=[{ value:"native"}, {value:"naturalized"}, {value:"non-native"}, {value:"invasive"}, {value:"endangered"}, {value:"protected"}];
	db.endemic_status.save(v);
	
	property_list.push(["family names", "family_names"]);
	v=[{ value:"Fabaceae"}, {value:"Lauraceae"}, {value:"Rosaceae"}];
	db.family.save(v);
	
	//Must create library collection last so that population works properly//
	db.createCollection(library_list[0], {});
	
	var curLib = db.getCollection(library_list[0]);
	for(p in property_list){
		curEntry = db.getCollection(property_list[p][1]);
		doc = {property : property_list[p][0], collection : property_list[p][1]};
		curLib.insert(doc);
		/*
		var valueCursor = curEntry.find({},{_id:1} );
		valueCursor.forEach(
			function(doc){
				curLib.update(
					{property: property_list[p]},
					{'$push': {values : new DBRef(curEntry, doc._id)}}
				)
			}
		)*/
	}
	
	db.intrinsic_lib.find();
	
	property_list = [];
	
	


//intrinsics:
	/* Not sure how to handle this quite yet
	property_list.push("height range");
	v = [{value: "min"}, {value: "max"}];
	db.height_range.save(v);
	
	property_list.push("spread range");
	v = [{value: "min"}, {value: "max"}];
	db.spread_range.save(v);
	
	*/


	property_list.push(["layer", "layer"]);
	v = [{value: "climax"}, {value: "understory"}, {value: "shrub"}, {value: "herb"}, {value: "groundcover"}, {value: "climber"}, {value: "clumper"}, {value: "runner"}, {value: "palm"}, {value: "emergent palm"}, {value: "root crop"}];
	db.layer.save(v);
	
	property_list.push(["canopy density", "canopy_density"]);
	v = [{value: "impenetrable"}, {value: "dense"}, {value: "moderate"}, {value: "sparse"}, {value: "almost none"}];
	db.canopy_density.save(v);
	
	property_list.push(["shade tolerance", "shade_tol"]);
	v = [{value: "permanent deep shade"}, {value: "permanent shade"}, {value: "partial shade"}, {value: "light shade"}, {value: "no shade"}];
	db.shade_tol.save(v);

	property_list.push(["salt tolerance", "salt_tol"]);
	v = [{value: "salt-tolerant", description:"Highly resistant to salt drift and can be used in exposed environment."}, {value: "moderately salt-tolerant", description: "Tolerates some salt spray, but grow best when protected from it."}, {value: "slightly salt-tolerant", description: "Should be protected from any spray."}, {value: "not salt-tolerant"}];
	db.salt_tol.save(v);
	
	property_list.push(["flood tolerance", "flood_tol"]);
	v = [{value: "flood-tolerant", description:"Survives high water table and flooded conditions for days to weeks."}, {value: "moderately flood-tolerant", description: "Survives several days of excessively wet or flooded soil conditions."}, {value: "not flood-tolerant", description: "Not tolerant of wet or flooded soil."}];
	db.flood_tol.save(v);
	
	property_list.push(["drought tolerance", "drought_tol"]);
	v = [{value: "drought-tolerant", description: "Tolerates lack of water for a few days to several weeks."}, {value: "moderately drought-tolerant", description: "Can withstand several days of drought with some stress effects."}, {value: "not drought-tolerant", description: "May survive a few days of drought, but with severe damage."}];
	db.drought_tol.save(v);
	
	property_list.push(["humidity tolerance", "humidity_tol"]);
	v = [{value: "humidity-tolerant", description:"Can achieve normal growth in humidity greater than 70%."}, {value: "moderately humidity-tolerant", description: "Tolerates high humidity, but will decrease reproduction."}, {value: "not humidity-tolerant", description:"Cannot with stand high-humidity conditions and will incur damage."}];
	db.humidity_tol.save(v);
	
	property_list.push(["wind tolerance", "wind_tol"]);
	v = [{value: "very wind tolerant", description:"Can survive winds from 110-130 mph"}, {value: "moderately wind tolerant", description:"Can survive winds from 75-110mph"}, {value: "somewhat wind-tolerant", description:"Can survive winds from 55-75mph"}, {value: "not wind-tolerant", description:"Can survive winds less than 55mph"}];
	db.wind_tol.save(v);
	
	//Removing this b.c. I think it is redundant to flood tolerance
	/*property_list.push("soil drainage tolerance");
	v = [{value: "poor-drainage tolerant", description: "Wet to shallow depths most of the time."}, {value: "somewhat-poor-drainage tolerant", description: "periodic wetness at shallow depths due to seasonable weather or water conditions."}, {value: "moderate-drainage tolerant", description: "Soil is wet in root zone for short period of the year."}, {value: "well-drained tolerant", description: "Adequate water movement; root growth not restricted due to wetness"}, {value: "excessively-drained tolerance", description:"Soil doesn't retain adequate water for most plant growth following precipitation."}];
	db.soil_drainage_tol.save(v);*/
	
	property_list.push(["soil pH tolerance", "soil_pH_tol"]); 
	//specific for florida, what about ca?
	//v = [{value: "alkaline-tolerant", description:"greater than 6.0"}, {value: "small-range neutral", description: "5.8-6.3"}, {value:"wide-range neutral", description:"5.5-7.0"}, {value: "acidic", description "less than 5.5"}];
	//general ranges
	v = [{value: "alkaline-tolerant", description:"Can withstand pH greater than 8.5."}, {value: "slightly alkaline-tolerant", description: "Can withstand pH between  7-8.5"}, {value:"slightly acidic-tolerant", description:"Can withstand pH between 5.5-7."}, {value: "acidic-tolerant", description: "Can withstand pH less than 5.5"}];
	db.soil_pH_tol.save(v);
	
	
	//POINT TO GEN LIb
	property_list.push(["pest intolerance", "pest_intol"]);
	//DO GENERAL LIB FIRST?
	db.createCollection("pest_intol", {});
	
	
	/* Not sure what to do about this yet
	//NOT IN LIBRARY
	property_list.push("longevity");
	db.createCollection("longevity", {});
	
	//NOT IN LIBRARY
	property_list.push("time to first harvest");
	db.createCollection("first_harvest",{});
	*/
	
	
	property_list.push(["harvest season", "harvest_season"]);
	v = [{value: "spring"}, {value: "summer"}, {value: "autumn"}, {value: "winter"}];
	db.harvest_season.save(v);
	
	//Must create library collection last so that population works properly//
	db.createCollection(library_list[1], {});
	
	var curLib = db.getCollection(library_list[1]);
	for(p in property_list){
		curEntry = db.getCollection(property_list[p][1]);
		doc = {property : property_list[p][0], collection : property_list[p][1]};
		curLib.insert(doc);
		/*
		var valueCursor = curEntry.find({},{_id:1} );
		valueCursor.forEach(
			function(doc){
				curLib.update(
					{property: property_list[p]},
					{'$push': {values : new DBRef(curEntry, doc._id)}}
				)
			}
		)*/
	}
	
	property_list = [];



//needs

	//sun
	property_list.push(["sun", "sun"]);
	v = [{value: "full sun"}, {value: "partial sun"}, {value: "indirect sun"}, {value: "morning sun"}, {value: "afternoon sun"}, ];
	db.sun.save(v);
	//water
	property_list.push(["water","water"]);
	v = [{value: "low"}, {value: "moderate"}, {value: "high"}, {value: "aquatic"}];
	db.water.save(v);
	
	
	/* This will actually be in the gen lib... we just need to point, no?
	//nutrients
	property_list.push("nutrients");
	db.createCollection("nutrients", {});
	*/
	
	//inoculant
	property_list.push(["inoculants", "innoculants"]);
	db.createCollection("inoculants", {});
	
	/* Not sure what to do with this yet
	property_list.push("chill hours");
	db.createCollection("chill_hours", {});
	*/

	//Must create library collection last so that population works properly//
	db.createCollection(library_list[2], {});
	
	var curLib = db.getCollection(library_list[2]);
	for(p in property_list){
		curEntry = db.getCollection(property_list[p][1]);
		doc = {property : property_list[p][0], collection : property_list[p][1]};
		curLib.insert(doc);
		/*
		var valueCursor = curEntry.find({},{_id:1} );
		valueCursor.forEach(
			function(doc){
				curLib.update(
					{property: property_list[p]},
					{'$push': {values : new DBRef(curEntry, doc._id)}}
				)
			}
		)*/
	}
	
	property_list = [];



//products
	//food
	property_list.push(["food", "food"]);
	v = [{value: "greens"}, {value: "grains"}, {value: "vegetables"}, {value: "nuts"}, {value: "fruit"}];
	db.food.save(v);
	//raw materials
	property_list.push(["raw material", "raw_materials"]);
	v = [{value: "biomass"}, {value: "timber"}, {value: "rubber"}, {value: "fiber"}, {value: "oil"}, {value: "fuel"}];
	db.raw_materials.save(v);
	//medicinals
	property_list.push(["medicinal", "medicinals"]);
	v = [{value: "antispasmodic"}, {value: "stimulant"}, {value: "carminative"}, {value: "anti-inflammatory"}, {value: "antiseptic"}];
	db.medicinals.save(v);
	//chemical resources (non-medicinal)
	property_list.push(["biochemical material", "biochemicals"]);
	v = [{value: "detergents"}, {value: "wetting agent"}, {value: "emulsifier"}, {value: "foaming agent"}];
	db.biochemicals.save(v);
	//cultural amenity
	property_list.push(["cultural and amenity", "cultural_amenity"]);
	v = [{value: "aesthetic"}, {value: "recreational"}, {value: "artistic inspiration"}, {value: "cultural heritage and identity"}, {value: "spiritual and religious inspiration"}];
	db.cultural_amenity.save(v);
	
	/* problem, do this in gen, and I think we need to just ref?
	//nutrients
	property_list.push("nutrients");
	db.createCollection("nutrients", {});
	*/
	
	//Must create library collection last so that population works properly//
	db.createCollection(library_list[3], {});
	
	var curLib = db.getCollection(library_list[3]);
	for(p in property_list){
		curEntry = db.getCollection(property_list[p][1]);
		doc = {property : property_list[p][0], collection : property_list[p][1]};
		curLib.insert(doc);
		/*
		var valueCursor = curEntry.find({},{_id:1} );
		valueCursor.forEach(
			function(doc){
				curLib.update(
					{property: property_list[p]},
					{'$push': {values : new DBRef(curEntry, doc._id)}}
				)
			}
		)*/
	}
	
	property_list = [];



//behaviors

	//erosion control
	property_list.push(["erosion control", "erosion_control"]);
	v = [{value: "great"}, {value: "medium"}, {value: "little"}, {value: "none"}];
	db.erosion_control.save(v);
	//toxicity treatment
	property_list.push(["toxin removal", "toxin_removal"]);
	v = [{value: "air"}, {value: "soil"}];
	db.toxin_removal.save(v);
	
	/* This is in the general lib, and we should just be refing.
	//pest regulation
	property_list.push("pest regulation");
	db.createCollection("pest regulation", {});
	
	//pollinator attractor
	property_list.push("pollinator attractor");
	db.createCollection("pollinator attractor", {});
	//animal regulation
	property_list.push("animal regulation");
	db.createCollection("animal regulation", {});
	//animal attractor
	property_list.push("animal attractor");
	db.createCollection("animal attractor", {});
	*/
	
	//leaf shedding
	property_list.push(["leaf shedding", "leaf_shedding"]);
	v = [{value: "deciduous"}, {value: "semi-deciduous"}, {value: "evergreen"}];
	db.leaf_shedding.save(v);
	
	//Must create library collection last so that population works properly//
	db.createCollection(library_list[4], {});


var curLib = db.getCollection(library_list[4]);
	for(p in property_list){
		curEntry = db.getCollection(property_list[p][1]);
		doc = {property : property_list[p][0], collection : property_list[p][1]};
		curLib.insert(doc);
		/*
		var valueCursor = curEntry.find({},{_id:1} );
		valueCursor.forEach(
			function(doc){
				curLib.update(
					{property: property_list[p]},
					{'$push': {values : new DBRef(curEntry, doc._id)}}
				)
			}
		)*/
	}
	
	property_list = [];

/*

//Now set up the libraries

	var collectionArray = db.getCollectionNames();
	
	var i, p, l = 0;
	
	var curLib = db.getCollection(library_list[l]);
	
	while(i < collectionArray.length - 1 ){ 
	//filter through every collection. The last one is behavior library.
	
		if(collectionArray[i] == library_list[l]){ 
		//when the collection is a library, we're ready to fill the next library.
			i,l += 1;
			curLib = db.getCollection(library_list[l]);
		}
		
		prop = {property : property_list[p]};
		curLib.insert(prop);
		var valueCursor = db.collectionArray[i].find({},{_id:1} );
		valueCursor.forEach(
			function(doc){
				curLib.update(
					{property: property_list[p]},
					{'$push': {values : new DBRef(collectionArray[i], doc._id)}}
				)
			}
		)
		i,p += 1; 
		//move to the next collection and its properties
	}
	*/