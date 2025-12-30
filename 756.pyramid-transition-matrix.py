#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#

# @lc code=start
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        nxt = defaultdict(list)
        for rule in allowed:
            a, b, c = rule[0], rule[1], rule[2]
            nxt[(a, b)].append(c)

        @lru_cache(None)
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True


            candidates = []

            def build_next(i: int):
                if i == len(row) - 1:
                    next_row = "".join(candidates)
                    return dfs(next_row)

                pair = (row[i], row[i + 1])
                if pair not in nxt:
                    return False 

                for top in nxt[pair]:
                    candidates.append(top)
                    if build_next(i + 1):
                        return True
                    candidates.pop()

                return False

            return build_next(0)

        return dfs(bottom)
        
# @lc code=end

