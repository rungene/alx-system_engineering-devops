# Configures a brand new Ubuntu machine setting the custom HTTP header using puppet - automated

exec { 'runs apt-update':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure => 'installed',
  name   => 'nginx',
}

file_line { 'custom HTTP header response - append a line in nginx config file':
  path  => '/etc/nginx/nginx.conf',
  line  => "\tadd_header X-Served-By ${hostname};",
  after => 'http {',
}

exec { 'restart nginx service with sudo privileges':
  command => '/usr/sbin/service nginx restart',
}
