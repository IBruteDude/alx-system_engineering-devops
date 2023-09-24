# install puppet module

exec { 'install module':
	command => 'puppet module install puppetlabs-stdlib',
}

include stdlib

file_line {
  'ensure pwd off':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '   PasswordAuthentication no',
  ;
 'ensure private key path correct':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '   IdentityFile ~/.ssh/school',
}
