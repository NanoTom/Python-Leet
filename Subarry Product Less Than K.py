def countSubarrays(nums, k):
    if k <= 1:
        return 0

    count = 0
    product = 1
    left = 0

    for right in range(len(nums)):
        product *= nums[right]
        print(product)

        while product >= k:
            product /= nums[left]
            left += 1

        count += right - left + 1

    return count


# Example usage
nums1 = [10, 5, 2, 6]
k1 = 100
print(countSubarrays(nums1, k1))  # Output: 8

nums2 = [1, 2, 3]
k2 = 0
print(countSubarrays(nums2, k2))  # Output: 0