exec { 'refresh_cache':
    command => '/usr/bin/env sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
}
