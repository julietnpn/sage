<?php


function define_basic()
{
define(PRODUCT,'ESCan');									//Name of Product
define(ORGANIZATION, 'The Engineering Student Council');	//Name of Organization or Company
define(EMAIL, 'esc.uci@email.com');							//Email seen by users when notified
define(WEBSITE, 'http://yoursite.com/');					//url of your site where this application is hosted
define(DESCRIPTION, 'ESCan Description');					//Description of the system
}


function define_db()
{
define(DBDATABASE, '');  			//MySQL Database Name
define(DBSERVER, ''); 				//MySQL Server usually localhost
define(DBUSERNAME, '');				//MySQL Username
define(DBPASSWORD, ''); 			//MySQL Password
}

function define_webmaster()
{
define(WEBMASTER_USERNAME, ''); 	//Enter the username of the webmaster
define(WEBMASTER_PASSWORD, ''); 	//Enter the password of the webmaster
define(WEBMASTER_EMAIL, ''); 		//Enter the webmaster's email address
}

define_db();
define_basic();
define_webmaster();
?>