# remove the user no. files security limit
exec { 'unlimit the nofiles limit':
  path    => '/bin',
  command => 'echo -e "www-data\thard\tnofile\t\tunlimited\nwww-data\tsoft\tnofile\t\tunlimited" >> /etc/security/limits.conf' ,
}
