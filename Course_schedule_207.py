from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        mapping = defaultdict(list)
        for course1, course2 in prerequisites:
            if course1 == course2:
                return False
            
            if course1 in mapping or course2 not in mapping:
                mapping[course1].append(course2)
            else:
                try:
                    course1_exist = mapping[course2].index(course1)
                except:
                    mapping[course1] = mapping[course2]
                else:
                    return False
        return True


if __name__ == '__main__':
    n = 20
    p = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    print(Solution().canFinish(n, p))

