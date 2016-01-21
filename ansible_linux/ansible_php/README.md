svn
==============
  用来通过svn同步代码到服务器上

Requirement
==============

  RHEL/centos
  
Guid
==============
  
      svn_url=http:// 
  
      local_url=/data/www
  
  此为一组同步代码的路径，svn_url指定svn服务器的的代码路径，local_url指定本地的存储路径。
  
USE
=============

        anisble-playbook site.yml --limit=test --extra-vars "svn_url=http://svn.abc.tv/svn/coolcms/ local_url=/data/www/api.abc.com"
        
  --limit= 非必须，指定hosts文件里面的test分组执行该playbook，如果不指定，则在hosts文件里面的所有主机执行.
  
  --extra-vars 必须指定的变量，指定了svn的url路径和本地的存放目录。
