distances_input = open("input.txt", "r")
total_distance = 0
total_similarity = 0
similarity = 0
left_distances = []
right_distances = []

for distance in distances_input.read().split("\n"):
    
    if distance == "":
        break

    distance = distance.split("   ")
    left_distances.append(distance[0])
    right_distances.append(distance[1])
    
distances_input.close()

left_distances.sort()
right_distances.sort()

for distance_left, distance_right in zip(left_distances, right_distances):
    total_distance += abs(int(distance_left) - int(distance_right))
    
print (f"Total distance: {total_distance}")

# --------- Part two --------- #

for distance_left in left_distances:
    for distance_right in right_distances:
        if int(distance_left) == int(distance_right):
            similarity += 1

    total_similarity += similarity * int(distance_left)
    similarity = 0

    
print(f"Total similarity: {total_similarity}")