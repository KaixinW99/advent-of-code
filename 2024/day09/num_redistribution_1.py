#
# test the code: python num_redistribution_1.py < input.txt
# check the time: time python num_redistribution_1.py < input.txt

def parse_disk_map(disk_map):
    files, free_spaces = [], []
    is_file = True
    for digit in disk_map:
        length = int(digit)
        if is_file:
            files.append(length)
        else:
            free_spaces.append(length)
        is_file = not is_file
    if len(files)-1 != len(free_spaces): 
        raise ValueError('Invalid disk map: file.size != free_space.size + 1')
    return files, free_spaces

#print(parse_disk_map(open(0).read().strip()))
def compact_files(files, free_spaces):
    disk = []
    file_id = 0

    file_total_length = sum(files)

    for file_length, free_length in zip(files, free_spaces):
        disk.extend([file_id] * file_length)
        disk.extend(['.'] * free_length)
        file_id += 1
    
    if len(files) > len(free_spaces):
        disk.extend([file_id] * files[-1])
    
    # number moving
    while disk.index('.') < file_total_length:
        dot_index = disk.index('.')
        for i in range(len(disk)-1, dot_index, -1):
            if disk[i] != '.':
                disk[dot_index], disk[i] = disk[i], '.'
                break
    return disk

def calculate_checksum(disk):
    checksum = 0
    for position, block in enumerate(disk):
        if block != '.':
            checksum += position * block
    return checksum

def main():
    disk_map = open(0).read().strip()
    files, free_spaces = parse_disk_map(disk_map)
    disk = compact_files(files, free_spaces)
    checksum = calculate_checksum(disk)
    print(checksum)

if __name__ == '__main__':
    main()