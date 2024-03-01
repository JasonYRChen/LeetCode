class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        index_n = 0
        for index_t in range(len(typed)):
            if index_n < len(name) and name[index_n] == typed[index_t]:
                index_n += 1
            elif not index_t or typed[index_t] != typed[index_t-1]:
                return False
        return index_n == len(name)
        
"""
        # solution 2
        name_list, typed_list = [[name[0], 0]], [[typed[0], 0]]
        for c in name:
            if c != name_list[-1][0]:
                name_list.append([c, 1])
            else:
                name_list[-1][1] += 1
        for c in typed:
            if c != typed_list[-1][0]:
                typed_list.append([c, 1])
            else:
                typed_list[-1][1] += 1
        while name_list and typed_list:
            c_name, n_name = name_list.pop()
            c_typed, n_typed = typed_list.pop()
            if not (c_name == c_typed and n_name <= n_typed):
                return False
        return False if name_list or typed_list else True

        # solution 1
        name_start, name_stop = 0, 1
        typed_start, typed_stop = 0, 1
        while name_stop <= len(name) or typed_stop <= len(typed):
            while name_stop < len(name) and name[name_stop] == name[name_start]:
                name_stop += 1
            while typed_stop < len(typed) and typed[typed_start] == typed[typed_stop]:
                typed_stop += 1
            if name_start < len(name) and typed_start < len(typed) and name[name_start] == typed[typed_start] and (typed_stop - typed_start) >= (name_stop - name_start):
                name_start, name_stop = name_stop, name_stop + 1
                typed_start, typed_stop = typed_stop, typed_stop + 1
            else:
                return False
        return True
"""
