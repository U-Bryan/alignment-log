# Question ---------------------------------------------------------------------------------

# In a file called faces.py, implement a function called convert that accepts a str as input
# and returns that same input with any :) converted to 🙂 and any :( converted to 🙁. 
# All other text should be returned unchanged.
# Then, in that same file, implement a function called main that prompts the user for input, 
# calls convert on that input, and prints the result. 
# Be sure to call main at the bottom of your file.


### Solution ###

# Main function that asks user for input and runs the convert function
def main():
    n = input('Enter a message: ')
    convert(n)

# Convert function that converts users input to smiley face
def convert(i):
    new = i.replace(':(', '🙁')
    new2 = new.replace(':)', '🙂')
    print(new2)

# Main, which runs the main function
main()