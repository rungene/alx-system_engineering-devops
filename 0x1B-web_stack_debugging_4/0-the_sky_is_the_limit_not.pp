# Correcting too many open file error nginx
exec { 'increase ulimit':
  path    => '/bin/',
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
}

exec { 'restart-nginx':
  path    => '/usr/bin/',
  command => 'service nginx restart',
}
