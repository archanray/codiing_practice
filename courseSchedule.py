class Solution:
    def dfs(self, course, visited):
        """
        cycle detection with topological sort
        """
        if visited[course] == 1:
            return False
        if visited[course] == -1:
            return True
        visited[course] = 1
        for prereq in self.adj[course]:
            if not self.dfs(prereq, visited):
                return False
        visited[course] = -1
        return True
    
    def canFinish(self, numCourses, prereqs):
        self.adj = [[] for _ in range(numCourses)]
        # create adj list of graph
        for course,prereq in prereqs:
            self.adj[course].append(prereq)
        # perform DFS
        visited = [0] * numCourses
        for course in range(numCourses):
            if not self.dfs(course, visited):
                return False
        return True