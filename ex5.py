name = 'Michael Zimmermann'
age = 19
height = 74
weight = 220
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kilos = weight / 2.2046
cm = height * 2.54

print "Let's talk about %s" % name
print "He's %d cm tall." % cm
print "He's %d kilos heavy." % kilos
print "He could lose some weight!"
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s, depending on the coffee." % teeth
print "If I add %d, %d, and %d, I get %d." % (age, height, weight, age + height + weight)