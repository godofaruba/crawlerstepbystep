# crawlerstepbystep

本项目仅作为爬虫入门联系，来更好熟悉Google人脸爬取流程

其中以项目 `Lab3_2: IMDb黑人女演员名单爬取` 作为主要姓名信息爬取操作，图像爬取使用google_images_download包更加全面
## 服务器配置

安装anaconda

```
wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
sh Anaconda3-5.1.0-Linux-x86_64.sh
```

新建并激活爬虫环境crawler

```
conda create -n crawler python=3.6
source activate crawler
```

安装google-images-download包

```
pip install google_images_download
```

安装dlib、numpy和opencv包

```
pip install cmake
pip install dlib
pip install opencv-python
pip install numpy
```

新建爬取工作目录

```
mkdir downloads
```

下载dlib项目文件（可选）

```
git clone https://github.com/davisking/dlib.git
```

上传名单keywords.txt到~/downloads爬取工作目录

//开始爬取Google名单对应图片

```
googleimagesdownload -kf "./keywords.txt" -l 100 -s ">800*600" -t "face"
```

##### 后台执行防止中断 推荐

```
nohup googleimagesdownload -kf "./keywords.txt" -l 100 -s ">800*600" -t "face" > 1.out 2>&1 &
```

复制文件从外网服务器到内网服务器

```
scp -r root@142.93.85.232:/root/google-crawler/downloads/downloads/ /home/xiongweiyu/downloads
```

在内网服务器使用dlib人脸聚类处理

```shell
nohup python ./face_clustering.py ./weights/shape_predictor_5_face_landmarks.dat ./weights/dlib_face_recognition_resnet_model_v1.dat ./downloads/ ./outputs/  > 1.out 2>&1 &
```

查看输出信息

```shell
cat 1.out
```

查看后台进程运行情况（shell关闭后失效）

```shell
jobs -l
```

查看后台进程号

```shell
ps -ef | grep nohup.sh
```

终止前台运行的进程

```
Ctrl+C
```

终止后台运行的进程

```shell
kill -9  进程号PID/job号
```

如果某个进程起不来，可能是某个端口被占用

查看使用某端口的进程（端口->进程）

```shell
lsof -i:8090
```

查看到进程id之后，使用netstat命令查看其占用的端口

```shell
netstat -anpt |grep 7779
```

