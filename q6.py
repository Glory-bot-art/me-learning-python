with open("log.txt", "r") as f:
    k=f.read()

    if "python" in k:
        print("python is here. ")
        print(k.find("python"))
    else:
        print("nope no python in this lil bro")