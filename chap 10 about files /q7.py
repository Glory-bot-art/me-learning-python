with open("log.txt", "r") as f:
    k = f.read()

if "python" in k:
    print("python is here.")
    # get the line number instead of character index
    for i, line in enumerate(k.splitlines(), start=1):
        if "python" in line:
            print(f"found on line {i}")
            
else:
    print("nope no python in this lil bro")