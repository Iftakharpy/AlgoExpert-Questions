# time O(nlogn) 
# space O(1)
def nonConstructibleChange(coins):
    coins.sort()
    
    min_sum = 0
    for coin in coins:
        potential_min_sum = min_sum + 1
        if coin > potential_min_sum:
            return potential_min_sum
        
        min_sum += coin
    
    return min_sum + 1
