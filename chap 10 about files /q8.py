# for making copy of file
with open("kinggz.txt", "r") as input_file:
    content = input_file.read()
    with open("kinggz copy.txt", "w") as output_file:
        output_file.write(content)