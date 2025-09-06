# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # using dictionary to deal with matching level
        structure = {}
        i = 0
        level = 0
        while i < len(traversal):
            isdigit = traversal[i].isdigit()

            # decipher whether it's dashes or number
            code = ''
            while i < len(traversal) and traversal[i].isdigit() == isdigit:
                code += traversal[i]
                i += 1

            if isdigit:
                node = TreeNode(int(code))
                structure[level] = node
                if level:
                    parent = structure[level - 1]
                    if parent.left:
                        parent.right = node
                    else:
                        parent.left = node
            else:
                level = len(code)
        return structure[0]

        # using stack to deal with matching level
#        stack = []
#        i = 0
#        level = 0
#        while i < len(traversal):
#            isdigit = traversal[i].isdigit()
#
#            # decipher whether it's dashes or number
#            code = ''
#            while i < len(traversal) and traversal[i].isdigit() == isdigit:
#                code += traversal[i]
#                i += 1
#
#            if isdigit:
#                node = TreeNode(int(code))
#                while stack and level <= stack[-1][0]:
#                    stack.pop()
#                if stack:
#                    if stack[-1][1].left:
#                        stack[-1][1].right = node
#                    else:
#                        stack[-1][1].left = node
#                stack.append((level, node))
#            else:
#                level = len(code)
#        return stack[0][1]
