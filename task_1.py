from algorithm import insert, Node


def get_max(node):
    """Знаходить найбільше значення у двійковому дереві"""

    current = node
    while current.right:
        current = current.right
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
    max_value = get_max(root)
    print(f"Найбільше значення: {max_value}")


if __name__ == "__main__":
    main()
