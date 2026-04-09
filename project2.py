import time

"""
PART B: GREEDY ALGORITHM
Problem: Activity Selection
Selects the maximum number of non-overlapping activities using greedy approach
'activities' parameter is a list of tuples (start_time, finish_time)
The function returns: 'selected' which is list of activities, and 'count' which is the total number of selected activities
"""

def activity_selection(activities):
    sorted_activities = list(activities)   #using insertion sort, make a copy to avoid modifying the original list
    for i in range(1, len(sorted_activities)):
        key = sorted_activities[i]
        j = i - 1
        while j >= 0 and sorted_activities[j][1] > key[1]:  #sort by finish time
            sorted_activities[j + 1] = sorted_activities[j]
            j -= 1
        sorted_activities[j + 1] = key

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
    return max_value, dp


"""
TEST CASES FOR ALL 3 PARTS
"""

def activity_selection_test():
    print("=" * 50)
    print("GREEDY ALGORITHM: Activity Selection")

    print("\nTest Case 1: Small Input")
    activities = [(0, 3), (1, 5), (2, 4), (6, 8)]
    start = time.perf_counter()
    selected, count = activity_selection(activities)
    finish = time.perf_counter()
    print(f"Input: {activities}")
    print(f"Selected Activities: {selected}")
    print(f"Total Count: {count}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


    print("\nTest Case 2: Medium Input")
    activities = [
        (0, 7), (1, 4), (3, 6), (3, 9), 
        (5, 11), (8, 12), (9, 15), (2, 16),
        (12, 17), (17, 24), (10, 18), (7, 23) 
    ]
    start = time.perf_counter()
    selected, count = activity_selection(activities)
    finish = time.perf_counter()
    print(f"Input: {activities}")
    print(f"Selected Activities: {selected}")
    print(f"Total Count: {count}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


    print("\nTest Case 3: Edge Case - Single Activity")
    activities = [(2, 6)]
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



def knapsack_01_test():
    print("=" * 50)
    print("DYNAMIC PROGRAMMING: 0/1 Knapsack")

    print("\nTest Case 1: Small Input")
    weights = [1, 3, 5]
    values = [4, 6, 8]
    capacity = 6
    start = time.perf_counter()
    max_value, dp = knapsack_01(weights, values, capacity)
    finish = time.perf_counter()
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print(f"Max Value: {max_value}")
    print(f"DP Table: {dp}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


    print("\nTest Case 2: Medium Input")
    weights = [1, 2, 3, 8, 7, 4]
    values = [20, 5, 10, 40, 15, 25]
    capacity = 10
    start = time.perf_counter()
    max_value, dp = knapsack_01(weights, values, capacity)
    finish = time.perf_counter()
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print(f"Max Value: {max_value}")
    print(f"DP Table: {dp}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


    print("\nTest Case 3: Edge Case - Zero Capacity")
    weights = [1, 2, 3]
    values = [10, 5, 4]
    capacity = 0
    start = time.perf_counter()
    max_value, dp = knapsack_01(weights, values, capacity)
    finish = time.perf_counter()
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print(f"Max Value: {max_value}")
    print(f"DP Table: {dp}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")


    print("\nTest Case 4: Edge Case - All items are too heavy")
    weights = [5, 6, 7]
    values = [10, 15, 40]
    capacity = 3
    start = time.perf_counter()
    max_value, dp = knapsack_01(weights, values, capacity)
    finish = time.perf_counter()
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print(f"Max Value: {max_value}")
    print(f"DP Table: {dp}")
    print(f"Execution Time: {(finish - start) * 1000:.5f} milliseconds\n")



"""
MAIN
"""
if __name__ == "__main__":
    activity_selection_test()
    knapsack_01_test()

