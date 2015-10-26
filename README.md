# millions
Python suite to open millions of connections to millions of IPv6 addresses

## Requirements

#### /etc/sysctl.conf

~~~
fs.file-max = 4200000
fs.nr_open = 4200000
net.ipv4.ip_local_port_range = 1025 65535
net.core.somaxconn = 50000
~~~

#### /etc/security/limits.conf

~~~
root             -       nofile          4000000
~~~

#### EPEL and python packages

~~~
yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum -y install python-pip

pip install py2-ipaddress
pip install pyroute2
~~~

## License

Creative Commons Zero 1.0 Universal

*"No Rights Reserved"*
