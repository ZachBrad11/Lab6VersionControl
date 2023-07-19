def encode(password):
    output_password = ""
    for number in password:
        temp_number = int(number) + 3
        if temp_number >= 10:
            temp_number -= 10
        output_password += str(temp_number)
    return output_password
        
        
def main():
    while True:
        print("Menu\n\n"
              "-------------\n\n"
              "1. Encode\n\n"
              "2. Decode\n\n"
              "3. Quit\n\n\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            pass
        elif option == 3:
            break
        else:
            print("Error! Enter a valid input")
            
            
if __name__ == '__main__':
    main()