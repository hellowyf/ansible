变量
----------

指定tag的k和v，将符合条件的ec2添加到elb下,ec2_mode指定是在elb下添加实例还是删除实例(add/del)

	tag_key: class
	tag_value: test
	ec2_mode: del

指定执行操作的elb名称,包括新建elb，删除elb，添加或删除ec2

	elb_name: test

新建elb需指定安全组id

	sg_id: sg-49312f2b

实例健康检测配置，检测协议，端口，http协议需指定检测路径ping_path，tcp不需要，超时时间，不健康次数，健康次数

	ping_protocol: tcp
	ping_port: 80
	ping_path:
	timeout: 30
	interval: 60
	unhealthy: 2
	healthy: 2

负载均衡的调度协议和端口

	protocol: http
	port: 80
	instance_protocol: http
	instance_port: 80
操作：
----------

	ansible-playbook site.yml --tags=var

var如下：

tags=create：创建elb，使用变量elb_name,sg_id,健康检测和负载均衡调度协议

tags=del：删除elb，使用变量elb_name
  tags=ec2：在elb下删除或者添加实例，具体操作取决于变量ec2_mode，指定tag_k,v
