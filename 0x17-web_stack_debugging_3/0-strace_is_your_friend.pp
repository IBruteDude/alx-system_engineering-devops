# Changes the false file name causing server error
exec { 'edit_false_file_name':
    command => '/usr/bin/env sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
}
