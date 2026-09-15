with open("input.dat") as file: commands = [command.strip() for command in file.readlines()]
path = "/home"
dirs = {"/home": 0}
# Process every command
for command in commands:
    # Commands that start with $
    if command[0]=="$":
        # Do nothing when listing directories or files
        if command[2:4] == "ls":
            pass
        # Manage changing paths
        elif command[2:4]=="cd":
            # Go back to root
            if command[5:6]=="/":
                path = "/home"
            # Go back in the path
            elif command[5:7]=="..":
                path = path[:path.rfind("/")]
            # Change path
            else:
                dir_name = command[5:]  # Getting the name of new directory
                path = path + "/" + dir_name    # adding the name to the path
                dirs.update({path:0})
    # Do nothing when listing directories available
    elif command[0:3]=="dir":
        pass
    # Get the file size and change directories in which it was found
    else:
        size = int(command[:command.find(" ")]) # Get the size of file
        dir = path 
        for _ in range(path.count("/")):
            dirs[dir]+=size
            dir=dir[:dir.rfind("/")]
total = 0

# spave required - space unused  (total space - space used)
limit = 30000000 - (70000000 - dirs["/home"])
valid_dirs = []

for folder, memory in dirs.items():
    # ! Part 1
    if memory <= 100000:
        total += memory
    
    # ! Part 2
    if limit <= memory:
        valid_dirs.append(memory)

print("Answer to part 1:",total)
print("Answer to part 2:",min(valid_dirs))