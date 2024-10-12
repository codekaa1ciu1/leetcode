from typing import List

# TODO, fuck hahaha, need do again

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        m = sorted(milestones,reverse=True)
        print(f'{m=}')
        wd = 0
        while 1:
            if m[0] == 0:
                m.remove(0)
                m = sorted(m, reverse=True)
                print(f'finish 1 job, resorted{m=}')
            while len(m) >= 1 and m[-1] == 0:
                m.remove(0)
            if len(m) == 0:
                return wd
            if len(m) == 1:
                return wd + 1
            if m[0] < m[1]:
                m = sorted(m, reverse=True)
                print(f'1st job small than 2nd job, resorted{m=}')
            if m[0] >= len(m) - 1:
                print(f'largest {m[0]=} is too big')
                for x in range(1, len(m)):
                    m[x] -= 1
                    wd += 1
                m[0] -= (len(m)-1)
                wd += (len(m)-1)
            else:
                print(f'largest job{m[0]} is not big enough')
                for x in range(1, m[0]+1):
                    m[x] -= 1
                    wd += 1
                wd += m[0]
                m[0] = 0
            print(f'{m=}, {wd=}')


def test_numberOfWeeks():
    solution = Solution()
    test_cases = [
        # ([1, 2, 3], 6),
        # ([5, 2, 1], 7),
        # ([0, 0, 0], 0),
        # ([10, 10, 10], 30),
        # ([1, 1, 1], 3),
        # ([9,3,6,8,2,1], 29),
        # ([3,9,7,1,2,3], 25),
        ([20,33,15,42,18,16,21,12,44,28,42,45,7,7,39,21,22,44], 476)
    ]

    for i, (milestones, expected) in enumerate(test_cases):
        result = solution.numberOfWeeks(milestones)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
    print("All test cases passed!")


if __name__ == "__main__":
    test_numberOfWeeks()

