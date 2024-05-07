print("There is more than one way to say hello:")

# This is a list consisting of three strings
hello_list = ["Hello", "G'day", "Shalom"]

for hello in hello_list:
    print("\t", hello, " World!")

print("\nThese squares are just perfect:")

# This construct is called a 'list comprehension'
squares = [i**2 for i in range(11)]

# You can loop over elements of lists without having to use indexing
for s in squares:
    print("  ", s, end="")

# The last line of every code snippet is also evaluated as output (in addition to
# any figures and printing output generated previously).
import numpy as np
np.sqrt(squares)
