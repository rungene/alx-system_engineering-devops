# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
exec { 'holberton-soft-nofile':
  command => 'sed -i "/holberton soft/s/4/4096/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin/',
}

exec { 'holberton-hard-nofile':
  command => 'sed -i "/holberton hard/s/5/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin/',
}
