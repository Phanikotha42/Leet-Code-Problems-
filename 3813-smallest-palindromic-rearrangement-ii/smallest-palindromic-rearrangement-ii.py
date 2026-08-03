import collections

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s, k):
        count = collections.Counter(s)

        if not self._isPalindromePossible(count):
            return ""

        halfCount, midLetter = self._getHalfCountAndMidLetter(count)

        if k > self._countArrangements(halfCount):
            return ""

        leftHalf = self._generateLeftHalf(halfCount, k)

        return "".join(leftHalf) + midLetter + "".join(reversed(leftHalf))

    def _isPalindromePossible(self, count):
        odd = 0
        for v in count.values():
            if v % 2:
                odd += 1
        return odd <= 1

    def _getHalfCountAndMidLetter(self, count):
        half = [0] * 26
        middle = ""

        for ch, freq in count.items():
            half[ord(ch) - ord("a")] = freq // 2
            if freq % 2:
                middle = ch

        return half, middle

    def _generateLeftHalf(self, halfCount, k):
        length = sum(halfCount)
        left = []

        for _ in range(length):
            for i in range(26):
                if halfCount[i] == 0:
                    continue

                halfCount[i] -= 1
                ways = self._countArrangements(halfCount)

                if ways >= k:
                    left.append(chr(i + ord("a")))
                    break

                k -= ways
                halfCount[i] += 1

        return left

    def _countArrangements(self, count):
        total = sum(count)
        ans = 1

        for freq in count:
            ans *= self._nCk(total, freq)
            if ans >= self.MAX:
                return self.MAX
            total -= freq

        return ans

    def _nCk(self, n, k):
        if k > n:
            return 0

        k = min(k, n - k)
        ans = 1

        for i in range(1, k + 1):
            ans = ans * (n - i + 1) // i
            if ans >= self.MAX:
                return self.MAX

        return ans