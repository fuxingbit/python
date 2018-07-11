# @Time    : 2018/7/10 14:53
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

import paramiko

# 创建ssh 对象

ssh = paramiko.SSHClient()

# 允许连接不在known_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname='123.57.133.60', port=22, username='root', password='Alienzjn95@')

# 执行命令

stdin, stdout, stderr = ssh.exec_command('df -h')

res, err = stdout.read(), stderr.read()
result = res if res else err

print(result.decode())

ssh.close()
