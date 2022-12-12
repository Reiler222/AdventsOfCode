from string import ascii_letters
backpacks = open("Day 3\input.txt", "r").read().splitlines()
priorities = {v: k for k, v in enumerate(ascii_letters, start=1)}
total = 0


for elf in range(0,len(backpacks), 3):

    first_elf, second_elf, third_elf = backpacks[elf], backpacks[elf + 1], backpacks[elf + 2]
    
    first_elf, second_elf, third_elf = set(first_elf), set(second_elf), set(third_elf)
    
    first_elf = first_elf.intersection(second_elf)
    first_elf = first_elf.intersection(third_elf)

    total += priorities[first_elf.pop()]
    
print(total)
