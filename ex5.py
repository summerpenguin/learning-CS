name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180.0 # ibs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
centimeters = height * 2.54
kilograms = weight / 2.2

print "Let's talk about %r." % name
print "He's %r centimeters tall." % centimeters
print "He's %r kilograms heavy." % kilograms
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)