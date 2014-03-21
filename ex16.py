#	.close()				close file
# 	.flush()				flush internal buffer
#	.read([size])			reads content of file, [size] max bytes
#	.readline([size])		reads one line of text file contains trailing newline, [size] max bytes
#	.truncate([size])		empties file, truncate to size
#	.write(str)				writes a string to file, no return value
#	.writelines(sequence)	write sequence of strings to file

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
# ctrl-c, ctrl-z kills the script
print "If you don't want that it CTRL-C (^C)."
print "If you do want that, hit RETURN"
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s" % (line1, line2, line3))

print "And finally, we close it."
target.close()

target2 = raw_input("Now read which file: ")
text2 = open(target2, 'r')
print text2.read()
text2.close()

# 'w' write, 'r' read, 'a' append
# '+' read and write

# 'w' erases existing file with the same name