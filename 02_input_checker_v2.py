
def user_choice():

    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", 'img', "pix", "picture", "pic", "p"]

    valid = False
    while not valid:

        response = input("File type (integer / text / image): ").lower()
        
        if response in text_ok: 
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image")    
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            print("Please choose a valid file type!")  
            print()

keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)
    print()
