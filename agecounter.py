import datetime
print "Today is: ", datetime.date.today()

print "microseconds:", datetime.timedelta(microseconds=1)
print "milliseconds:", datetime.timedelta(milliseconds=1)
print "seconds     :", datetime.timedelta(seconds=1)
print "minutes     :", datetime.timedelta(minutes=1)
print "hours       :", datetime.timedelta(hours=1)
print "days        :", datetime.timedelta(days=1)
print "weeks       :", datetime.timedelta(weeks=1)

def age(years):
    print "You are %s years old" % years
    print "You are %s days old" % (int(years) * 365)
    print "You are %s hours old" % (int(years) * 8760)
    print "You are %s minutes old" % (int(years) * 525600)
    print "Wow! That's a lot!"

years = raw_input("How many years old are you?")

age(years)