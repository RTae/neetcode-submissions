class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_t = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in map_t:
                if stack and stack[-1] == map_t[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
