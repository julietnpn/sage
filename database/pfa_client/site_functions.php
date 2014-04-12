<?php
//include ('connect-wp-db.php');

$site_title = '';


function loadSiteDetails(){
	GLOBAL $site_title;
	
	//TO DO: UPDATE THIS TO MONGO
	//This function will set all of the global variables with the site details
	$result = mysql_query("SELECT title FROM SiteInfo WHERE id=1");
	if(mysql_num_rows($result) > 0){
		$site_title = mysql_result($result, 0, 0);
	} else{
		$site_title = "Default Site Title";
	}

}


function get_site_title(){
	GLOBAL $site_title;
	return $site_title;
}
	
function set_site_title($name){
		GLOBAL $site_title;
		if($name != $site_title){
			$site_title = $name;
			//todo: set it sql
		}
	}
	
	
//added for picture uploads
// used in: addToDB.php, viewPlantDetails.php 


// first let's set some variables 

// make a note of the current working directory relative to root. 
$directory_self = str_replace(basename($_SERVER['PHP_SELF']), '', $_SERVER['PHP_SELF']); 

// make a note of the location of the upload handler script 
$uploadHandler = 'http://' . $_SERVER['HTTP_HOST'] . $directory_self . 'upload.processor.php'; 

// set a max file size for the html upload form 
$max_file_size = 10485760; // size in bytes 


?>

