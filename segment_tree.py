# https://neetcode.io/problems/segmentTree/question

class SegmentTreeNode:
    def __init__(self, total: int, L: int, R: int):
        self.sum = total

        # indices of range covered
        self.L = L
        self.R = R

        # child nodes
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"SegmentTreeNode [{self.L}, {self.R}] sum={self.sum}"
    
    def update(self, index: int, val: int):
        if self.L == self.R:
            self.sum = val
        else:
            M = (self.L + self.R) // 2
            if index > M: # right subtree
                self.right.update(index, val)
            else: # left subtree
                self.left.update(index, val)
            self.sum = self.right.sum + self.left.sum
    
    def query(self, L: int, R: int):
        if self.L == L and self.R == R:
            return self.sum
        M = (self.L + self.R) // 2
        if L > M: # range is in right subtree
            return self.right.query(L, R)
        elif R <= M: # range is in left subtree
            return self.left.query(L, R)
        else: # range overlaps both subtrees
            return self.left.query(L, M) + self.right.query(M+1, R)

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.tree = SegmentTree.build(nums, 0, len(nums)-1) # root node
    
    @staticmethod
    def build(nums: List[int], L: int, R: int):
        if L == R:
            return SegmentTreeNode(nums[L], L, R)
        M = (L+R)//2
        root = SegmentTreeNode(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M+1, R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)
    
    def query(self, L: int, R: int) -> int:
        return self.tree.query(L, R)
