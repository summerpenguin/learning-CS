# -*- coding: utf-8 -*-��
# ����x����"������ʮ����"
x = "There are %d types of people." % 10
# ����binary����"binary"
binary = "binary"
# ���� do_not����"don��t"
do_not ="don't"
# ����y����"������ʶbinary�Ͳ���ʶbinary����"
y = "those who know %s and those who %s." % (binary,do_not)
# ��ӡx
print x
# ��ӡy
print y
# ��ӡ"��˵����ʽ���ַ�%r���������ӳ�����X"
print "I said: %r." % x
# ��ӡ"��Ҳ˵��'��ʽ���ַ�%s�����������ӳ�����y'"
print "I also said: '%s'." % y
# ����hilariCous����False
hilarious = False
# ����joke_evaluation����"���Ц������Ц�𣿣� ��ʽ���ַ�%r"
joke_evaluation = "Isn't that joke so funny?! %r"
# ��ӡ����joke_evaluation % hilarious
print joke_evaluation % hilarious
# ����w����"��������ߵ�..."
w = "This is the left side of..."
# ����e����"һ�����ұߵ����ӡ�"
e = "a string with a right side."

print w + e