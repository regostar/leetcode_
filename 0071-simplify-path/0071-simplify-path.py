class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for portion in path.split('/'):
            #  process each portion one by one
            if portion == '..':
                # go back one step
                if stack:
                    stack.pop()
            elif not portion or portion == '.':
                # do nothing
                continue
            else:
                # add to stack this is a path or directory name
                stack.append(portion)
        final_str = '/' + '/'.join(stack)
        return final_str
