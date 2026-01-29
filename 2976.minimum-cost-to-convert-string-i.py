#
# @lc app=leetcode id=2976 lang=python3
#
# [2976] Minimum Cost to Convert String I
#

# @lc code=start
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        memo = dict()
        graph = dict()

        n = len(original)
        for i in range(n):
            if original[i] not in graph:
                graph[original[i]] = []
            graph[original[i]].append((changed[i], cost[i]))

        def compute_cost(c1, c2):
            if c1 == c2:
                return 0
            if (c1, c2) in memo:
                return memo[(c1, c2)]
            min_cost = float('inf')
            h = []
            heapq.heappush(h, (0, c1))
            visited = set()
            while h:
                curr_cost, curr_char = heapq.heappop(h)
                if curr_char in visited:
                    continue
                visited.add(curr_char)
                if curr_char == c2:
                    min_cost = curr_cost
                    break
                if curr_char in graph:
                    for neighbor, edge_cost in graph[curr_char]:
                        if neighbor not in visited:
                            heapq.heappush(h, (curr_cost + edge_cost, neighbor))
            memo[(c1, c2)] = min_cost
            return min_cost

        ans = 0
        for c1, c2 in zip(source, target):
            cost_to_convert = compute_cost(c1, c2)
            if cost_to_convert == float('inf'):
                return -1
            ans += cost_to_convert
        return ans
# @lc code=end

