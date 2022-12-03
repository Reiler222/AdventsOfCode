calories_file = open("Puzzle1\input.txt", "r")
elven_dictionary = {}
final_calories_sum = 0
elf_count = 1
top_calories = 0

# Read all file lines, adding a new elf when '' is readed
for calories in calories_file.read().split("\n"):
    if calories == '':
        elf_count += 1
        elven_dictionary[elf_count] = 0
        final_calories_sum = 0
        continue
    else:
        final_calories_sum += int(calories)
        
    elven_dictionary[elf_count] = final_calories_sum

calories_file.close()

# Sorting the dict by value for part 2
sorted_elven_dict = sorted(elven_dictionary.items(),key=lambda x:x[1], reverse=True)
count = 1
for elf in sorted_elven_dict:
    if count >= 4:
        break
    else:
        top_calories += elf[1]
        count += 1

print(top_calories)

    