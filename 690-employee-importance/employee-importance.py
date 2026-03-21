"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        queue = deque()
        graph = {employ.id : employ for employ in employees}

        queue.append(id)

        while queue:
            emp = queue.popleft()
            res+=graph[emp].importance

            for employee in graph[emp].subordinates:
                queue.append(employee)
        return res
        