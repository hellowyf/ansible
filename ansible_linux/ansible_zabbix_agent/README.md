变量
----------
server_ip: 指定zabbix服务器的ip地址，
需要在host文件的ip后面加一列 a=hostname 比如：
	172.31.2.111	a=AWS-MPP.haproxy001.172-31-2-111

使用
----------
	ansible-playbook site.yml -i host_path

ChangeLog
----------
将install和config zabbix分离，

对于已经安装了zabbix，只是更改配置文件的操作，指定tag为config即可

	ansible-playbook site.yml --tags=config
