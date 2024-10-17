class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = {'a': a, 'b': b, 'c': c}
        result = []

        while True:
            max_char = max(counts, key=counts.get)
            if len(result) >= 2 and result[-1] == result[-2] == max_char:
                second_char = max([char for char in counts if char != max_char], key=counts.get)
                if counts[second_char] == 0:
                    break
                result.append(second_char)
                counts[second_char] -= 1
            else:
                if counts[max_char] == 0:
                    break
                result.append(max_char)
                counts[max_char] -= 1

        return ''.join(result)


