## --- GLobal Vars ---
n1, n2 = 0, 1
count = 0

dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", " 9"]

## --- Functions --
def check_type(n):
    global dig
    # converting to integer
    if n in dig:
        n = int(n)
    else:
        while n not in dig:
            print("\nWrong Type!")
            tmp = input("Please enter only digits?(0-9):")
            n = tmp
        n = int(n)
    return n

def check_num(n):
    # checking if it's negative
    while n <= 0:
        print("\nWrong Number!")
        tmp = input("Please enter only digits?(0-9):")
        if tmp != "0":
            tmp = check_type(tmp)
            n = tmp
        else:
            n = 0

    return n


def main():
    global count, n1, n2
    # getting user input
    num = input("Enter number of terms :")

    # checking input
    num = check_num(check_type(num))

    ## --- MAIN --
    if num == 1:
        print(f"\nFabinocci sequence upto {num} terms:")
        print(n1)
    else:
        print("\nFabinocci sequence:")
        while count < num:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

## --- Main Code ---
main()

