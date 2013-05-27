import time
t = time.localtime()

monthblock = ["Blank", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

dayblock = ["blank", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "twenty-first", "twenty-second", "twenty-third", "twenty-fourth", "twenty-fifth", "twenty-sixth", "twenty-seventh", "twenty-eighth", "twenty-ninth", "thirtieth", "thirty-first"]

timeblock = ["12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"]

print "\nYour local time and date:\n" 
print "It's", timeblock[t.tm_hour], "&", t.tm_min, "minutes past", "on the", dayblock[t.tm_mday], "of", monthblock[t.tm_mon], "in", t.tm_year

