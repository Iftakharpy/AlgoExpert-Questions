# time O(nlogn)
# space O(1)
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if redShirtHeights[-1]>blueShirtHeights[-1]:
        redShirtHeights, blueShirtHeights = blueShirtHeights, redShirtHeights
    
    for red, blue in zip(redShirtHeights, blueShirtHeights):
        if not red<blue:
            return False
    return True
