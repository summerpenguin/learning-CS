#将参数调入模块
from sys import argv
#在运行代码时需要输入的代码文件名称和需要调用的文件名称
script, filename = argv
#打印”我们将要擦除文件，文件名为格式化字符%r带标点映射文件名“
print "We're goint to erase %r." % filename
#打印”如果你不想这么做，可以按CERL-C键终止进程“
print "If you don't want that, hit CRTL-C (^C)."
#打印”如果你想这么做，请点击RETURN键“
print "If you do want that, hit RETURN."

#以”？“为提示符读取控制台的输入
raw_input("?")

#打印#开启文件。。。#
print "Opening the file..."
#为变量target赋值为开启命令，开启对象是写入状态下的文件名
target = open(filename, 'w')

#打印”正在清空文件。再见！“
print "Truncating the file. Goodbye!"
#使变量target执行truncate命令
target.truncate()

#打印”现在我将针对文本文件中的三行对你提问“
print "Now I'm going to ask you for three lines."

#以”第一行：“为提示符读取控制台的输入，并将其赋值给变量line1
line1 = raw_input("line 1: ")
#以”第二行：“为提示符读取控制台的输入，并将其赋值给变量line2
line2 = raw_input("line 2: ")
#以”第三行：“为提示符读取控制台的输入，并将其赋值给变量line3
line3 = raw_input("line 3: ")

#打印”我即将要将这些信息输入到文件中。“
print "I'm going to write these to the file."
，c
#使变量target执行write命令，材料是变量line1的赋值
target.write(line1)
#使变量target执行write命令，材料是分行符
target.write("\n")
#使变量target执行write命令，材料是变量line2的赋值
target.write(line2)
#使变量target执行write命令，材料是分行符
target.write("\n")
#使变量target执行write命令，材料是变量line3的赋值
target.write(line3)
#使变量target执行write命令，材料是分行符
target.write("\n")

#打印“于是结束了，让我们关闭文件。”
print "And finally, we close it."
#使变量target执行close命令，关闭文档并保存
target.close()
