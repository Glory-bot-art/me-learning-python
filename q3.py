from pathlib import Path

# Create the folder if it doesn't exist yet
output_dir = Path("tables")#= the path to the folder
output_dir.mkdir(exist_ok=True)#= create the folder

for i in range(2, 21):
    # Open a new file for each number (e.g., tables/table_2.txt)
    file_path = output_dir / f"table_{i}.txt"#= the path to the file
    
    with open(file_path, "w") as f:
        f.write(f"--- Table of {i} ---\n")
        
        for j in range(1, 11):
            f.write(f"{i:2d} x {j:2d} = {i * j:3d}\n")