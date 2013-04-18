<?php
ini_set("session.cookie_domain","esc.eng.uci.edu/escan");
// Show all information, defaults to INFO_ALL


ini_set('display_errors', 1); 
ini_set('expose_php', 1); 
ini_set('display_startup_errors', 1);
ini_set('log_errors', 1); 
ini_set('sendmail_from', 'esc.uci@gmail.com');
ini_set('error_log', 'error_log.txt');
error_reporting(E_ALL);

phpinfo();

?>
