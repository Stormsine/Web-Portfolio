<?php
$email = $_POST['email']; // Get the submitted email

// Validate the email (you can add more validation logic here)
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  die('Invalid email format');
}

// Store the email in a file
$file = 'D:/Newfolder/WebJ/email_data.txt';
$current = file_get_contents($file);
$current .= $email . "\n";
file_put_contents($file, $current);

// Display a success message
echo 'Email submitted successfully!';
?>
