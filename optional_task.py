#Ask user to enter a number <= 100
#If the number is > 100, display error message 
#When valid number is entered, check if even
#If even multiply by 2 otherwise multiply by 3. Print in both cases

while True:
    number = int(input("Please enter a number equal to or less than 100: "))
    if number % 2 == 0:
        print(number * 2)
    else:
        print(number * 3)
    if number > 100:
        print("Please try again!")

