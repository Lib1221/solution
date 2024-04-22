class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        t = 0
        y = 0
        count = 0
        for i in range(len(trainers)):
            if t < len(players) and players[t] <= trainers[y]:
                t+=1
                count+=1
            y+=1
        return count
        
            
        
