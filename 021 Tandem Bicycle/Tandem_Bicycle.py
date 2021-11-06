# time O(nlogn)
# space O(1)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    
    total = 0
    for pair in zip(redShirtSpeeds, blueShirtSpeeds):
        total+=max(pair)
    return total
