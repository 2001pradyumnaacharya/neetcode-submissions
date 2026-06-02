class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 1
        a = 1
        ind = 0

        if len(chars) == 1:
            return 1

        while i < len(chars):
            if j == len(chars):
                chars[ind] = chars[i]
                ind += 1

                if a > 1:
                    for digit in str(a):
                        chars[ind] = digit
                        ind += 1
                print(chars)
                break

            if chars[i] != chars[j]:
                chars[ind] = chars[i]
                ind += 1

                if a > 1:
                    for digit in str(a):
                        chars[ind] = digit
                        ind += 1

                i = j
                j = i + 1
                a = 1
            else:
                j += 1
                a += 1

        return ind