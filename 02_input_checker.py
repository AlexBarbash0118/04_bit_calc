
def user_choice():

    valid = False
    while not valid:

        response = input("File type (integer / text / image): ").lower()

        if response == "text" or response == "t":
            return "text"

        else:
            print("Please choose a valid file type!")
            print()



data_type = user_choice()
print("You chose", data_type)

print()