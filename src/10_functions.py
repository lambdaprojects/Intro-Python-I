# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def isEvenOdd(t):
    if (t%2 == 0):
        return 'Even!'
    else:
        return 'Odd!'

print(isEvenOdd(num))
