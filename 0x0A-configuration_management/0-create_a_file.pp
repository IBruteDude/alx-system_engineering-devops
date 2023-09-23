# create a temporary 'school' file with attributes
file { 'starter':
  path => '/tmp/school',
  owner => 'www-data',
  group => 'www-data',
  mode => '0744',
  content => 'I love Puppet',
}
