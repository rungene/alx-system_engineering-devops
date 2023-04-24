# Use Puppet to make changes to our configuration file(in a server).
file_line { 'refuse to authenticate using a password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line { 'path to find the private keys':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
