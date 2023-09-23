# execute a command
exec { 'pkilling':
  command => 'sudo pkill --signal TERM killmenow',
}
