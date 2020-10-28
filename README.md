> 本项目是一个内容管理系统，基于Django实现，可能会涉及到爬虫的部分(目前还在确定中)
>项目的部署基于Nginx+uwsgi+Django+Mysql+Redis+Supervisor进行部署

1. 提供了以下的功能
+ 自定义startapp命令，实现urls.py文件和serializers.py文件的自动创建
+ 使用多个Mysql数据库，实现了数据库路由

2. 部署流程需要注意的事项

    + nginx配置文件位置
    ```shell script
    which nginx
    ```
    + uwsgi配置文件位置

    + supervisor配置文件cms_uwsgi需要修改
    ```shell script
     directory的值需要改成项目的uwsgi配置文件位置
     environment虚拟环境位置需要修改
    ```
