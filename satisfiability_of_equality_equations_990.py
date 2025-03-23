class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def dfs(pool, key):
            if pool[key] == key:
                return key
            return dfs(pool, pool[key])


        pool = {}
        for equation in equations:
            x, eq, y = equation[0], equation[1:3], equation[3]
            if eq == '==':
                if x not in pool and y not in pool:
                    pool[y] = y
                    pool[x] = y
                elif (x not in pool) ^ (y not in pool):
                    pool[x] = pool[x] if x in pool else dfs(pool, y)
                    pool[y] = pool[y] if y in pool else dfs(pool, x)
                else:
                    pool[dfs(pool, x)] = dfs(pool, y)
        
        for equation in equations:
            x, eq, y = equation[0], equation[1:3], equation[3]
            if eq == '!=':
                if x not in pool:
                    pool[x] = x
                if y not in pool:
                    pool[y] = y
                if dfs(pool, x) == dfs(pool, y):
                    return False
        return True
