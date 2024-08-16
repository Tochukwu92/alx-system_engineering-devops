# Fixes bad "phpp" extention to "php" in "wp-settings.php"

exec{'fix-wordpress':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path    => '/usr/local/bin/:/bin/'

#  Fix permission for the web directory

file { '/var/www/html':
	ensure	=> directory,
	owner	=> 'www-data',
	group	=> 'www-data',
	mode	=> '0755',
	recurse	=> true,

#  Ensure Apache is running

service { 'apache2':
	ensure	=> running,
	enable	=> true,
