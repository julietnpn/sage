

<?php 


include('header.php');

$default_sort = 'genus';
$allowed_order = array('id', 'genus', 'height', 'spread', 'shape', 'pH', 'sun', 'water', 'hardiness zone');


/* if order is not set, or it is not in the allowed
 * list, then set it to a default value. Otherwise, 
 * set it to what was passed in. */
 
/* 
if (!isset ($_GET['order']) || 
    !in_array ($_GET['order'], $allowed_order)) {
    $order = $default_sort;
} else {
    $order = $_GET['order'];
}

$orderKey = $allowed_order.indexOf($order)
if($order == $allowed_order[0])
	//do whats already happening.
else if($order == $allowed_order[1])
	//get_table_entries_order('Plant', 'genus');
else if($orderKey <5){
	////get_table_entries_order('IntrinsicChars
}*/

?>

<h2 align="CENTER"><a href="addToDB.php">Add Plant</a></h2>

<div id="accordian" ><!--Parent of the Accordion-->

<?php 
//default print in order of entry
$cursor_allPlants = $db_plant_coll->find();

if (!empty($cursor_allPlants)) :
	foreach($cursor_allPlants as $document){
		printDBListing($document);
	}


else: ?>

<p>The database is empty! Please add some plant data!</p>

<?php endif; ?>



</div><!--End of accordion parent-->



<div id="footer">

<!-- Please leave this line intact -->
</div>
</body>
</html>
