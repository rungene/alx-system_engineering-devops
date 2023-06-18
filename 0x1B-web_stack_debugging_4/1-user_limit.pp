# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
file_line { 'holberton-soft-nofile':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 4096',
  match => '^holberton\s+soft\s+nofile',
}

file_line { 'holberton-hard-nofile':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 8192',
  match => '^holberton\s+hard\s+nofile',
}
