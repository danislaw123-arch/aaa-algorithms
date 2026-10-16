class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if node is None:
        return 0
    else:
        return node.height

def update(node):
    node.height = 1 + max(height(node.left), height(node.right))

def rotate_left(a):
    b = a.right
    a.right = b.left
    b.left = a
    update(a)
    update(b)
    return b

def rotate_right(a):
    b = a.left
    a.left = b.right
    b.right = a
    update(a)
    update(b)
    return b

def balance_factor(node):
    return height(node.right) - height(node.left)

def balance(root):
    update(root)
    bf = balance_factor(root)
    if bf == 2:
        u = root.right
        if balance_factor(u) >= 0:
            return rotate_left(root)
        else:
            root.right = rotate_right(u)
            return rotate_left(root)
    if bf == -2:
        u = root.left
        if balance_factor(u) <= 0:
            return rotate_right(root)
        else:
            root.left = rotate_left(u)
            return rotate_right(root)
    return root

def add(root, X):
    if root is None:
        return Node(X)
    if X == root.key:
        return root
    if X < root.key:
        root.left = add(root.left, X)
    else:
        root.right = add(root.right, X)
    return balance(root)

def find_min(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current

def delete(root, X):
    if root is None:
        return None
    if X < root.key:
        root.left = delete(root.left, X)
        return balance(root)
    if X > root.key:
        root.right = delete(root.right, X)
        return balance(root)

    if root.left is None and root.right is None:
        return None
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left

    succ = find_min(root.right)
    root.key = succ.key
    root.right = delete(root.right, succ.key)
    return balance(root)

def exists(root, X):
    current = root
    while current is not None:
        if X == current.key:
            return 'YES'
        elif current.key < X:
            current = current.right
        else:
            current = current.left
    return 'NO'         

def next(root, X):
    ans = None
    current = root
    while current is not None:
        if current.key == X:
            return X
        if current.key > X:
            ans = current.key
            current = current.left
        else:
            current = current.right
    return ans

def prev(root, X):
    ans = None
    current = root
    while current is not None:
        if current.key == X:
            return X
        if current.key < X:
            ans = current.key
            current = current.right
        else:
            current = current.left
    return ans    

def print_tree(root, A):
    if root is None:
        return
    A.append(root.key)
    print_tree(root.left, A)
    print_tree(root.right, A)


    
Q = int(input())
comands = []
root = None
for _ in range(Q):
    comands.append(input())
for i in range(Q):
    parts = comands[i].split()
    if parts[0] == 'add':
        root = add(root, int(parts[1]))
    elif parts[0] == 'del':
        root = delete(root, int(parts[1]))
    elif parts[0] == 'exists':
        print(exists(root, int(parts[1])))
    elif parts[0] == 'next':
        print(next(root, int(parts[1])))
    elif parts[0] == 'prev':
        print(prev(root, int(parts[1])))
    elif parts[0] == 'root':
        if root is None:
            print('Empty')
        else:
            print(root.key)
    elif parts[0] == 'height':
        print(height(root))
    elif parts[0] == 'print':
        if root is None:
            print('Empty')
        else:
            A = []
            print_tree(root, A)
            print(*A)


