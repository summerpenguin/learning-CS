#将参数调入模块
from sys import argv
#在运行代码时需要输入的代码文件名称和需要调用的文件名称
script, filename = argv
将打开特定文件的open命令赋值给变量txt
txt = open(filename)
打印”这里是你的文件,文件名为格式化字符%r带标点映射文件名“
print "Here's your file %r:" % filename
打印变量txt并执行read命令，txt的赋值是打开特定文件
print txt.read()
打印”再打一次文件名“
print "Type the filename again:"
将变量file_again赋值为操作台输入参数，并且该参数以>为提示符
file_again = raw_input("> ")
将变量txt_again赋值为打开特定文件的open命令
txt_again = open(file_again)
打印变量txt_again并执行read命令
print txt_again.read()


