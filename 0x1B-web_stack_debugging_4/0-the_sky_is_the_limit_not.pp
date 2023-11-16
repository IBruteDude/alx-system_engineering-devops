# enable disabled multi_accept option in nginx
exec { 'enable multi_accept':
  path    => '/bin',
  command => 'sed -i "s/# multi_accept/multi_accept/" /etc/nginx/nginx.conf',
}
