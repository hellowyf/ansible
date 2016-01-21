变量
----------
指定tag的k和v执行开机关机操作

	tag_key: business
	tag_value: BYD

执行更改操作，指定更改后的实例类型

	modify_type: c3.2xlarge

开启实例使用的变量。

	instance_type: c3.4xlarge
	image: ami-1412d
	security_group: launc-22

指定tag的k,v；针对指定的k，v匹配开机的数量，

	exact_count: 1
	tag_k: tag_v

新建机器添加卷的大小和卷的名称

	vol_size:
	dev_name:

新建机器，实例tag的变量字典，如果变量的key对应的value没有值，用""替代表示值为空。在tag.yml文件

	name: "pfv"
	hostname: "pfv"
	class: "webv"
	enviroment: "production"
	business: "v"
	interface: "v"

使用：
----------
	ansible-playbook site.yml --tags=var

tags=stop，关机，使用的变量有tag_key tag_value

tags=start，开机，使用的变量有tag_key tag_value

tags=modify，更改现有实例类型，使用的变量，tag_key tag_value modify_type

tags=launch，新建实例，使用变量，tag.yml文件给新建实例打tag。instance_type，image，security_group,exact_count,count_tag*。
