<?php
/* 
 CONNECT-DB.PHP
 Allows PHP to connect to your database
*/

 // Database Variables (edit with your own server information)
 $db_name = 'plantdb_oc';
 
 //Ju's shit from before
 //server is only used if not default localhost
 //$server = 'localhost:27020';
 //$user = 'root';
 //$pass = 'root';

 
 // Connect to Database
 // server is only used if not default localhost
 //$pgconnection = new MongoClient($server);
 
 
 $pgconnection = new MongoClient();
 $db = $pgconnection->$db_name;
 
 $db_plant_coll = $db->plant_lib;
 $db_general_lib = $db->general_lib;
 $db_intrinsics_lib = $db->intrinsics_lib;
 $db_needs_lib = $db->needs_lib;
 $db_products_lib = $db->products_lib;
 $db_behaviors_lib = $db->behaviors_lib;
 
?>