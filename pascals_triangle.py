# calcualtes rows of pascal's triangle
# no where near the most efficient it could be
# but it works
# coded by Liam Csiffary

counter = 0
number_of_rows = int(input("How many rows of pascal's triangle do you want to calculate: "))
# initializes lists
current_row = []
old_row = [1]
# the loop that calculates the rows
while counter <= number_of_rows:
    last_num = 1
    # adds 1 to the start of each row
    current_row.append(1)

    for each in old_row:
        current_row.append(last_num + each)
        # saves the last number to be added to the next number
        last_num = each

    # adds 1 to the end of each row
    current_row.append(1)
    # removes the second number in the list. For some reason the program makes a 
    # useless number which instead of taking the time to fix I just popped it out
    current_row.pop(1)
    counter += 1
    
    # prints the row of pascals triangle to the user
    print(current_row)
    # resets the lists
    old_row = current_row
    current_row = []
