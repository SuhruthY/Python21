import sys

## --- FUNCTIONS ---
# function to check leap year
def leap_it(year):
    if (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0):
         print(f"\n{year} is a leap year")
    else:
        print(f"\n{year} is not a leap year")

# Check user input
def check_input(year):
    while (len(year) < 1) | (len(year) != 4):
        year = input(f"\nWrong Input!\nEnter Again:")

    return year

# function tpo seek user input
def ask_user():
    year = input("Enter a year:")

    check_input(year)

    try:
        return int(year)
    except:
        print("\nEnter only numbers")
        sys.exit("Wrong input!")

## --- Main prog ---
leap_it(ask_user())

qn = input("\nWanna try for other one (Y/N):")
while qn in ["Y", "y", "N", "n"]:
    leap_it(ask_user())
    qn = input("\nWanna try for other one (Y/N):")


