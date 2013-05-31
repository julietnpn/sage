<?php 

include('connect-pg-db.php');

//mysql_query format of all entries in the products table



function get_table_entries($tablename)
{
	return mysql_query("SELECT * FROM ".$tablename." WHERE active=TRUE");
}

function get_table_entries_order($tablename, $order)
{
	return mysql_query("SELECT * FROM ".$tablename." WHERE active=TRUE ORDER BY ".$order);
}


function get_entries_with_pl_id($tablename, $pl_id){
	return mysql_query("SELECT * FROM ".$tablename." WHERE active=TRUE AND pl_id=".strval($pl_id));
}	


function type_of_products()
{
	$types = array('Food', 'Medicine', 'BuildingMaterials', 'HomeMaterials');
	$return = array();
	foreach( $types as $t){
		$result = get_table_entries($t);
		$num = mysql_num_rows($result);
		if ($num > 0){
			$prodstruct['name'] = $t;
			$prodstruct['num_entries'] = $num;
			$prodstruct['data'] = $result;
			array_push($return, $prodstruct);
			}
	}
	return $return;
}

function product_info($data, $entry){
	$prod_id = mysql_result($data, $entry, 1);
	$plant_part = mysql_result($data, $entry, 'plantpart');
	
	
	//get plant info:
	$result = mysql_query("SELECT pl_id FROM Product WHERE active=TRUE AND id = ".$prod_id);
	$plant_id = mysql_result($result, 0, 0);
	$result = mysql_query("SELECT * FROM Plant WHERE active = TRUE and id = ".$plant_id);
	$genus = mysql_result($result, 0,1);
	$species = mysql_result($result, 0,2);
	$common_names = mysql_result($result, 0,3);
	
	$array = array();
	$array["genus"]= $genus;
	$array["species"] = $species;
	$array["names"] = $common_names;
	$array["plant_part"] = $plant_part;
	
	return $array;
}
	
	
function add_New_Plant($varString){
	$varCategories = explode("|", $varString); //plantinfo | newplantdata    
	$plant_id = add_Plant_Info($varCategories[0]); //returns the mongo_db ref.
	//update_New_Image_plid($plant_id); <!-- will do later.
	add_New_Plant_Data($plant_id, $varCategories[1]);
}

function add_New_Plant_Data($plant_id, $categoriesList){
	//$plant_id is the plant document's mongo_db ref (in the plants collection).
	global $db_plant_coll;
	$lists = array("intrinsics_list", "needs_list", "products_list", "behaviors_list");
	$categories = explode("$$", $categoriesList);
	
	for($i = 0; $i < sizeof($categories); $i++)
	{
		echo('testing testing '.$categories[$i]);
	
		if($categories[$i] != ""){
			$propertyList = explode("},", $categories[$i]);
			//echo("size of list: ".sizeof($PropertyList));
			
			//JULIET START HERE you're looking at how to insert into the plant lists. they don't exist yet. I think you should just create an array, and then insert them into the list!
			if(sizeof($propertyList) == 0)
				add_Property($plant_id, $categories[$i], $lists[$i]);
			for($j = 0; $j<sizeof($propertyList); $j++){
				if($propertyList[$j] != ""){
					add_Property($plant_id, $propertyList[$j], $lists[$i]);
				}	
			}
		}
	}

}

function delete_Plant_Data($categoriesList){
	$table = array("IntrinsicChar", "Need", "Product", "Behavior", "Image"); //add Images
	$varArray = explode("$$", $categoriesList);
	
	for($i = 0; $i < sizeof($varArray); $i++){
		if($varArray[$i] != ""){
			$list = explode(",", $varArray[$i]);
			for($j = 0; $j<sizeof($list); $j++){
				delete_Property($list[$j], $table[$i]);
			}
		}
	}
}

function update_Plant($varString){
	$varOperation = explode("|", $varString); //plantid | plantinfo |newplantdata | delete plant data
	
	$plant_id = $varOperation[0];
	update_New_image_plid($plant_id);
	$varUpdatedPlantInfo = $varOperation[1];
	$varInsert = $varOperation[2];
	$varDelete = $varOperation[3];

	if($varUpdatedPlantInfo != "")
		update_Plant_Info($varUpdatedPlantInfo, $plant_id);
	
	add_New_Plant_Data($plant_id, $varInsert);
	
	delete_Plant_Data($varDelete);

}

function delete_Plant($varString){
	delete_Property($varString, 'Plant');
	delete_Properties_of_plid($varString, 'Image');
	delete_Properties_of_plid($varString, 'IntrinsicChar');
	delete_Properties_of_plid($varString, 'Need');
	delete_Properties_of_plid($varString, 'Product');
	delete_Properties_of_plid($varString, 'Behavior');
}

function add_Plant_Info($varString){
	global $db_plant_coll;
	
	$propertyList = explode("},", $varString);
	
	$query = array();
	
	for($i = 0; $i < sizeof($propertyList); $i++){
		$contents = explode("{", $propertyList[$i]);
		array_push($query, array($contents[0] => $contents[1]));
	}
	$db_plant_coll->insert($query);
	
	return $query['_id']; //the array passed to insert is amended with an _id field.
	
	/*$query = "INSERT INTO Plant SET ";
	for($i = 0; $i < sizeof($propertyList); $i++){
		$contents = explode("{", $propertyList[$i]);
		$query=$query.$contents[0]."='".mysql_real_escape_string($contents[1])."'";
		if($i < sizeof($propertyList)-1)
			$query= $query.", ";
	}
	//echo('DEBUG: add_plant_info'.$query);
	mysql_query($query);
	
	return mysql_insert_id();
	*/
	
}

function update_Plant_Info($varString, $pl_id){
	$propertyList = explode("},", $varString);
	$query = "Update Plant SET ";
	for($i = 0; $i < sizeof($propertyList); $i++){
		$contents = explode("{", $propertyList[$i]);
		$query= $query.$contents[0]."='".strval(mysql_real_escape_string($contents[1]))."'";
		
		if($i < sizeof($propertyList)-1)
			$query= $query.", ";
	}
	$query= $query.' WHERE id='.$pl_id;

	//echo('DEBUG: update_Plant_Info '.$query);
	mysql_query($query);
}


function add_Property($plant_id, $varString, $collection_name){
	global $db, $db_plant_coll;
	//plant_id is the mongo_db ref for the plant doc in the plants collection
	//varString contins the property and value pair
	//collection_name represents which library it is a part of.
	
	echo('DEBUG: add_Property plant_id is'.$plant_id);
	
	$contents = explode("{", $varString);
	//contents[0] is the property
	//contents[1] is the value
	
	//get collection name by looking up "property" in the corresponding library
	$collection = $db->selectCollection($collection_name);
	$query_p = $collection->findOne(array('property'=>$contents[0]));
	$prop_coll = $db->selectCollection($query_p['collection']);
	
	//get doc ref to that property's value.
	$query_v = $prop_coll->findOne(array('value'=>$contents[1]));
	$value_ref = $prop_coll->createDBRef($query_v);
	
	//save property's doc ref to plant's list
	$db_plant_coll->update(array('_id'=>$plant_id), array('$push' => array($collection_name=>$value_ref)));
	
	//save plant ref to property's doc plant list.
	$query_plant = $db_plant_coll->findOne(array('_id'=>$plant_id));
	$plant_ref = $db_plant_coll.createDBRef($query_plant);
	$prop_coll.update(array('_id'=>$query['_id']), array('$push' => array('plant_list'=>$plant_ref)));

/*
	if ($table == "Product")
		add_ProductProperty($plant_id, $varString, $table);
		
		
	$contents = explode("{", $varString);

	$query_select = "SELECT * FROM ".$table." WHERE pl_id=".$plant_id;
	
	$query_contents = "`".mysql_real_escape_string($contents[0])."`='".mysql_real_escape_string($contents[1])."'";

	$result = mysql_query($query_select);

	if (mysql_num_rows($result) == 0){
		$query_insert = "INSERT INTO ".$table." SET pl_id=".strval($plant_id).", ".$query_contents;
		echo('DEBUG: add_property, '.$query_insert);
		mysql_query($query_insert);
		
	}else{
		$query_update = "UPDATE ".$table." SET ".$query_contents." WHERE pl_id=".strval($plant_id);
		echo('DEBUG: add_property, '.$query_update);
		mysql_query($query_update);
	}
	*/
	
}
	


function add_ProductProperty($plant_id, $varString, $table){
	
	$contents = explode("{", $varString);
	$attributes = explode("*", $contents[1]);
	
	//This is really only valid for Products, but for all the others, what should happen is that there is one entry, and that entry needs to be looked up, and each of these column-properties should have their values
	
	$query = "INSERT INTO ".$table." SET pl_id=".strval($plant_id).", property='".$contents[0]."', ";
	
	$query= $query."plant part='".mysql_real_escape_string($attributes[0])."', yield='".mysql_real_escape_string($attributes[1])."', ";//plant part, yield
		
	$query= $query."val='".mysql_real_escape_string($attributes[2])."'";///value
	
	
	
	echo('DEBUG: add_productproperty '.$query);
	mysql_query($query);
}

function add_Image($fileName){
	$query = "INSERT INTO Image SET path='".mysql_real_escape_string($fileName)."'";
	//echo("Debug: query is ".$query);
	return(mysql_query($query));
	}
	
function delete_Property($varString, $table){
	$query = 'UPDATE '.$table.' SET active=FALSE WHERE id='.$varString;
	//echo('DEBUG: '.$query);
	mysql_query($query);
}

function delete_Properties_of_plid($varString, $table){
	$query = 'UPDATE '.$table.' SET active=FALSE WHERE pl_id='.$varString;
	//echo('DEBUG: '.$query);
	mysql_query($query);
}

function update_New_Image_plid($plant_id){
	sleep(2);
	$rs = mysql_query('SELECT id FROM Image WHERE active=TRUE AND pl_id IS NULL');
	//for size of rs, get the id, then update pl_id to $plant_id
	for($i=0; $i<mysql_num_rows($rs);$i++){
		$id = mysql_result($rs, $i, 0);
		$query = 'UPDATE Image SET pl_id='.$plant_id.' WHERE id='.$id;
		echo("DEBUG: ".$query);
		mysql_query($query);
	}
}

function load_Plant_Data($pl_id){
	$rs_Plant = mysql_query("SELECT * FROM Plant WHERE active=TRUE AND id=".strval($pl_id));
	//echo("DEBUG: why is query coming back as bool? ".$pl_id);
	$genus = mysql_result($rs_Plant, 0, 1);
	$species = mysql_result($rs_Plant, 0, 2);
	$commonnames = mysql_result($rs_Plant, 0, 3);
	
	$plantData = array($genus, $species, $commonnames);
	
	
	$intrinsic = get_entries_with_pl_id('IntrinsicChar', $pl_id);
	$needs = get_entries_with_pl_id('Need', $pl_id);
    $products = get_entries_with_pl_id('Product', $pl_id);
    $behaviors = get_entries_with_pl_id('Behavior', $pl_id);
    $images = get_entries_with_pl_id('Image', $pl_id);
    
    $intrinsicsData = array();
    if ($intrinsic != 0){
		for($j=0; $j <  mysql_num_rows($intrinsic); $j++){
			$entity = array();
			$tbl_id = mysql_result($intrinsic, $j, 0);
			$property =  mysql_result($intrinsic, $j, 2);
			array_push($entity,$tbl_id, $property);
			if($property == "shape"){
				$shape = mysql_result($intrinsic, $j, 5);
				array_push($entity, $shape);
			}else {
				$val = mysql_result($intrinsic, $j, 3);
				array_push($entity, $val, "centimeters");
			}
			array_push($intrinsicsData, $entity);
		}
    }
    
    array_push($plantData, $intrinsicsData);
    
    $needsData = array();
    for($j=0; $j <  mysql_num_rows($needs); $j++){
    	$entity = array();
    	$tbl_id = mysql_result($needs, $j, 0);
    	$property =  mysql_result($needs, $j, 2);
    	$val = mysql_result($needs, $j, 3);
    	array_push($entity, $tbl_id, $property, $val);
		array_push($needsData, $entity);
    }
    
    array_push($plantData, $needsData);
    
    $productsData = array();
    for($j=0; $j <  mysql_num_rows($products); $j++){
    	$entity = array();
    	$tbl_id = mysql_result($products, $j, 0);
    	$property =  mysql_result($products, $j, 2);
    	$plantpart = mysql_result($products, $j, 3);
    	$yield = mysql_result($products, $j, 4);
    	$food = mysql_result($products, $j, 5);
    	$val = mysql_result($products, $j, 6);
    	array_push($entity, $tbl_id, $property, $plantpart,$yield);
    	if($property == "food"){
			array_push($entity, $food);
    	}else{
    		array_push($entity, $val);
    	}
    	
		array_push($productsData, $entity);
    }
    
    array_push($plantData, $productsData);
    
    
    $behaviorsData = array();
    for($j=0; $j <  mysql_num_rows($behaviors); $j++){
    	$entity = array();
    	$tbl_id = mysql_result($behaviors, $j, 0);
    	$property =  mysql_result($behaviors, $j, 2);
    	$val = mysql_result($behaviors, $j, 3);
    	array_push($entity, $tbl_id, $property, $val);
		array_push($behaviorsData, $entity);
    }
    
    array_push($plantData, $behaviorsData);
    
    $imagePaths = array();
    
	for($j=0; $j <  mysql_num_rows($images); $j++){
		$path= array();
		$tbl_id = mysql_result($images, $j, 0);
		$filepath = mysql_result($images, $j, 2);
		array_push($path, $tbl_id, $filepath);
		array_push($imagePaths, $path);
	}
    
    array_push($plantData, $imagePaths);
    
	return $plantData;
}

function printPlantData_SingleCategory($categoryData, $categoryName){
	for ($i=0; $i<sizeof($categoryData); $i++){
		$idPref = $categoryName . $categoryData[$i][0];
		echo("<div id='".$idPref."' class='numval'><a onclick='delete_Element(\"".$idPref."\")' href='#'> X </a>");
		echo("<div id='".$idPref."proplist' class='numval' style='display:inline'>Property: ".$categoryData[$i][1]."</div>");
		echo("<div id='".$idPref."value' style='display:inline; margin-left:10px' class='numval'>Value: ");
		
		for($j=2; $j < sizeof($categoryData[$i]); $j++){
			echo("<div id='".$idPref."valuechild".$j."' style='display:inline'>".$categoryData[$i][$j]." </div>");
		}
		echo("</div></div>");
	}
}

function printImages($filePaths){
	/*for ($i=0; $i<sizeof($filePaths); $i++){
		if($i%4 == 0){
			$id = $i/4;
			echo("<div id='savedimages".$id."' class='imageRow'>");
		}
		$imageInfo = $filePaths[$i];
		echo("<div id='images".$imageInfo[0]."' class='single'><img src='uploaded_files/".$imageInfo[1]."' width='200'/><br/><a onclick='delete_Element(\"images".$imageInfo[0]."\")' href='#'> X </a></div>");
		if($i%4 == 3 || $i == sizeof($filePaths) -1)
			echo("</div>");
	}*/
	
	
	echo("<div id='savedimages' class='imageRow'>");
	for ($i=0; $i<sizeof($filePaths); $i++){
		$imageInfo = $filePaths[$i];
		$imageSize = getimagesize("uploaded_files/".$imageInfo[1]);
		$width = 200;
		$height = $width * $imageSize[1] / $imageSize[0];
		$divWidth = $width+10; //for padding;
		$divHeight = $height+10+13;  //padding + link height
		//echo('<div id="images'.$imageInfo[0].'" style="display:block; float:left; padding:5px; background-image:url(\'uploaded_files/'.$imageInfo[1].'\'); width:'.$width.'px; height:'.$height.'px;"><a onclick="delete_Element(\'images'.$imageInfo[0].'\')" href="#"> X </a></div>');
		//echo('<p style="position: absolute; top: 1em; right: 2em; width: 120px; padding: 4px; background-color: #fff;"><a onclick="delete_Element(\'images'.$imageInfo[0].'\')" href="#"> X </a></p></div>');
		echo('<div id="images'.$imageInfo[0].'" style="display:block; float:left; padding:5px; width:'.$divWidth.'px; height:'.$divHeight.'px;"><img src="uploaded_files/'.$imageInfo[1].'" width="'.$width.'"/><a onclick="delete_Element(\'images'.$imageInfo[0].'\')" href="#"> X </a></div>');
	}
	echo("</div>");
	
}

function printDBListing($plantRS){
	//get genus, species, common name of the plant
		$pl_id = $plantRS[0];
		$genus = $plantRS[1];
		$species = $plantRS[2];
		$commonnames = $plantRS[3];
		
		echo('<div class="accordion_child">');
		//sleep(5);
		$images = get_entries_with_pl_id('Image', $pl_id);
			echo('<div class="image">');
			$featureImgPath = mysql_result($images, 0, 2);
				echo('<img src="uploaded_files/'.$featureImgPath.'" alt="'.$genus.' '.$species.'" width="200"/>');
			echo('</div>');
		echo('<div class="leftcolumn">');
		
		//echo('DEBUG: plant id = '.$pl_id);
		//to do have this go to a new page when they click on it...
		echo('<p><a href="viewPlantDetails.php?pl_id='.$pl_id.'">Scientfic Name: '.$genus.' '.$species.'</a></p>');
		echo('<p>Common Name: '.$commonnames.'</p>');      
		echo('<div>Intrinsic Characteristics:<div class="indent">');
		
		$intrinsic = get_entries_with_pl_id('IntrinsicChar', $pl_id);
		if(mysql_num_rows($intrinsic) > 0){
			for($i=0; $i< mysql_num_fields($intrinsic); $i++){
				$property =  mysql_fetch_field($intrinsic, $i);
				$value = mysql_result($intrinsic, 0, $i);
				if($value == null)
					continue;
				
				if($property->name == 'id' || $property->name == 'pl_id')
					continue;
				else if($property->name == 'active')
					break;
					
				echo('<br>'.$property->name.': '.strval($value));
				if($property->name == 'height maximum' || $property->name== 'height minimum' || $property->name == 'spread maximum' || $property->name == 'spread minimum'){
					echo(' cm');
				}
			}
		}
		echo("</div></div></div>");
		
		
		$needs = get_entries_with_pl_id('Need', $pl_id);
		$products = get_entries_with_pl_id('Product', $pl_id);
		$behaviors = get_entries_with_pl_id('Behavior', $pl_id);
		
		echo('<div class="rightcolumn"><div class="propheading">Needs:<div class="indent">');
		if(mysql_num_rows($needs) > 0){
			for($i=0; $i< mysql_num_fields($needs); $i++){
				$property =  mysql_fetch_field($needs, $i);
				$value = mysql_result($needs, 0, $i);
				if($value == null)
					continue;
				
				if($property->name == 'id' || $property->name == 'pl_id')
					continue;
				else if($property->name == 'active')
					break;
					
				echo('<br>'.$property->name.': '.strval($value));
				
			}
		}
		
		
		/*for($j=0; $j <  mysql_num_rows($needs); $j++){
			$property =  mysql_result($needs, $j, 2);
			$val = mysql_result($needs, $j, 3);
			echo($property.': '.$val.'<br>');
		}*/
		echo("</div></div>");
		
		echo('<div class="propheading">Products & Behaviors:<div class="indent">');
		for($j=0; $j <  mysql_num_rows($products); $j++){
			$property =  mysql_result($products, $j, 2);
			$plantpart = mysql_result($products, $j, 3);
			$yield = mysql_result($products, $j, 4);
			$food = mysql_result($products, $j, 5);
			$val = mysql_result($products, $j, 6);
			echo($property.': '.$yield.' ');
			if($property == "food"){
				echo($food.', plant part: '.$plantpart.'<br>');
			}else{
				echo($val.', plant part: '.$plantpart.'<br>');
			}
		}
		for($j=0; $j <  mysql_num_rows($behaviors); $j++){
			$property =  mysql_result($behaviors, $j, 2);
			$val = mysql_result($behaviors, $j, 3);
			echo($property.': '.$val.'<br>');
		}
		
		echo("</div></div>");
		echo("</div></div>");
}



function loadFunctionalAnalysis($collection){
	//propertyList['name'] = intrinsics;
	//propertyList['layer'] = {canopy, understory, ...}
	
	global $db;
	$libCursor = $collection->find();
	//$cursor looks like:
	//[{ "_id" : ObjectId( "511ae981ff2ca2d43bc464ef" ),
  	//	"property" : "layer",
  	//	"collection" : "layer" },
  	//
  	//{ "_id" : ObjectId( "511ae981ff2ca2d43bc464f0" ),
 	//  "property" : "canopy density",
  	//  "collection" : "canopy_density" }, 
  	//
  	// ... ]

	$propertyList = array();
	$propertyList['name'] = $collection->getName();
	
	
	foreach ($libCursor as $libDoc){
		//Now we go through each pointer in the library, find the actual collection and load its values.
		$property = $libDoc['property'];
		$prop_collection_name = $libDoc['collection'];
		$propCollection = $db->selectCollection($prop_collection_name);
		
		//loading values
		$propCursor = $propCollection->find();
		$val = array();
		foreach ($propCursor as $propDoc){
			array_push($val, [$propDoc['value'], $propDoc['description']]);
		}
			
		
		$propertyList[$property] = $val;
		
	
	}
	
	return $propertyList;


///////////// Old Stuff
/*
	$result = mysql_query("SHOW COLUMNS FROM ".$table);
	if (mysql_num_rows($result) > 0) {
	
			$propertyList = array();
			$propertyList['name'] = $table;
			while ($row = mysql_fetch_assoc($result)) { //problem, this assoc array wants to be accessed by the row names.
				//$row is an array containing filed, type, null, key, default, extra in that order
				
				$field = $row['Field'];
				$type = $row['Type'];
			
				
				if($field != "val"){
					$enum = Null;
					
					if(strrpos($type, "enum")!== false){
						
						//remove enum stuff
						preg_match('/enum\((.*)\)$/', $type, $matches);
						$val = explode(',', $matches[1]);
						foreach($val as $v)
							$enum[] = trim($v, "'");
						$type = $enum;
					}
				
					if($field == 'id' || $field == 'pl_id' || $field == 'property') // all of the fields from active on wards are just important to the DB
						continue;
					if($field == 'active' || $field == 'plant part') // all of the fields from active on wards are just important to the DB
						break;
					
					
					$propertyList[$field] = $type;
				}
				else{
					foreach ($enum as $e)
						$propertyList[$e] = $type;
				}
		}	
			
		return $propertyList;
	} 
	else
		return false;
		*/
}

function loadFATools(){
	$result = mysql_query("SHOW COLUMNS FROM Product");
	$propertyList = array();
	if (mysql_num_rows($result) > 0) {
		while ($row = mysql_fetch_assoc($result)) {
		
			$field = $row['Field'];
			$type = $row['Type'];
			
			if($field == 'id' || $field == 'pl_id' || $field == 'property' || $field == 'val')
				continue;
			
			if($field == 'active') // all of the fields from active on wards are just important to the DB
				break;
			
			$enum = Null;
					
			if(strrpos($type, "enum")!== false){
				//remove enum stuff
				preg_match('/enum\((.*)\)$/', $type, $matches);
				$val = explode(',', $matches[1]);
				foreach($val as $v)
					$enum[] = trim($v, "'");
				$type = $enum;
			}
			
			$propertyList[$field] = $type;
			
		}
		return $propertyList;
	}else{
		return false;
		}

}