# Question ----------------------------------------------------------------------------------------------------------
# Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:
# dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), 
# remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
# percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), 
# remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
# Assume that the user will input values in the expected formats


### Solution ###

# Main function that takes the dollar and percent input from user and runs float functions on both
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Function that takes an input, removes the dollar sign, converts it to float and returns the converted value
def dollars_to_float(d):
    d = d.replace('$', '')
    d = float(d)
    return d

# Function that takes and input, removes the percent sign, divides by 100 (to convert to percent) and returns value
def percent_to_float(p):
    p = p.replace('%', '')
    p = int(p) /100
    return p

# Main, which runs the main function
main()
