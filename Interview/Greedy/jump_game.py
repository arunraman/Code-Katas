class Solution():

    def jump_game_1(self, A):
        reachable = 0
        for i, length in enumerate(A):
            if i > reachable:
                break
            reachable = max(reachable, i + length)
        return reachable >= len(A) - 1

    def jump_game_2(self, A):
        last, curr, steps = 0, 0, 0
        for i, ei in enumerate(A):
            if i > last:
                last = curr
                steps += 1
            curr = max(curr, i + ei)
        return steps


S = Solution()
print S.jump_game_1([2,3,1,1,4])
print S.jump_game_1([3,2,1,0,4])

print S.jump_game_2([2,3,1,1,4])

