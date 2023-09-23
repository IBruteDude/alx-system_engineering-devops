# create a temporary 'school' file with attributes
file { '/tmp/school':
  owner => 'www-data',
  group => 'www-data',
  mode => '0744',
  content => 'I love Puppet',
}
