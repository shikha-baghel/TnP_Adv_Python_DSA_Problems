def find_missing_num(arr):
    n = max(arr)
    arr_sum = sum(arr)
    total_sum = n * (n+1) // 2
    missing_num = total_sum - arr_sum
    return missing_num
print(find_missing_num(lst3))
