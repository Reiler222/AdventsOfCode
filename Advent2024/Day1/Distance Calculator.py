distances_input = open("input.txt", "r")
total_distance = 0
left_distances = []
right_distances = []

for distance in distances_input.read().split("\n"):
    
    if distance == "":
        break

    distance = distance.split("   ")
    left_distances.append(distance[0])
    right_distances.append(distance[1])

left_distances.sort()
right_distances.sort()

for distance_left, distance_right in zip(left_distances, right_distances):
    total_distance += abs(int(distance_left) - int(distance_right))
    
print (total_distance)