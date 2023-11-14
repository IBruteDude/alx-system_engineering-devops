# replacing the wrong name of the wordpress file in its settings
exec { 'replace wrong name':
  command => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'"
}
