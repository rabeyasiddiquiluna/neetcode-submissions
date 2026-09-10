class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] *  numCourses
        adj = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            indegree[course] += 1
            adj[pre].append(course)

        q = deque()
        finish = 0

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses



        