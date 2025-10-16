a = [1, 6, 4, 2]

unique_sorted = sorted(set(a), reverse=True)

if len(unique_sorted) >= 2:
    second_max = unique_sorted[1]
    print("Second largest element is:", second_max)
else:
    print("Not enough unique elements to find second maximum.")
