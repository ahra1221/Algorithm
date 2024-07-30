class Solution(object):
    def findRelativeRanks(self, score):
        answer = [ 0 for i in range(len(score))]
        sorted_score = sorted(score)
        rank = len(score)
        for i in sorted_score:
            idx = score.index(i)
            if rank == 1:
                answer[idx] = "Gold Medal"
            elif rank == 2:
                answer[idx ] = "Silver Medal"
            elif rank == 3:
                answer[idx] = "Bronze Medal"
            else:
                answer[idx] = str(rank)
            rank -= 1
        return answer
        
