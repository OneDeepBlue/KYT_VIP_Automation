
自动化测试框架Demo:
    config:
        存放测试用例管理配置文件和测试用例数据配置文件
    docs:
        文档目录
    Libs:
        ShareBusiness：业务函数库
	ShareModules：公共函数库
    mysql_bak:
        mysql数据库备份文件
    output:
        logs: 存放测试执行生成的日志
        report: 存放测试执行生成的结果
	screenshot：存放浏览器截图
    po:
        存放页面对象的类
    Scripts:
        存放测试脚本
    runtest.py:
        测试执行的入口程序

====================================================================
requirements.txt 项目的依赖清单说明

导出依赖清单的方法（可能会导出不全）：
	这里需要使用到的工具叫pipreqs,先安装: pip install pipreqs 
	装好之后cmd到项目路径下: pipreqs ./
	然后输入：type requirements.txt
	使用requirements.txt自动安装所有依赖包
	一条命令全搞定：pip install -r requirements.txt

====================================================================