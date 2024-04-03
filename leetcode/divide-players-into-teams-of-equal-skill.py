class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        sum = 0
        d = skill[left] + skill[right]
        while(left < right):
            sum += skill[left]*skill[right]
            if d != skill[left] + skill[right]:
                return -1
            d = skill[left] + skill[right]
            right-=1
            left+=1
        return sum

            

        
