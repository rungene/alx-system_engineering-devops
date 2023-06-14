# Puppet script that search for the string .phpp and replace it with the string .php
exec { 'fix_typo_php_files':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
