from sys import argv

script, first, second, third, fourth = argv

print "The script is called:", script
print "The flower is:", first
print "The penguin is:", second
print "The diamond is:", third
print "The bird is:", fourth

name = int(raw_input("Who is you?"))
mobilephone_number = raw_input("What is your number?")

print "Your name is %s and your number is %s." % (name, mobilephone_number)