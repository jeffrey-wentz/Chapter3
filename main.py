def collatz(number):
    if number % 2 == 0:
        number = number / 2
        print(str(number))
    else:
        number = 3 * number + 1
    return number


try:
    user_num = int(input("Enter your number: "))
    while user_num > 1:
        user_num = collatz(user_num)
except ValueError:
    print("Must enter an integer!")

