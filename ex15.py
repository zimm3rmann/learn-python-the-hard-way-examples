from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
write = raw_input("New text: ")
print write
print txt.read()
