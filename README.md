
# 使用方法
* 通过Sagemaker部署自己的模型，可以是Sagemaker训练的模型，也可以是已经训练好的模型
* 本文采用已经训练好的模型，需要通过Sagemaker sdk 部署模型到Sagemaker endpoint
* 使用仓库中的python代码进行测试，其中包括通过互联网访问的延迟测试，VPC内的延迟测试等
* 

## 准备环境
### 更新awscli
pip install --upgrade --user awscli

### 安装pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

### 安装boto3
pip install boto3

### 设置Ec2角色
设置角色后ec2上的程序才可以访问sagemaker 

### 创建Sagemaker runtime endpoint 
指定ec2所在的VPC 和子网
注意安全组要与ec2的安全组相同，或者单独配置允许ec2的流量访问

## 开始测试
### 执行程序进行测试
python test_sagemaker_endpoint.py


## VPC内测试
### 复制脚本到私有子网服务器
scp -i test-oregon.pem test_sagemaker_endpoint.py ec2-user@172.31.66.133:/home/ec2-user/test_sagemaker_endpoint

### 创建NAT gateway 并更新路由表

## 测试结果
测试结果可以通过Cloudwatch 查看延迟情况并统计
