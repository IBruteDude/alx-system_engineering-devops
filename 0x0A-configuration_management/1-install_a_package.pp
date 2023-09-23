# installs flask on the server
package { 'pipflask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}
