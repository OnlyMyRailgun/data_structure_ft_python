# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return "<value: {}>".format(self.value)

    __repr__ = __str__


class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.length = 0

    def append(self, value):
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = Node(value)
        self.length = self.length + 1

    def remove(self, value):
        prevNode = self.head
        currentNode = self.head.next
        while currentNode != None and currentNode.value != value:
            prevNode = currentNode
            currentNode = currentNode.next
        if currentNode != None:
            prevNode.next = currentNode.next
            self.length = self.length - 1
    
    def iter_node(self):
        currentNode = self.head.next
        while currentNode != None:
            yield currentNode
            currentNode = currentNode.next
    
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    
    def __len__(self):
        return self.length


def test_append():
    linkedList = LinkedList()
    linkedList.append(2)
    linkedList.append(1)
    linkedList.append(3)
    linkedList.append(0)

    return linkedList


def test_remove_first_node():
    linkedList = test_append()
    linkedList.remove(2)
    
    assert list(linkedList) == [1, 3, 0]
    return linkedList


def test_remove_last_node():
    linkedList = test_append()
    linkedList.remove(0)
    
    assert list(linkedList) == [2, 1, 3]
    return linkedList


def test_remove_middle_node():
    linkedList = test_append()
    linkedList.remove(3)
    
    assert list(linkedList) == [2, 1, 0]
    return linkedList


def test_remove_non_exist_node():
    linkedList = test_append()
    linkedList.remove(100)
    
    assert list(linkedList) == [2, 1, 3, 0]
    return linkedList


def test_len():
    linkedList = test_append()
    assert len(linkedList) == 4
    linkedList.remove(1)
    assert len(linkedList) == 3
    linkedList.remove(100)
    assert len(linkedList) == 3

    return linkedList


test_append()
test_remove_first_node()
test_remove_last_node()
test_remove_middle_node()
test_remove_non_exist_node()
test_len()
