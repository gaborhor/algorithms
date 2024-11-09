import math
import sys

sys.setrecursionlimit(10**8)
def cPairDist(points):
    print(f"Input list: {points}")
    points.sort()
    print(f"List of points sorted: {points}")

    def recCPairDist(points, low=0, high=None):

        if high==None:
            high = len(points)-1

        if low==high:
            return math.inf

        mid = (low+high)//2

        left_rec = recCPairDist(points, low, mid)
        right_rec = recCPairDist(points, mid+1, high)
        mid_check = (points[mid+1]-points[mid])
        # print(left_rec)
        # print(right_rec)
        # print(mid_check)

        return(min(
                    left_rec,
                    right_rec,
                    mid_check
                   )
               )

    return recCPairDist(points)


list_1 = [7,4,12,14,2,10,16,6]
######## [2,4,6,7,10,12,14,16]

list_2 = [7,4,12,14,2,10,16,5]
######## [2,4,5,7,10,12,14,16]

list_3 = [14,8,2,6,3,10,12]
######## [2,3,6,8,10,12,14]

print(cPairDist(list_1))
print(cPairDist(list_2))
print(cPairDist(list_3))
