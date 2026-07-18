class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        visiting = set()

        # Create a graph
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        

        # Using dfs to check there is a close loop or not
        def dfs(crs):
            # this course already visit mean we found a loop
            if crs in visiting:
                return False
            # This mean this there is no pre-requisites for this course 
            if preMap[crs] == []:
                return True
            
            # Mark as vist first
            visiting.add(crs)
            # Check a pre course in this course
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # mean this course has no loop
            visiting.remove(crs)
            # clear it, so no need to process it again
            preMap[crs] = []

            return True

        # Check all the course
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True