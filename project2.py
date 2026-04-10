import time
import random

"""
PART A: DIVIDE & CONQUER (D&C) 
Problem: Merge Sort
Sorts an array by recursively splitting it into halves and merging them in order
'arr' parameter is the unsorted list of elements provided for sorting 
The function returns: 'sorted_arr' which is the resulting sorted array
Requirement: Implementation must be from scratch without using built-in sort functions 
"""

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])   #recursively sort left half
    right_half = mergeSort(arr[mid:])   #recursively sort right half

    return merge(left_half, right_half)  #merge sorted halves

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:   #compare elements from both halves
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])   #append remaining elements from left half
    sorted_arr.extend(right[j:])  #append remaining elements from right half

    return sorted_arr

"""
PART B: GREEDY ALGORITHM
Problem: Activity Selection
Selects the maximum number of non-overlapping activities using greedy approach
'activities' parameter is a list of tuples (start_time, finish_time)
The function returns: 'selected' which is list of activities, and 'count' which is the total number of selected activities
"""

def activity_selection(activities):
    sorted_activities = sorted(activities, key=lambda x: x[1])  #sort by finish time

    selected = []

    selected.append(sorted_activities[0])  #select the first activity
    last_finish_time = sorted_activities[0][1]

    # greedy selection
    for i in range(1, len(sorted_activities)):
        start, finish = sorted_activities[i]
        if start >= last_finish_time:  #activity is compatible if its start time >= last selected finish time
            selected.append(sorted_activities[i])
            last_finish_time = finish

    return selected, len(selected)


"""
PART C: DYNAMIC PROGRAMMING
Problem: 0/1 Knapsack
Solve the 0/1 Knapsack problem using a 2D dynamic programming table
'weights' is the list of item weights
'values' is the list of item values
'capacity' is the maximum weight capacity of the knapsack
The function returns: 'max_value' which is the maximum value that can be obtained, and 'dp' the full DP table
"""

def knapsack_01(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]  #initialize 2D DP table with zeros

    for i in range(1, n + 1):           #fill the DP table
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]     #items not included
            
            if weights[i - 1] <= w:     #items included
                include_value = dp[i - 1][w - weights[i - 1]] + values[i - 1]

                if include_value > dp[i][w]:    #take the better option
                    dp[i][w] = include_value

    max_value = dp[n][capacity]
    return max_value

"""
TEST CASES FOR PART A: DIVIDE & CONQUER
"""
def merge_sort_test():
    print("=" * 50)
    print("DIVIDE & CONQUER: Merge Sort")

    print("\nTest Case 1: Small Input (n = 10)")
    arr = [38, 27, 43, 3, 9, 82, 10, 5, 12, 15]
    start = time.perf_counter()
    sorted_arr = mergeSort(arr)
    finish = time.perf_counter()
    print(f"Input: {arr}")
    print(f"Sorted Output: {sorted_arr}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")

    print("\nTest Case 2: Medium Input (n = 100)")
    arr = [random.randint(1, 100) for _ in range(100)]
    start = time.perf_counter()
    sorted_arr = mergeSort(arr)
    finish = time.perf_counter()
    print(f"Input: {arr}")
    print(f"Sorted Output: {sorted_arr}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")

    print("\nTest Case 3: Large Input (n = 1000)")
    arr = [random.randint(1, 1000) for _ in range(1000)]
    start = time.perf_counter()
    sorted_arr = mergeSort(arr)
    finish = time.perf_counter()
    print(f"Input: {arr}")
    print(f"Sorted Output: {sorted_arr}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")

    print("\nTest Case 4: Edge Case - Already Sorted")
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start = time.perf_counter()
    sorted_arr = mergeSort(arr)
    finish = time.perf_counter()
    print(f"Input: {arr}")
    print(f"Sorted Output: {sorted_arr}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")

    print("\nTest Case 5: Edge Case - Reverse Sorted")
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    start = time.perf_counter()
    sorted_arr = mergeSort(arr)
    finish = time.perf_counter()
    print(f"Input: {arr}")
    print(f"Sorted Output: {sorted_arr}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")

    print("\nTest Case 6: Edge Case - Single Element") 
    arr = [5]
    start = time.perf_counter()
    sorted_arr = mergeSort(arr)
    finish = time.perf_counter()
    print(f"Input: {arr}")
    print(f"Sorted Output: {sorted_arr}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")

"""
TEST CASES FOR PART B: GREEDY ALGORITHM
"""

def activity_selection_test():
    print("=" * 50)
    print("GREEDY ALGORITHM: Activity Selection")

    print("\nTest Case 1: Small Input (n = 10)")
    activities = [(0, 3), (1, 5), (2, 4), (6, 8), (5, 7), (8, 10), (11, 17), (3, 4), (7, 9), (9, 11)]
    start = time.perf_counter()
    selected, count = activity_selection(activities)
    finish = time.perf_counter()
    print(f"Input: {activities}")
    print(f"Selected Activities: {selected}")
    print(f"Total Count: {count}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


    print("\nTest Case 2: Medium Input (n = 100)")
    acts = [(random.randint(0, 200), random.randint(0, 200)) for _ in range(100)]
    activities = [(min(s, f), max(s, f)) for s, f in acts]
    start = time.perf_counter()
    selected, count = activity_selection(activities)
    finish = time.perf_counter()
    print(f"Input: {activities}")
    print(f"Selected Activities: {selected}")
    print(f"Total Count: {count}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


    print("\nTest Case 3: Large Input (n = 1000)")
    acts = [(random.randint(0, 2000), random.randint(0, 2000)) for _ in range(1000)]
    activities = [(min(s, f), max(s, f)) for s, f in acts]
    start = time.perf_counter()
    selected, count = activity_selection(activities)
    finish = time.perf_counter()
    print(f"Input: {activities}")
    print(f"Selected Activities: {selected}")
    print(f"Total Count: {count}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")



    print("\nTest Case 4: Edge Case - All activities overlap")
    activities = [(1, 10), (2, 9), (3, 8), (4, 7)]
    start = time.perf_counter()
    selected, count = activity_selection(activities)
    finish = time.perf_counter()
    print(f"Input: {activities}")
    print(f"Selected Activities: {selected}")
    print(f"Total Count: {count}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


"""
TEST CASES FOR PART C: DYNAMIC PROGRAMMING
"""

def knapsack_01_test():
    print("=" * 50)
    print("DYNAMIC PROGRAMMING: 0/1 Knapsack")

    print("\nTest Case 1: Small Input (n = 10)")
    weights = [1, 3, 5, 2, 8, 10, 6, 7, 9, 4]
    values = [4, 6, 8, 3, 7, 9, 5, 2, 1, 10]
    capacity = 17
    start = time.perf_counter()
    max_value = knapsack_01(weights, values, capacity)
    finish = time.perf_counter()
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print(f"Max Value: {max_value}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


    print("\nTest Case 2: Medium Input (n = 100)")
    weights  = [random.randint(1, 20) for _ in range(100)]
    values   = [random.randint(1, 100) for _ in range(100)]
    capacity = 500
    start = time.perf_counter()
    max_value = knapsack_01(weights, values, capacity)
    finish = time.perf_counter()
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print(f"Max Value: {max_value}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


    print("\nTest Case 3: Large Input (n = 1000)")
    weights  = [random.randint(1, 20) for _ in range(1000)]
    values   = [random.randint(1, 100) for _ in range(1000)]
    capacity = 4500
    start = time.perf_counter()
    max_value = knapsack_01(weights, values, capacity)
    finish = time.perf_counter()
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print(f"Max Value: {max_value}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


    print("\nTest Case 4: Edge Case - All items are too heavy")
    weights = [5, 6, 7]
    values = [10, 15, 40]
    capacity = 3
    start = time.perf_counter()
    max_value = knapsack_01(weights, values, capacity)
    finish = time.perf_counter()
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print(f"Max Value: {max_value}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")



"""
MAIN
"""
if __name__ == "__main__":
    merge_sort_test()
    activity_selection_test()
    knapsack_01_test()

