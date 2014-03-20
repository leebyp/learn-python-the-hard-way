print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# raw_input([prompt])	prompt written to output without trailing newline
# read line from input and convert to string

#*security problems*
#input([prompt])		eval(raw_input([prompt]))
#eval()		parsed and evaluated as python expression