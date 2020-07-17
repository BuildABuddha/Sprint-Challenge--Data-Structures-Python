class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        temp_list = []
        current_node = self.head
        while current_node:
            temp_list.append(current_node.value)
            current_node = current_node.next_node

        return "[" + ", ".join([str(i) for i in temp_list]) + "]"

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # If node is none, then we're at the end and should make the previous one the head.
        if node is None:
            self.head = prev
        else:
            # Keep next node in mind so we can fix it after this.
            next_node = node.next_node

            # Swap its pointers around
            node.next_node = prev

            # Move onto next node, using the current node as the previous!
            self.reverse_list(next_node, node)
