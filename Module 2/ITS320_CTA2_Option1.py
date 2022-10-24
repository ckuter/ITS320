# Option #1: Creating a Python Application
# Author: Clarissa Kuter
def main():
    input_string = input("Enter a string (max 50 characters): ")

    if len(input_string) > 50:
        print("String too long. Please enter a shorter string.")
        exit(1)

    is_alnum = False
    is_alpha = False
    is_digit = False
    is_lower = False
    is_upper = False

    for i in range(0, len(input_string)):
        if input_string[i].isalnum():
            is_alnum = True
        if input_string[i].isalpha():
            is_alpha = True
        if input_string[i].isdigit():
            is_digit = True
        if input_string[i].islower():
            is_lower = True
        if input_string[i].isupper():
            is_upper = True

    print("Your string contains alphanumeric characters: " + str(is_alnum))
    print("Your string contains alphabetical characters: " + str(is_alpha))
    print("Your string contains digits: " + str(is_digit))
    print("Your string contains lowercase characters: " + str(is_lower))
    print("Your string contains uppercase characters: " + str(is_upper))

if __name__ == "__main__":
    main()
