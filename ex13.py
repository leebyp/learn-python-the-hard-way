#import modules needed
from sys import argv

#takes whatever is in argv, unpacks, and assigns to all the variables on the left
script, int(first), int(second) = argv
third = raw_input("What's your third variable? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
