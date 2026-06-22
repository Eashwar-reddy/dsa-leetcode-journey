from collections import defaultdict

class Solution(object):
    def maxNumberOfBalloons(self, text):
        hm = defaultdict(int)

        for i in text:
            hm[i] += 1

        ans = float('inf')

        for i in "balon":
            if i == 'l' or i == 'o':
                temp = hm[i] // 2
            else:
                temp = hm[i]

            ans = min(ans, temp)

        return ans