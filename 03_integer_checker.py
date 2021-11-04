def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter an integer that is more than (or equal to) {}".format(low)

        try:

            response = int(input(question))

            if response >= low:
                return response

            else:
                print(error)
                print()   
        
        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":
    print()
    var_integer = num_check("Enter an integer: ", 0)
    print()

    image_width = num_check("Image width? ", 1)
    print()
    image_height = num_check("Image height? ", 1)
    