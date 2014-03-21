from sys import argv

script, filename = argv

#returns file
txt = open(filename)

print "Here's your file %r:" % filename
#reads the file returned from open
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

text_again = open(file_again)
print text_again.read()

txt.close()
txt_again.close()

# file(name [, mode [, buffering]]) -> file object
# modes, 'r', 'w', 'a'
# '+' simulataneous read and write
# 'b' binary files

# python
# quit(), ctrl+z