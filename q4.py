# Step 1: Read the existing file content
with open("q3gg.txt", "r") as f:
    content = f.read()

# Step 2: Replace the word
new_content = content.replace("donkey", "#####" )

# Step 3: Write the updated text back into the file
with open("q3gg.txt", "w") as f:
    f.write(new_content)

print("Word replaced successfully!")