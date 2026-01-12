class Solution(object):
    def pickGifts(self, gifts, k):
        for _ in range(k):
            max_value = 0
            max_index = -1
            for i in range(len(gifts)):
                if gifts[i] > max_value:
                    max_value = gifts[i]
                    max_index = i
            gifts[max_index] = int(max_value ** 0.5)
        return sum(gifts)
