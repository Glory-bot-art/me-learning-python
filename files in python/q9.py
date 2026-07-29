with open("kinggz.txt", "r") as input_file:
    with open("kinggz copy.txt", "r") as output_file:  # Opened in read mode to check contents
        if input_file.read() == output_file.read():
            print("The contents are identical!")
        else:
            print("The contents are different.")