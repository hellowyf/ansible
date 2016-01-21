介绍
--------
此playbook用于安装python2.7.8 pip setuptool等工具

变量
---------
package=tornado,psutil

package用来指定额外安装的各种软件包，通过pip安装

用法：
--------

ansible-playbook site.yml -i host --extra-vars "package=tornado,psutil"
