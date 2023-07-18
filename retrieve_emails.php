<?php
$file = 'D:/Newfolder/WebJ/email_data.txt';
$emails = file_get_contents($file);
$emailsArray = explode("\n", $emails);

// Display the emails
foreach ($emailsArray as $email) {
  echo $email . '<br>';
}
?>
