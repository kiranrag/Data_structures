class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as a parameter and appends it to the list and returns nothing.

        The runtime for this method is O(1), or constant time, because appending to the end of a list happens in constant time"""
        self.items.append(item)

    def pop(self):
        """this method removes and returns the last item of the list, which is also the top item of the stack

        The runtime here is a constant time, because all it does is index to the last item of list"""
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """This method returns the last item in the list which is also the top item of the stack

        This method runs in constant time because indexing in list is done in constant time"""
        if self.items:
            return self.items[-1]
        return None
    def size(self):
        """This method returns the length of list i.e the stack

        This method runs in constant time because finding the length of list also happens in constant time"""

        return len(self.items)

    def is_empty(self):

        """This method returns a boolean value. It returns true is list is empty

        Testing for equality happens in constant time"""
        return self.items == []

