# 이진탐색트리를 위한 노드 클래스
class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

# 이진탐색트리의 탐색 연산
def search_bst(n, key):
    if n is None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

# 이진탐색트리의 값을 이용한 탐색 연산
def search_value_bst(n, value):
    if n is None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    return search_value_bst(n.right, value)

# 최대와 최소 키를 가지는 노드 탐색 연산
def search_max_bst(n):
    while n is not None and n.right is not None:
        n = n.right
    return n

def search_min_bst(n):
    while n is not None and n.left is not None:
        n = n.left
    return n

# 이진탐색트리의 삽입 연산
def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False

# 이진탐색트리의 삭제 연산
def delete_bst(root, key):
    def delete_bst_case1(parent, node, root):
        if parent is None:
            return None
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
        return root

    def delete_bst_case2(parent, node, root):
        child = node.left if node.left is not None else node.right
        if node == root:
            return child
        if node == parent.left:
            parent.left = child
        else:
            parent.right = child
        return root

    def delete_bst_case3(parent, node, root):
        succp = node
        succ = node.right
        while succ.left is not None:
            succp = succ
            succ = succ.left
        if succp.left == succ:
            succp.left = succ.right
        else:
            succp.right = succ.right
        node.key, node.value = succ.key, succ.value
        return root

    parent, node = None, root
    while node is not None and node.key != key:
        parent = node
        node = node.left if key < node.key else node.right
    if node is None:
        return root

    if node.left is None and node.right is None:
        return delete_bst_case1(parent, node, root)
    elif node.left is None or node.right is None:
        return delete_bst_case2(parent, node, root)
    else:
        return delete_bst_case3(parent, node, root)

# 이진탐색트리를 이용한 맵 클래스
class BSTMap:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def search(self, key):
        return search_bst(self.root, key)

    def searchValue(self, value):
        return search_value_bst(self.root, value)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg='BSTMap:', order=1):
        print(msg, end=' ')
        if order == 1:
            self.inorder(self.root)
        elif order == 2:
            self.preorder(self.root)
        elif order == 3:
            self.postorder(self.root)
        print()

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f'{node.key}: {node.value}', end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(f'{node.key}: {node.value}', end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(f'{node.key}: {node.value}', end=' ')


# 테스트 프로그램
if __name__ == "__main__":
    map = BSTMap()

    # 데이터 입력
    n = int(input("삽입 데이터 개수: "))
    for _ in range(n):
        key = int(input("key 값 입력 (예: 35): "))
        value = input("value를 입력하세요: ")
        map.insert(key, value)

    print('[최대 키]:', map.findMax().key)
    print('[최소 키]:', map.findMin().key)

    search_key = int(input("검색할 key 값 (예: 35): "))
    found = map.search(search_key)
    if found:
        print(f"[탐색 결과]: 찾음 ({found.key}: {found.value})")
    else:
        print("[탐색 결과]: 없음")

    # 순회 방식 선택
    while True:
        order = int(input("순회 방식 선택 (1: inorder, 2: preorder, 3: postorder): "))
        if order in (1, 2, 3):
            map.display("트리 순회 결과:", order=order)
            break
        else:
            print("잘못된 입력입니다. 1, 2 또는 3 중에서 선택해주세요.")
