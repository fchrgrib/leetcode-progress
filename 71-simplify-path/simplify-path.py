class Solution:
    def simplifyPath(self, path: str) -> str:
        if path[0] != "/":
            path = "/"+path
        stack = []
        stack_path = []

        for i in range(len(path)):
            if path[i] == "/":
                if len(stack) != 0:
                    tmp = stack.pop()
                    str_m = path[tmp+1:i]

                    if str_m == "..":
                        if len(stack_path) != 0:
                            stack_path.pop()
                        stack.append(i)
                        continue
                    elif str_m == "" or str_m == ".":
                        stack.append(i)
                        continue
                    stack_path.append(str_m)
                stack.append(i)
        if path[-1] != "/":
            if len(stack) != 0:
                    tmp = stack.pop()
                    str_m = path[tmp+1:]

                    if str_m == "..":
                        if len(stack_path) != 0:
                            stack_path.pop()
                    if not (str_m == "" or str_m == ".") and not str_m == "..":
                        stack_path.append(str_m)
        return "/"+"/".join(stack_path)
        