IPMI
==============
	远程桌面管理工具

Requirement
==============

	RHEL/centos  dell服务器
  
  
USE
=============

	anisble-playbook site.yml -i host.yml

host.yml
============
	10.100.10.10 ipmi_ip=10.200.10.10
    被管理服务器ip		ipmi的地址
