class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G, indegree, q, ans = defaultdict(list), [0] * numCourses, deque(), []
        for nxt, pre in prerequisites:
            G[pre].append(nxt)
            indegree[nxt] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            ans.append(cur)
            for nextCourse in G[cur]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    q.append(nextCourse)

        return ans if len(ans) == numCourses else []
        