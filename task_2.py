from algorithm import insert, Node


def get_min(node):
    """Знаходить найменше значення у двійковому дереві"""

    current = node
    while current.left:
        current = current.left
    return current.data if current else 0


def main():
    root = Node(7)
    root = insert(root, 4)
    root = insert(root, 2)
    root = insert(root, 5)
    root = insert(root, 8)
    root = insert(root, 7)
    root = insert(root, 9)

    print(root)
    min_value = get_min(root)
    print(f"Найменше значення: {min_value}")


if __name__ == "__main__":
    main()
