# execute a command
exec { 'pkilling':
  command => 'pkill --signal TERM killmenow',
}
