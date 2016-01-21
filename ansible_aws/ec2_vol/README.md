变量：
-----------
指定tag的k和v，执行添加磁盘

	tag_key: class
	tag_value: test

添加卷的大小和卷的名称

	vol_size: 5
	device_name: /dev/sdf

指定删除卷的id

	vol_id:

操作
----------

	ansible-playbook site.yml --tags=var

var变量如下：

tag=attach：新建卷附加到实例下，使用变量tag-k,v vlo_size,device_name

tag=rm：删除指定实例的卷，使用变量tag-k,v vlo_id

