变量
----------
指定tag的k和v执行添加和删除eip操作

	tag_key: class
	tag_value: test
操作：
----------

	ansible-playbook site.yml --tags=var

var如下：

tag=connect：关联实例和EIP，变量tag-k，v

tag=disconnect：取消实例和EIP的关联，变量tag-k，v
