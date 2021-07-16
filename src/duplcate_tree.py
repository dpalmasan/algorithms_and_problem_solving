from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List:
        _, hashmap = self.constructMapRecursive(root, {})
        return [list(key) for key, count in hashmap.items() if count > 1]

    def constructMapRecursive(self, node, hashmap: dict):
        if node.left is None and node.right is None:
            subtree = [node.val]
            key = tuple(subtree)
            hashmap[key] = hashmap.get(key, 0) + 1
            return subtree, hashmap

        result = [node.val]
        if node.left is not None:
            subtree_left, hashmap = self.constructMapRecursive(
                node.left, hashmap
            )
            result.extend(subtree_left)

        if node.right is not None:
            subtree_right, hashmap = self.constructMapRecursive(
                node.right, hashmap
            )
            result.extend(subtree_right)
        key = tuple(result)
        hashmap[key] = hashmap.get(key, 0) + 1
        return result, hashmap


class SolutionSubmit:
    # assuming nodes are hashable
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        _, hashmap = self.constructMapRecursive(root, {})
        return [node for node, count in hashmap.items() if count > 1]

    def constructMapRecursive(self, node, hashmap: dict):
        if node.left is None and node.right is None:
            hashmap[node] = hashmap.get(node, 0) + 1
            return node, hashmap

        if node.left is not None:
            subtree_left, hashmap = self.constructMapRecursive(
                node.left, hashmap
            )

        if node.right is not None:
            subtree_right, hashmap = self.constructMapRecursive(
                node.right, hashmap
            )
        hashmap[node] = hashmap.get(node, 0) + 1
        return node, hashmap


def print_tree(root: TreeNode):
    queue = [(root, 0)]

    while queue:
        node, depth = queue.pop()
        print((node.val, depth), end=", ")
        if node.left is not None:
            queue.insert(0, (node.left, depth + 1))
        if node.right is not None:
            queue.insert(0, (node.right, depth + 1))

    print()


# For testing purposes
tree = [1, 2, 3, 4, None, 2, 4, None, None, 4]
# tree = [0,0,0,0,None,None,0,None,None,None,0]
root = TreeNode(tree[0])
queue = [root]
i = 1
while queue:
    node = queue.pop()

    if i < len(tree) and tree[i] is not None:
        node.left = TreeNode(tree[i])

    if i + 1 < len(tree) and tree[i + 1] is not None:
        node.right = TreeNode(tree[i + 1])
    i += 2

    if node.left is not None:
        queue.insert(0, node.left)
    if node.right is not None:
        queue.insert(0, node.right)

print_tree(root)
sol = Solution()
print(sol.findDuplicateSubtrees(root))
