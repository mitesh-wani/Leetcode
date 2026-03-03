class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count=0
        for pt1 in points:
            for pt2 in points:
                if pt1==pt2:continue
                if (pt1[0] <= pt2[0] and pt1[1] >= pt2[1]):
                    is_valid=True
                    for pt3 in points:
                        if pt1==pt3 or pt2==pt3:continue
                        if (pt1[0]<=pt3[0]<=pt2[0] and pt2[1]<=pt3[1]<=pt1[1]):
                            is_valid=False
                    if is_valid:
                        count+=1
            
        return count
