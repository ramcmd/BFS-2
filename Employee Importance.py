# TC: O(n) where n is the len(employees)
# SC: O(n) where n is the size of the hashmap, + O(n) for the size of the queue 
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id_: int) -> int:
        
        hashmap = {}
        
        for employee in employees:
            if employee.id not in hashmap:
                hashmap[employee.id] = [employee.importance, employee.subordinates]
        
        q = deque()
        total_imp = 0
        
        q.append(id_)
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                total_imp += hashmap[node][0]
                for i in range(len(hashmap[node][1])):
                    q.append(hashmap[node][1][i])
            
        return total_imp
        
        
        
        
        