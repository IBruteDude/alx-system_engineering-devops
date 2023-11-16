# remove the user no. files security limit
exec { 'comment out the limit':
  path    => '/bin',
  command => 'sed -i "s/holberton/# holberton/" /etc/security/limits.conf',
}
