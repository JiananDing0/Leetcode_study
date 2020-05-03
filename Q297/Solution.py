# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        result = ''
        # When the queue get all 'null', we quit
        determine = lambda lst: all(x is None for x in lst)
        # Breadth first search
        while determine(queue) is False:
            currNode = queue[0]
            # Remove the first element of the queue
            queue.pop(0)
            # Append value to result list
            if currNode is None:
                result += 'null'
            else:
                result += str(currNode.val)
                # Renew the queue
                queue.append(currNode.left)
                queue.append(currNode.right)
            result += ','
        if result == '':
            return '[' + result + ']'
        return '[' + result[:-1] + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        # Pre-defined functions
        leftNode = lambda i: i * 2 + 1
        rightNode = lambda i: i * 2 + 2
        # Preprocessing the string data into a list of data
        if len(data) == 2:
            return None
        data = data[1:-1]
        dataList = data.split(",")
        # Find the return values
        return self.deserialize_helper(dataList, 0, leftNode, rightNode)
    
    def deserialize_helper(self, data, index, leftNode, rightNode):
        # Depth First Search
        if index >= len(data):
            return None
        newNode = TreeNode(data[index])
        newNode.left = self.deserialize_helper(data, leftNode(index), leftNode, rightNode)
        newNode.right = self.deserialize_helper(data, rightNode(index), leftNode, rightNode)
        return newNode

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
