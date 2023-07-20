def encode(password):  # encodes a password by adding 3 to each number (Coded by: Zachary Bradley)
    output_password = ""  # output will be a string
    for number in password:
        temp_number = int(number) + 3  # adds 3 to number
        if temp_number >= 10:  # if number is greater than 10, subtracts 10
            temp_number -= 10
        output_password += str(temp_number)  # string grows each iteration
    return output_password

def decode(password): # coded by lauren kempfe
    decodedpass = ''  # decodedpass is a string
    for num in password:
        if int(num) - 3 < 0: #checks if negative
            temp = int(num) + 7 #adds back 10 and subtracts 3
        else:
            temp = int(num) - 3
        decodedpass += str(temp)
    return int(decodedpass)
        
def main():
    while True:

        # prints the menu

        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        # user input for menu

        option = int(input("Please enter an option: "))

        # Goes through options and follows path chosen by user

        if option == 1:  # encodes password
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:  # left blank for partner to modify
            print(f'The encoded password is {password}, and original password is {decode(password)}.')
        elif option == 3:  # ends function
            break
        else:  # tells user to enter a valid menu number
            print("Error! Enter a valid input")
            
            
if __name__ == '__main__':
    main()
