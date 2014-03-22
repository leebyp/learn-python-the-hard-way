and
del			#remove slices from list, or whole variables
from		#from x import y
not			
while
as 			#relabeling to perform try
			with open("hello.txt", "wb") as f:
				f.write("Hello Python!\n")
			equiv to
			f = open("hello.txt", "wb")
			try:
				f.write("Hello Python\n")
			finally:
				f.close()
elif
global		#declaration for entire current code block, listed identifiers as globals
or
with 		#
assert		#checks condition, true => nothing, false => raise AssertionError
else
if
pass		#placeholder for when require syntax
			def f(arg): pass
yield		#normal function / subroutines
			#function creates a series of values
			#transfer temporary control back to point of call
			#save the work of the function
			#generators / coroutines
			#yield just as return for generator functions
			def simple_generator_function():
				yield 1
				yield 2
				yield 3
			for value in simple_generator_function():
				print(value)
			-> 1, 2, 3
			our_generator = simple_generator_function()
			next(our_generator)
			-> 1
			next(our_generator)
			-> 2
			next(our_generator)
			-> 3

			def get_primes(number):
				while True:
					if is_prime(number):
						yield number
					number += 1

			#reach end of definition / return
			#StopIteration exception raised

			def get_primes(number):
				while True:
					if is_prime(number):
						number = yield number
					number += 1
			def print_successive_primes(iterations, base=10):
				prime_generator = get_primes(base)
				prime_generator.send(None)		#execute code from generator to first yield
				for power in range(iterations):
					print(prime_generator.send(base**power))	#send value to generator and returns value yielded by generator
break		#terminates loop
except
import
print
class:		#declare class
exec 		#execute a file / string of python code / code created by compile function
in
raise 		#raise errors
continue	#continue next iteration loop
finally		#try... except... finally...
is 			#identity comparison
return
def: 		#define function:
for
lambda: 	#create anonymous functions
			lamda x: x%3 == 0
try

True
False
None
strings
numbers
floats
lists

\\
\'
\"
\a
\b
\f 
\n 
\r 
\t 
\v 

%d
%i
%o
%u
%x
%X
%e
%E
%f
%F
%g
%G
%c
%r
%s
%%

+
-
*
** 			#power
/
//			#floor division
%
<
>
<=
>=
==
!=
<>			#similar to !=
( )
[ ]
{ }
@			#applies a decorator to a function
			#decorator is a callable that takes a function as an argument and returns a replacement function
			#(function within a function)
			#simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
,	
:
.
=
;
+=
-=
*=
/=
//=
%=
**=

