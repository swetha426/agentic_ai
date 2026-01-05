class TaskNode:
    def __init__(self, name, action):
        self.name = name
        self.action = action
        self.next_nodes = []

    def next(self, node):
        self.next_nodes.append(node)
        return node


class TaskFlow:
    def __init__(self, start_node):
        self.start_node = start_node
