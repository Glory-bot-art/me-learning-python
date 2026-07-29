# GOOD: Keeps file open longer than needed
with open("poem.txt", "r") as input_file:
    content = input_file.read()
    if "twinkel" in content:
        print("\nit has twinkel")
    else:
        print("\nit does not have twinkel")
    print(content) # File is still held open during all these print statements


# BEST: File closes immediately after reading!
with open("poem.txt", "r") as input_file:
    content = input_file.read()

# File is safely closed NOW. Everything below uses memory:
if "twinkel" in content:
    print("\nit has twinkel")
else:
    print("\nit does not have twinkel")
print(content)