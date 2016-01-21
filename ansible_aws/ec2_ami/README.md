变量
-----------
创建ami使用实例的id

	instance_id: i-2ecd2016
新建ami的名称

	ami_name: test
需要删除的ami的id

	ami_id: ami-b61f8d8f

操作：
----------

	ansible-playbook site.yml --tags=var

var变量如下：

tag=create：创建AMI，使用变量instance_id  ami_name

tag=del：删除AMI，使用变量ami_id
