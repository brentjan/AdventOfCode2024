def compact(disk):
    left = 0
    right = len(disk) - 1

    while right > 0:
        while disk[right][0] == '.':
            right -= 1
        while left < right and (disk[left][0] != '.' or disk[left][1] < disk[right][1]):
            left += 1

        if left < right:
            # Swap
            remaining_space = disk[left][1] - disk[right][1]
            if remaining_space > 0:
                disk = disk[:left+1] + [('.', remaining_space)] + disk[left+1:] # Insert remaining space
                right += 1 # Array got shifted

            disk[left], disk[right] = disk[right], (disk[left][0], disk[left][1] - remaining_space if remaining_space > 0 else disk[left][1])

        left = 0 # O(n²)
        right -= 1

    # Determine checksum
    i, factor, checksum = 0, 0, 0
    while i < len(disk):
        block_index, size = disk[i]
        block_value = int(block_index) if block_index != '.' else 0
        
        for _ in range(size):
            checksum += factor * block_value
            factor += 1
        i += 1

    return disk, checksum


if __name__ == '__main__':
    disk = []
    
    with open("data/advent9.in") as file:
        full = True
        i = 0
        for line in file:
            for file_block in line.rstrip():
                file_block = int(file_block)
                disk.append((str(i) if full else '.', file_block))
                full = not full
                i += 1 if full else 0

    disk, checksum = compact(disk)
    print(checksum)
