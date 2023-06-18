"""
Leetcode 207: Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # form a graph using pre-requisites list
        adjacency_list = [[] for _ in range(numCourses)]
        for (course, pre_req) in prerequisites:
            adjacency_list[pre_req].append(course)

        visited = [-1] * numCourses
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        timestamp = [0]

        def dfs_check_cycle(source) -> bool:
            visited[source] = 1
            # update arrival timestamp
            arrival[source] = timestamp[0]
            timestamp[0] += 1

            for neighbor in adjacency_list[source]:
                if visited[neighbor] == -1:
                    # check if there's a cycle for neighbor successive course
                    if dfs_check_cycle(neighbor):
                        return True
                else: 
                    # back edge
                    if departure[neighbor] == -1:
                        # there's a cycle/loop in the graph detected by presence of back edge
                        return True

            # update departure time
            departure[source] = timestamp[0]
            timestamp[0] += 1
            return False

        for course in range(numCourses):
            if visited[course] == -1:
                if dfs_check_cycle(course):
                    # cycle/loop found, hence there's no way course schedule can be completed, hence return false
                    return False
        return True
