<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
define('DB_SERVER', 'johnny.heliohost.org');
define('DB_USERNAME', 'razaa02_razaa02');
define('DB_PASSWORD', 'OctopusCamel2020');
define('DB_NAME', 'razaa02_corpkg');

/* Attempt to connect to MySQL database */
$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);

// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
?>
