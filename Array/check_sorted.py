def check_sorted_arr(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i+1]:
            print("Unsorted")
            return
        i += 1
    print("Sorted")
