def age(years):
    print "You are %s years old" % years
    print "You are %s days old" % (int(years) * 365)
    print "You are %s hours old" % (int(years) * 8760)
    print "You are %s minutes old" % (int(years) * 525600)
    print "Wow! That's a lot!"

years = raw_input("How many years old are you?")

age(years)