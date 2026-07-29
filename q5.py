words = ["Monkey", "kingzz", "Ammar", "don", "kingzz", "l", "k", "kingi", "gi"]

# Step 1: Read the existing file content
with open("q3gg.txt", "r") as f:
    content = f.read()

# Step 2: Replace each word in the list, one at a time
for word in words:
    content = content.replace(word.strip(), "#"*len(word.strip()))

# Step 3: Write the updated text back into the file
with open("q3gg.txt", "w") as f:
    f.write(content)

print("Words replaced successfully!")