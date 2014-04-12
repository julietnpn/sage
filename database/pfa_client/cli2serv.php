<?php header('content-type: application/json; charset=utf-8');

include('db_functions.php');

if(isset($_GET['q'])){
	$f = strval($_GET['q']);

	if(strcmp($f,'get_FA') == 0 ){
		echo json_encode(get_FA());
	}
}

echo json_encode(get_FA());

function get_FA(){ 
	global $IntrinsicChar, $Need, $Product, $Behavior;
	/*$FA_List = json_encode($IntrinsicChar)."!*!".json_encode($Need)."!*!".json_encode($Product)."!*!".json_encode($Behavior);*/

	$FA_List = [$IntrinsicChar,$Need,$Product,$Behavior];
	
	return $FA_List;
}

?>