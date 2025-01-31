from math import isqrt

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for i in range k:
            m = max(gifts, key=max)
            gifts[gifts.index(m)] = isqrt(gifts[gifts.index(m)])

        return sum(gifts)