print("Options:")
print("1 - [+]")
print("2 - [-]")
print("3 - [*]")
print("4 - [/]")
print("5 - [//]")
print("-=-"*20)

usr_select = int(input("Select one option: "))

if usr_select == 1:
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    calc = n1 + n2
    
    print(f"The aswer are: {calc}")

if usr_select == 2:
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    calc = n1 - n2
    
    print(f"The aswer are: {calc}")

if usr_select == 3:
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    calc = n1 * n2
    
    print(f"The aswer are: {calc}")

if usr_select == 4:
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    calc = n1 / n2
    
    print(f"The aswer are: {calc}")

if usr_select == 5:
    n1 = int(input("First Number: "))
    n2 = int(input("Second Number: "))
    calc = n1 // n2
    print(f"The aswer are: {calc}")
