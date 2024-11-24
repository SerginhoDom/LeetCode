class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        n -= 10
        if n == 0:
            return True

        toremove = 9
        alice = False

        while n >= 0:
            if toremove > n and alice:
                return False
            if toremove > n and not alice:
                return True

            n -= toremove
            toremove -= 1
            alice = not alice