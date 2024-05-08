class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        rank = [""] * len(score)
        tmp = score
        score_to_idx= {}
        for i in range(len(score)):
            score_to_idx[score[i]] = i
        
        tmp.sort(reverse = True)
        
        for i in range(len(score)):
            if i == 0 :
                rank[score_to_idx[tmp[i]]] = "Gold Medal"
            elif i == 1 :
                 rank[score_to_idx[tmp[i]]] = "Silver Medal"
            elif i == 2 :
                 rank[score_to_idx[tmp[i]]] = "Bronze Medal"
            else:
                 rank[score_to_idx[tmp[i]]] = str(i+1)
        
        return rank
        
            
            