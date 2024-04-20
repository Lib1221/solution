class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left, right = 0, len(people)-1
        res = 0
        while left<=right:
            remain = limit-people[right]
            right-=1
            res+=1
            if remain >= people[left]:
                left+=1
        return res
        
