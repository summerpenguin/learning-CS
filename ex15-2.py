filename = raw_input("What is the filename?")

txt = open(filename) 

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"

txt_again = open(filename)

print txt_again.read()


