from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

# note, no file object to close after this line
indata = open(from_file ,'r').read()

print "The input file is %d bytes long" % len(indata)

# exists returns true if file exists
print "Does the output fie exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()

# one line copy script
# open(to_file, 'w').write(open(from_file, 'r').read())