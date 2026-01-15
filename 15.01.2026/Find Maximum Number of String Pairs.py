class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        pairs = 0
        reverse_dict = {}

        for word in words:
            reverse_word = word[::-1]
            if reverse_word in reverse_dict:
                pairs += reverse_dict[reverse_word]
                reverse_dict[reverse_word] += 1
            else:
                reverse_dict[word] = 1

        return pairs
