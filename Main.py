# Multiplication Table Generator

# Ask the user for a number
num = int(input("Enter the Number: "))

# Initialize the invalid try counter
invalid_tries = 0

while invalid_tries < 3:
    # Ask the user how many multiples they want
    mt = int(input("Enter the number of multiples (5, 10, 15, 20, 25, 30): "))

    # Check if the input is valid
    if mt in [5, 10, 15, 20, 25, 30]:
        print(f"\nMultiplication Table of {num} till {mt}")
        for i in range(1, mt + 1):
            print(f"{num} x {i} = {num * i}")
        break  # Exit the loop if the input is valid
    else:
        invalid_tries += 1
        print(f"Invalid input! You have {3 - invalid_tries} tries left.")

if invalid_tries == 3:
    print("Too many invalid tries. Program is exiting.")

exit()
