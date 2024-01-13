#Modify the "Times Table" again so that the user still enters the number of the table,
#but if this number is negative the table is printed backwards. So entering "-7"
#would produce the Seven Times Table starting at "12 times" down to "0 times".

def times_table():
    table_number = int(input("Enter the number for the times table (-12 to 12): "))

    if -12 <= table_number <= 12:
        if table_number >= 0:
            for i in range(13):  # Loop from 0 to 12 inclusive
                result = i * table_number
                print(f"{i} x {table_number} = {result}")
        else:
            for i in range(12, -1, -1):  # Loop backward from 12 to 0 inclusive
                result = i * table_number
                print(f"{i} x {table_number} = {result}")
    else:
        print("Error: Please enter a number between -12 and 12.")

# Call the times_table function
times_table()
