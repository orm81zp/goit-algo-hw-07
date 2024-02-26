"""Модуль реалізації базового класу двійкового дерева пошуку"""


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Корінь - "):
        ret = "\t" * level + prefix + str(self.data) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "Ліве  -- ")
        if self.right:
            ret += self.right.__str__(level + 1, "Праве -- ")
        return ret


def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.data:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root


def search(root, value):
    if root is None or root.data == value:
        return root
    if value < root.data:
        return search(root.left, value)
    return search(root.right, value)
