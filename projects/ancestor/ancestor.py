class Queue():
    def __init__(self):
        self.queue = []

    def enqeueu(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):
    q = Queue()

    neighbors = {}

    for node in ancestors:
        if node[1] not in neighbors:
            neighbors[node[1]] = set()

        neighbors[node[1]].add(node[0])

    if starting_node not in neighbors:
        return -1

    else:
        q.enqeueu(neighbors[starting_node])

    while True:
        n = q.dequeue()

        current_node = min(n)

        if current_node in neighbors:
            q.enqeueu(neighbors[current_node])

        else:
            return current_node