class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}
        # we need a tracking to check this course is already visit or not if we found it in it's neighbor mean it's a loop
        visit = set()

        # Create a map for course 
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Using dfs to check close loop
        def dfs(crs):
            
            # There is no loop for this course
            if preMap[crs] == []:
                return True

            # it already visit, so it's a loop
            if crs in visit:
                return False

            # Add vist
            visit.add(crs)
            # check neighbor
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # Remove from vist
            visit.remove(crs)
            # mark this course as empty list to know it's no loop, so we don't need to check again
            preMap[crs] = []
            
            return True


            
        
        # the idea is we will use dfs to check there is a close loop or not
        for crs in range(numCourses):
            # Check each course as a close loop or not
            if not dfs(crs):
                return False

        return True