# Question -------------------------------------------------------------------------------------------------------------

# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.


### Solution ###

# Promp the user for input and format the input to remove whitespaces and convert string to lowercase
gqol = input('What is the Great Question of Life, the Universe and Everything: ').lower().strip()

# Conditional statement that prints yes if the users input meets the requirement, or no if otherwise
if gqol == '42' or gqol == ("forty-two") or gqol == ('forty two'):
    print("Yes")
else:
    print("No")
