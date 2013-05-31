<?php include('db_functions.php'); 
	  ob_start();
	  if (isset($_GET['action'])){
		// Retrieve the GET parameters and executes the function
		  $funcName	 = $_GET['action'];
		  $vars	  = $_GET['vars'];
		  $funcName($vars); 
		  
	 } else if (isset($_POST['action'])){
		  // Retrieve the POST parameters and executes the function
		  $funcName	 = $_POST['action'];
		$vars	  = $_POST['vars'];
		$funcName($vars); 
	 } 

	

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>working</title>
</head>
<body>working</body>
</html>

<?php 

while (ob_get_status()) 
{
    ob_end_clean();
}

header("Location: index.php");
exit;
?>