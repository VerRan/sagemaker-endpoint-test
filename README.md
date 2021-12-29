         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!


sudo mount -t efs -o tls,accesspoint=fsap-0d274b141f1cf8a80 fs-64e2b161:/ efs


复制脚本到私有子网服务器
scp -i test-oregon.pem test_sagemaker_endpoint.py ec2-user@172.31.66.133:/home/ec2-user/test_sagemaker_endpoint

创建NAT gateway 并更新路由表

更新awscli
pip install --upgrade --user awscli

安装pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

安装boto3
pip install boto3

设置Ec2角色
设置角色后ec2上的程序才可以访问sagemaker 

创建Sagemaker runtime endpoint 
指定ec2所在的VPC 和子网
注意安全组要与ec2的安全组相同，或者单独配置允许ec2的流量访问


执行程序进行测试
python test_sagemaker_endpoint.py

