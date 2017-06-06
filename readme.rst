1、首先创建一个python虚拟环境
2、git clone https://github.com/whcy/sclm.git 到本地
3、pip install -r requirement.txt（因为我的机器装的postgresql，所以这里没有MySQL-python,自己用pip install MySQL-python 安装
4、到sknowledge/sknowledge下的setting里修改数据库配置：
      # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': "mysites",
    #     'USER': 'root',
    #     'PASSWORD': 'cy78102',
    #     'HOST': '127.0.0.1',
NAME:数据库名，提前创建好 ，
5、到sknowledge/ 下执行python manage.py collectstatic ���收集静态文件
6、执行python manage.py migrate 数据库迁移
7、执行python manage.py createsuperuser 创建超级用户
8、执行python manage.pu runserver


另：今天装了一个插件 debug-toolbar 方便调试 如果没意外，屏幕右边会有侧边调试工具栏 
