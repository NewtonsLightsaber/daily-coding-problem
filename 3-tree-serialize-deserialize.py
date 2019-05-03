import ast

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    vals = []

    def _serialize(node):
        if node:
            vals.append(str(node.val))
            _serialize(node.left)
            _serialize(node.right)
        else:
            vals.append('#')

    _serialize(root)
    return ' '.join(vals)

def deserialize(s):

    def _deserialize(vals):
        val = next(vals)

        if val == '#':
            return None

        node = Node(
            val=val,
            left=_deserialize(vals),
            right=_deserialize(vals)
        )
        return node

    vals = iter(s.split())
    return _deserialize(vals)

node = Node(
    'root',
    Node('left', Node('left.left')),
    Node('right')
)

print(serialize(node))

assert deserialize(serialize(node)).left.left.val == 'left.left'