"""
Leetcode 210: Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # form a graph using pre-requisites list
        adjacency_list = [[] for _ in range(numCourses)]
        for (course, pre_req) in prerequisites:
            adjacency_list[pre_req].append(course)

        visited = [-1] * numCourses
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        timestamp = [0]

        def dfs_check_cycle(source, topsort) -> bool:
            visited[source] = 1
            # update arrival timestamp
            arrival[source] = timestamp[0]
            timestamp[0] += 1

            for neighbor in adjacency_list[source]:
                if visited[neighbor] == -1:
                    # check if there's a cycle for neighbor successive course
                    if dfs_check_cycle(neighbor, topsort):
                        return True
                else:
                    # back edge
                    if departure[neighbor] == -1:
                        # there's a cycle/loop in the graph detected by presence of back edge
                        return True

            # update departure time
            departure[source] = timestamp[0]
            timestamp[0] += 1

            # append source to the topsort when departing from it 
            topsort.append(source)
            return False

        topsort = []
        for course in range(numCourses):
            if visited[course] == -1:
                if dfs_check_cycle(course, topsort):
                    # cycle/loop found, hence there's no way course schedule can be completed, hence return []
                    return []
        # reverse the topsort[] to sort the ouput array in topological order
        topsort.reverse()
        return topsort
