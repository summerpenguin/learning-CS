# -*- coding: utf-8 -*-。
# 变量x等于"这里有十种人"
x = "There are %d types of people." % 10
# 变量binary等于"binary"
binary = "binary"
# 变量 do_not等于"don’t"
do_not ="don't"
# 变量y等于"这里认识binary和不认识binary的人"
y = "those who know %s and those who %s." % (binary,do_not)
# 打印x
print x
# 打印y
print y
# 打印"我说：格式化字符%r——带标点映射变量X"
print "I said: %r." % x
# 打印"我也说：'格式化字符%s——不带标点映射变量y'"
print "I also said: '%s'." % y
# 变量hilariCous等于False
hilarious = False
# 变量joke_evaluation等于"这个笑话不好笑吗？！ 格式化字符%r"
joke_evaluation = "Isn't that joke so funny?! %r"
# 打印变量joke_evaluation % hilarious
print joke_evaluation % hilarious
# 变量w等于"这里是左边的..."
w = "This is the left side of..."
# 变量e等于"一根有右边的绳子。"
e = "a string with a right side."

print w + e