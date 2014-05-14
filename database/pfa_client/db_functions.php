<?php 

include('connect-pg-db.php');


$IntrinsicChar = setup_FA($db_intrinsics_lib);
	$Need = setup_FA($db_needs_lib);
	$Product = setup_FA($db_products_lib);
	$Behavior = setup_FA($db_behaviors_lib);

//in transition from mysql_query format to mongodb query

//ported, not tested
//function get_table_entries($tablename)
function get_collection_entries($collectionname)
{
	global $db;
	$c = $db->$collectionname;
	return $c->find();
}


//ported, not tested
//function get_table_entries_order($tablename, $order)
//TODO: incorporating a sort order, ascending/decending. Right now does decending order
function get_collection_entries_order($collectionname, $order)
{
	$cursor = get_collection_entries($collectionname);
	return $cursor->sort(array($order => -1));
}


//TODO: Can this be removed?
function get_entries_with_pl_id($tablename, $pl_id){
	return mysql_query("SELECT * FROM ".$tablename." WHERE active=TRUE AND pl_id=".strval($pl_id));
}	

//ported, not tested
function type_of_products()
{
	$types = get_collection_entries('products_lib');
	$return = array();
	foreach( $types as $t){
		$vals = $t['values'];
		$num = count($vals);
		if ($num > 0){
			$prodstruct['name'] = $t['name'];
			$prodstruct['num_entries'] = $num;
			$prodstruct['data'] = $vals;
			array_push($return, $prodstruct);
			}
	}
	return $return;
}

//TO DO: Identify the purpose of this function and then port.
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
	echo("add New Plant");
	$varCategories = explode("|", $varString); //plantinfo | newplantdata    
	$plant_id = add_Plant_Info($varCategories[0]); //returns the mongo_db ref.
	//update_New_Image_plid($plant_id); <!-- will do later.
	add_New_Plant_Data($plant_id, $varCategories[1]);
}

function add_New_Plant_Data($plant_id, $categoriesList){
	//$plant_id is the plant document's mongo_db ref (in the plants collection).
	global $db_plant_coll;
	$libs = array("intrinsics_lib", "needs_lib", "products_lib", "behaviors_lib");
	$lists = array("intrinsics_list", "needs_list", "products_list", "behaviors_list");
	$categories = explode("$$", $categoriesList);
	
	for($i = 0; $i < sizeof($categories); $i++)
	{
		echo('testing testing '.$categories[$i]);
	
		if($categories[$i] != ""){
			$propertyList = explode("},", $categories[$i]);
			//echo("size of list: ".sizeof($PropertyList));
			
			if(sizeof($propertyList) == 0)
				add_Property($plant_id, $categories[$i], $libs[$i], $lists[$i]);
			for($j = 0; $j<sizeof($propertyList); $j++){
				if($propertyList[$j] != ""){
					add_Property($plant_id, $propertyList[$j], $libs[$i], $lists[$i]);
				}	
			}
		}
	}

}

function delete_Plant_Data($categoriesList, $pl_id){
	$lists = array("intrinsics_list", "needs_list", "products_list", "behavior_list"); //add Images
	$varArray = explode("$$", $categoriesList);
	
	for($i = 0; $i < sizeof($varArray); $i++){
		if($varArray[$i] != ""){
			$data = explode(",", $varArray[$i]);
			for($j = 0; $j<sizeof($data); $j++){
				error_log("deleting in list ".$lists[$i]);
				delete_Property($data[$j], $lists[$i], $pl_id);
			}
		}
	}
}

function update_Plant($varString){
	$varOperation = explode("|", $varString); //plantid | plantinfo |newplantdata | delete plant data
	$plant_id = $varOperation[0];
	//update_New_image_plid($plant_id);  TODO
	$varUpdatedPlantInfo = $varOperation[1];
	$varInsert = $varOperation[2];
	$varDelete = $varOperation[3];

	if($varUpdatedPlantInfo != "")
		update_Plant_Info($varUpdatedPlantInfo, $plant_id);
	
	add_New_Plant_Data($plant_id, $varInsert);
	
	delete_Plant_Data($varDelete, $plant_id);
	
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
	echo("add plant info");
	global $db_plant_coll;
	
	$propertyList = explode("},", $varString);
	
	$query = array();
	
	for($i = 0; $i < sizeof($propertyList); $i++){
		$contents = explode("{", $propertyList[$i]);
		print_r($contents); echo "<br>";
		if(! empty($contents[0])){
			$query[$contents[0]] = $contents[1];
			print_r($query); echo "<br>";
		}
		
	}
	$db_plant_coll->insert($query);
	
	return $query['_id']; //the array passed to insert is amended with an _id field.
	
}

function update_Plant_Info($varString, $pl_id){
	//only for plant info like genus, species, common name...
	global $db_plant_coll;
	$propertyList = explode("},", $varString);
	for($i = 0; $i < sizeof($propertyList); $i++){
		$contents = explode("{", $propertyList[$i]);
		$db_plant_coll->update(array('_id'=>$pl_id), array('$set' => array($contents[0]=>$contents[1])));
	}
}


function add_Property($plant_id, $varString, $collection_name, $list_name){
	global $db, $db_plant_coll;
	//plant_id is the mongo_db ref for the plant doc in the plants collection
	//varString contins the property and value pair
	//collection_name represents which library it is a part of.
	
	$contents = explode("{", $varString);
	//contents[0] is the property
	//contents[1] is the value

	//get collection name by looking up "property" in the corresponding library
	$collection = $db->$collection_name; //the library
	$query_p = $collection->findOne(array('name'=>$contents[0])); // the entry in the library
	$prop_coll = $db->selectCollection($query_p['collection']); // the entrie's home collection
	
	//get doc ref to that property's value.
	$query_v = $prop_coll->findOne(array('value'=>$contents[1]));
	$value_ref = $prop_coll->createDBRef($query_v);
	$value_ref['active'] = true;
	
	//save property's doc ref to plant's list
	$db_plant_coll->update(array('_id'=>$plant_id), array('$push' => array($list_name=>$value_ref)));
	
	//save plant ref to property's doc plant list.
	$query_plant = $db_plant_coll->findOne(array('_id'=>$plant_id));
	$plant_ref = $db_plant_coll->createDBRef($query_plant);
	$prop_coll->update(array('_id'=>$query_v['_id']), array('$push' => array('plant_list'=>$plant_ref)));
	
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
	
function delete_Property($varString, $list, $pl_id){
	global $db_plant_coll;
	$subcoll= $db_plant_coll->findOne(array('_id'=>new MongoId($pl_id), 'needs_list.$id' => new MongoId($varString)));
	error_log("in delete_Property teh sub collection we'd like to delete is... ".print_R($subcoll,true));
	$db_plant_coll->update(array('_id'=>new MongoId($pl_id), $list.'.$id'=> new MongoId($varString)), array('$set' => array($list.'.$.active'=>false)));
	//$db_plant_coll->update(array('_id'=>$pl_id), array('$pull' => array($list=> array('$id'=>$varString))));
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
	global $db, $db_plant_coll, $db_intrinsics_lib, $db_needs_lib, $db_products_lib, $db_behaviors_lib;
	$query = $db_plant_coll->findOne(array('_id'=> new MongoId($pl_id)));
	
	$genus = $query['genus'];
	$species = $query['species'];
	$commonnames = $query['common_names'];
	
	$plantData = array($genus, $species, $commonnames);	
	
	$intrinsic = $query['intrinsics_list'];
	$needs = $query['needs_list'];
	$products = $query['products_list'];
	$behaviors = $query['behaviors_list'];
	//need images 
	
	$array = array($intrinsic, $needs, $products, $behaviors);
	$libs = array($db_intrinsics_lib, $db_needs_lib, $db_products_lib, $db_behaviors_lib);
    
	for($j=0; $j< sizeof($array); $j++){
		
		$dataArray = array();
		
		if(sizeof($array[$j]) > 0){
			for($i=0; $i< sizeof($array[$j]); $i++){
				$property_ref =  $array[$j][$i]['$ref'];
				$value_ref = $array[$j][$i]['$id'];
			
				$property_query = $libs[$j]->findOne(array('collection'=>$property_ref), array('name'));
				$property = $property_query['name'];
			
				$value_coll = $db->$property_ref;
				$value_query = $value_coll->findOne(array('_id'=>$value_ref));
				$value = $value_query['value'];
			
				array_push($dataArray, array($value_ref, $property, $value));
			}
		}
		array_push($plantData, $dataArray);
	}
    
	return $plantData;
}

function printPlantData_SingleCategory($categoryData, $categoryName){
	//var_dump($categoryData);
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
	global $db, $db_intrinsics_lib, $db_needs_lib, $db_products_lib, $db_behaviors_lib;
	
		$pl_id = $plantRS['_id'];
		$genus = $plantRS['genus'];
		$species = $plantRS['species'];
		$commonnames = $plantRS['common_names'];
		
		echo('<div class="accordion_child">');
		//$images = get_entries_with_pl_id('Image', $pl_id);
			echo('<div class="image">');
			//$featureImgPath = mysql_result($images, 0, 2);
				//echo('<img src="uploaded_files/'.$featureImgPath.'" alt="'.$genus.' '.$species.'" width="200"/>');
			echo('</div>');
		echo('<div class="leftcolumn">');
		

		//to do have this go to a new page when they click on it...
		echo('<p><a href="viewPlantDetails.php?pl_id='.$pl_id.'">Scientfic Name: '.$genus.' '.$species.'</a></p>');
		echo('<p>Common Name: '.$commonnames.'</p>');      
		echo('<div>Intrinsic Characteristics:<div class="indent">');
		
		$intrinsic = $plantRS['intrinsics_list'];
		$needs = $plantRS['needs_list'];
		$products = $plantRS['products_list'];
		$behaviors = $plantRS['behaviors_list'];
		
		$array = array($intrinsic, $needs, $products, $behaviors);
		$libs = array($db_intrinsics_lib, $db_needs_lib, $db_products_lib, $db_behaviors_lib);
		$headers = array('Intrinsic Characteristics', 'Needs', 'Products', 'Behaviors');
		
		for($j=0; $j< sizeof($array); $j++){
		
			if($j>0){
				echo('<div class="propheading">'.$headers[$j].':<div class="indent">');
			}
		
			if(sizeof($array[$j]) > 0){
				for($i=0; $i< sizeof($array[$j]); $i++){
					$property_ref =  $array[$j][$i]['$ref'];
					$value_ref = $array[$j][$i]['$id'];
				
					$property_query = $libs[$j]->findOne(array('collection'=>$property_ref), array('name'));
					$property = $property_query['name'];
				
					$value_coll = $db->$property_ref;
					$value_query = $value_coll->findOne(array('_id'=>$value_ref));
					$value = $value_query['value'];
				
					echo('<br>'.strval($property).': '.strval($value));
				}
			}
			if($j==0){
				echo("</div></div></div>");
				echo('<div class="rightcolumn">');
			}else{
				echo("</div></div>");
			}
		}
		
		
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
  	//	"collection" : "layer",
  	//	"values" : ["511ae981ff2ca2d43bc464a0", "511ae981ff2ca2d43bc464f9", "511ae981ff2ca2d43bc464b0"....] },
  	//
  	//{ "_id" : ObjectId( "511ae981ff2ca2d43bc464f0" ),
 	//  "property" : "canopy density",
  	//  "collection" : "canopy_density",
  	//  "values" : ["511ae981ff2ca2d43bc464a0", "511ae981ff2ca2d43bc464f9", "511ae981ff2ca2d43bc464b0"....] },
  	//
  	// ... ]

	$propertyList = array();
	$propertyList['name'] = $collection->getName();
	
	
	foreach ($libCursor as $libDoc){
		//Now we go through each pointer in the library, find the actual collection and load its values.
		$property = $libDoc['name'];
		$prop_collection_name = $libDoc['collection'];
		$propCollection = $db->selectCollection($prop_collection_name);
		
		//loading values
		$propCursor = $propCollection->find();
		$val = array();
		foreach ($propCursor as $propDoc){
			//check to see if the library value has a cooresponding description, if so push it to the array and if not only push the value to the array.
			if( array_key_exists('description', $propDoc) ){
				array_push( $val, [ $propDoc['value'], $propDoc['description'] ] );
			} else{
				array_push($val, $propDoc['value']);
			}
		}
	
		
		$propertyList[$property] = $val;
		
	}
	
	return $propertyList;

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

function setup_FA($dbcur){

	return loadFunctionalAnalysis($dbcur);
}

?>