# for sorted array
def check_sum_to_target(arr, target):
    i, j = 0, len(arr)-1
    while i < j:
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])
            i += 1
            j -= 1
        elif arr[i] + arr[j] > target:
            j -= 1
        else:
            i += 1
