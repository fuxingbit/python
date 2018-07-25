# @Time    : 2018/7/25 11:17
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

# !/usr/bin/python
# coding=utf-8
# ---------------------------------------------------------
# Name:         Tomcat错误日志发送邮件脚本
# Purpose:      收集Tomcat异常日志并发送邮件
# Python：       2.7/2.4  皆可使用
# --------------------------------------------------------
from os.path import getsize
from sys import exit
from re import compile, IGNORECASE
import sms

# 定义tomcat日志文件位置
tomcat_log = '/srv/tomcat-task/logs/task.log'
# 该文件是用于记录上次读取日志文件的位置,执行脚本的用户要有创建该文件的权限
last_position_logfile = '/tmp/last_position.txt'
# 匹配的错误信息关键字的正则表达式
# pattern = compile(r'Exception|^\t+\bat\b',IGNORECASE)
pattern = compile(r'Error in job', IGNORECASE)


# 读取上一次日志文件的读取位置
def get_last_position(file):
    try:
        data = open(file, 'r')
        last_position = data.readline()
        if last_position:
            last_position = int(last_position)
        else:
            last_position = 0
    except:
        last_position = 0
    return last_position


# 写入本次日志文件的本次位置
def write_this_position(file, last_positon):
    try:
        data = open(file, 'w')
        data.write(str(last_positon))
        data.write('\n' + "Don't Delete This File,It is Very important for Looking Tomcat Error Log !! \n")
        data.close()
    except:
        print "Can't Create File !" + file
        exit()


# 分析文件找出异常的行
def analysis_log(file):
    error_list = []
    try:
        data = open(file, 'r')
    except:
        exit()

    last_position = get_last_position(last_position_logfile)
    this_postion = getsize(tomcat_log)
    if this_postion < last_position:
        data.seek(0)
    elif this_postion == last_position:
        exit()
    elif this_postion > last_position:
        data.seek(last_position)
    for line in data:
        if pattern.search(line):
            error_list.append(line)

    write_this_position(last_position_logfile, data.tell())
    data.close()
    return ''.join(error_list)


# 调用发送邮件函数发送邮件
error_info = analysis_log(tomcat_log)

# if __name__ == "__main__":
if error_info:
    print(error_info)
    phone = "17319329936,15311493165,15001030176"
    text = "【253云通讯】您好，你的tomcat-task实例有报错信息，请尽快查看！"

    print(sms.send_sms(text, phone))
    print('短信发送成功')
