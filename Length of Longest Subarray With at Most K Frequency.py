def maxSubarrayLength(nums,k):
    start = 0
    max_length = 0
    freq_map = {}

    for end in range(len(nums)):
        num = nums[end]
        freq_map[num] = freq_map.get(num, 0) + 1

        while any(freq > k for freq in freq_map.values()):
            left_num = nums[start]
            freq_map[left_num] -= 1
            if freq_map[left_num] == 0:
                del freq_map[left_num]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

## study this code for  2958

