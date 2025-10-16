arr = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3

sorted_arr = sorted(arr)
nth_min = sorted_arr[N - 1]
mth_max = sorted_arr[-M]

total = mth_max + nth_min
difference = mth_max - nth_min

print(f"{M}st Maximum Number =", mth_max)
print(f"{N}rd Minimum Number =", nth_min)
print("Sum =", total)
print("Difference =", difference)
