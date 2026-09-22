'''num= int(input("Enter a number: "))

def EvenOdd():
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
EvenOdd()


age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: Rs. "))
job = input("Do you have a valid job? (yes/no): ").lower()
requested_loan = float(input("Enter the loan amount you want: Rs. "))

# Determine maximum loan amount
if income >= 30000 and income < 50000:
    maximum_loan = 300000
elif income >= 50000 and income < 80000:
    maximum_loan = 500000
elif income >= 80000 and income < 100000:
    maximum_loan = 800000
elif income >= 100000:
    maximum_loan = 1000000
else:
    maximum_loan = 0

print("\n----- Loan Details -----")
print("Maximum loan available: Rs.", maximum_loan)
print("Requested loan amount: Rs.", requested_loan)

# Check eligibility
if age < 21:
    print("Loan status: Not Approved")
    print("Reason: You must be at least 21 years old.")

elif income < 30000:
    print("Loan status: Not Approved")
    print("Reason: Your monthly income must be at least Rs. 30,000.")

elif job != "yes":
    print("Loan status: Not Approved")
    print("Reason: You must have a valid job.")

elif requested_loan > maximum_loan:
    print("Loan status: Not Approved")
    print("Reason: The requested loan amount exceeds the maximum allowed limit.")

elif requested_loan <= 0:
    print("Loan status: Not Approved")
    print("Reason: The requested loan amount must be greater than zero.")

else:
    print("Loan status: Approved")
    print("Congratulations! Your loan request has been approved.")



text = input("Enter a string with at least 8 characters: ")

# Check the length
if len(text) < 8:
    print("Please enter a string with at least 8 characters.")

else:
    # Display ASCII value of each character
    print("\nASCII values:")

    for character in text:
        print(character, "=", ord(character))

    # Convert characters at positions 2, 4, 6, 8, ... to uppercase
    result = ""

    for i in range(len(text)):
        character = text[i]

        # Positions are 2, 4, 6, 8...
        if (i + 1) % 2 == 0:
            ascii_value = ord(character)

            # Check if the character is lowercase
            if 97 <= ascii_value <= 122:
                ascii_value = ascii_value - 32
                character = chr(ascii_value)

        result = result + character

    print("\nFinal modified string:", result)
'''


number = int(input("Enter a 3-digit positive integer: "))

# Check if the number is a valid 3-digit positive integer
if number < 100 or number > 999:
    print("Please enter a 3-digit positive integer.")

else:
    # Decimal
    print("Decimal:", number)

    # Binary
    print("Binary:", bin(number))

    # Octal
    print("Octal:", oct(number))

    # Hexadecimal
    print("Hexadecimal:", hex(number))

    # Last digit
    last_digit = number % 10
    print("Last digit:", last_digit)

    # Check Even or Odd
    if number % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")
