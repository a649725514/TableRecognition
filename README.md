# 基于百度表格识别API接口实现图片转Excel
## 一、使用方法
1. 领取百度智能云文字识别免费额度，并创建应用，获取API_KEY和SECRET_KEY
2. 在TableRecognition.py同级目录下创建config.ini配置文件，配置文件内容如下：
   ```ini
   [DEFAULT]
    BAIDU_API_KEY = #替换成获取的API_KEY
    BAIDU_SECRET_KEY = #替换成获取的SECRET_KEY
   ```
3. 通过pip安装configparser依赖
   ```shell
   python -m pip install configparser
   ```
4. 运行脚本，输入图片所在的文件夹路径即可
   ```shell
   python TableRecognition.py
   ```
## 二、运行截图
![运行截图](https://www.picgo.net/image/1.ojk9G7)

![原图](https://www.picgo.net/image/1.ojo85l)

![效果图](https://www.picgo.net/image/2.ojoRXj)

## 三、打包成可执行文件
1. 通过pip安装pyinstaller依赖
   ```shell
   python -m pip install pyinstaller
   ```
2. 执行下述命令打包
    ```shell
    pyinstaller --onefile TableRecognition.py
    ```