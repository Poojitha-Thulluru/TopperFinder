def is_probable_topper_number(number):
    # Converting the number to a string
    number_str = str(number)

    # Calculate the sum of odd and even digits
    odd_sum = 0
    even_sum = 0

    for digit in number_str:
        if digit.isdigit():
            digit_value = int(digit)
            if digit_value % 2 == 0:
                even_sum += digit_value
            else:
                odd_sum += digit_value

    # Check if the sum of odd digits is equal to the sum of even digits
    return odd_sum == even_sum

# Get input from the user and handle exceptions
while True:
    try:
        number = int(input("Enter the number: "))

        # Check if the number is non-negative
        if number < 0:
            print("Invalid input. Please enter a non-negative integer.")
            continue

        # Check if the number is a probable topper number
        if is_probable_topper_number(number):
            print("The number", number, "is a probable topper number.")
        else:
            print("The number", number, "is not a probable topper number.")
        break

    except ValueError:
        print("Invalid input!! Please enter an Integer")