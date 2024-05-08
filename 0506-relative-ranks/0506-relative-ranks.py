class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        tmp = [0]*len(score)
        ranks =  ["Gold Medal","Silver Medal","Bronze Medal"]
        for i in range(len(score)):
            current_max = max(score)
            print(current_max)
            print(score.index(current_max))
            if i<3:
                tmp[score.index(current_max)]= ranks[0]
                score[score.index(current_max)] = -1
                ranks.pop(0)
            else :
                tmp[score.index(current_max)] = str(i+1)
                score[score.index(current_max)] = -1
                
                
        return tmp