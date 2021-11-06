# time O(nlogn)
# space O(1)
def minimumWaitingTime(queries):
    queries.sort()
    
    total = 0
    prev_sum = 0
    for i in queries[:-1]:
        prev_sum += i
        total += prev_sum
    
    return total

# time O(nlogn)
# space O(1)
def minimumWaitingTime(queries):
    queries.sort()
    
    total = 0
    for idx, wait_time in enumerate(queries, start=1):
        queries_left = len(queries) - idx
        total += queries_left * wait_time
        
    return total
