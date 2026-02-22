def count_frequency(arr):
    freq = {}
    for ele in arr:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1
    return freq
