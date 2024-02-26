from algorithm import insert, Node


def get_sum(node):
    """Знаходить суму всіх значень у двійковому дереві"""
    if not node:
        return 0

    result = node.data
    result += get_sum(node.left)
    result += get_sum(node.right)

    return result


def main():
    root = Node(7)
    root = insert(root, 4)
    root = insert(root, 2)
    root = insert(root, 5)
    root = insert(root, 8)
    root = insert(root, 7)
    root = insert(root, 9)

    print(root)
    sum_all = get_sum(root)
    print(f"Сума всіх значень: {sum_all}")


if __name__ == "__main__":
    main()
