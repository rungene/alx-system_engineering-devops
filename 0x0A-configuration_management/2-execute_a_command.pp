# a manifest that kills a process named killmenow
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
