<?php
include('include/config.php');
//session_start();

$username = "";
$password = "";

if($_SERVER["REQUEST_METHOD"] == "POST") {

// username and password sent from form

      $username = mysqli_real_escape_string($link,$_POST['username']);
      $password = mysqli_real_escape_string($link,$_POST['password']);

      $sql = "SELECT id FROM users WHERE username = '$username' and password = '$password'";
	  $result = mysqli_query($link,$sql);
      $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
      $active = $row['active'];

      $count = mysqli_num_rows($result);
      //echo $count;

      // If result matched $username and $password, table row must be 1 row

      if($count == 1) {

      $_SESSION['username'] = $username;

      //echo "Hi, ".$_SESSION['username'];

         header("location: welcome.php");

   }

}


?>
