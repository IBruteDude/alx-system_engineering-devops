# installs flask on the server
package { 'pipflask':
  name        => 'flask',
  provider    => 'pip3',
  ensure      => '2.1.0',
}
