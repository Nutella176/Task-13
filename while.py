#Using the while loop, ask user to enter a number until -1 is entered, then break
#Calculate the average of the numbers entered excluding -1

count_num_input = 0
sum_numbers = 0

while True:
    number = int(input("Please enter a number: "))
    if number != -1:
        count_num_input += 1
        sum_numbers += number
    else:
        break 
    
print(sum_numbers / count_num_input)
        
