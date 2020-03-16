

def maxSum(arr, windowSize):
    arraySize = len(arr)
    # n must be greater than k
    if arraySize <= windowSize:
        print("Invalid operation")
        return -1

    # Compute sum of first window of size k
    window_sum = sum([arr[i] for i in range(windowSize)])
    max_sum = window_sum
    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    for i in range(arraySize-windowSize):
        window_sum = window_sum - arr[i] + arr[i + windowSize]
        max_sum = max(window_sum, max_sum)

    return max_sum


arr = [1, 2, 100, -1, 5]
# maximum sum should be 104 => 100 + -1 + 5
answer = maxSum(arr, 3)
print(answer)
