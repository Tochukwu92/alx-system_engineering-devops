# enable the user holberton to login and open file without error.

# increase hard file limit for holberton user.
exec {'increase-hard-file-limit':
	command	=> 'sed -i "/^holberton hard/s/4/50000/" /ect/security/limits.conf',
	path	=> '/usr/local/bin/:/bin/'
}

# increase soft file limit for holberton user.
exec { 'increase-soft-file-limit':
	command	=> 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',
	path	=> '/usr/local/bin/:/bin/'
}
