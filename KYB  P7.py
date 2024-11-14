class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BSTMap:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
        return node

    def find_min(self):
        if self.is_empty():
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find_max(self):
        if self.is_empty():
            return None
        return self._find_max(self.root)

    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.key, node.value = temp.key, temp.value
            node.right = self._delete(node.right, temp.key)
        return node

    def display(self, msg='BSTMap:', order=1):
        print(msg, end=' ')
        if order == 1:
            self._inorder(self.root)
        elif order == 2:
            self._preorder(self.root)
        elif order == 3:
            self._postorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)

    def _preorder(self, node):
        if node:
            print(node.key, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key, end=' ')

class AVLMap(BSTMap):
    def _height(self, node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = max(self._height(node.left), self._height(node.right)) + 1

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _balance(self, node):
        if self._balance_factor(node) > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        elif self._balance_factor(node) < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        self._update_height(node)
        return node

    def _insert(self, node, key, value):
        node = super()._insert(node, key, value)
        return self._balance(node)

    def _delete(self, node, key):
        node = super()._delete(node, key)
        if node:
            node = self._balance(node)
        return node

if __name__ == "__main__":
    avl_map = AVLMap()
    avl_map.display("[삽입 전] : ")

    while True:
        key = input("삽입할 키 값을 입력하세요 (종료하려면 'q' 입력): ")
        if key.lower() == 'q':
            break
        try:
            key = int(key)
            value = input("해당 키에 대한 값을 입력하세요: ")
            avl_map.insert(key, value)
            avl_map.display(f"[삽입 {key}] : ")
        except ValueError:
            print("잘못된 입력입니다. 숫자 형식의 키를 입력하세요.")

    print('[최대 키] :', avl_map.find_max().key)
    print('[최소 키] :', avl_map.find_min().key)
    
    search_key = input("탐색할 키 값을 입력하세요: ")
    if search_key.isdigit():
        search_key = int(search_key)
        result = avl_map.search(search_key)
        if result:
            print(f'[탐색 {search_key}] : 성공, 값은 "{result.value}"입니다.')
        else:
            print(f'[탐색 {search_key}] : 실패')
    else:
        print("잘못된 입력입니다. 숫자 형식의 키를 입력하세요.")

    delete_key = input("삭제할 키 값을 입력하세요: ")
    if delete_key.isdigit():
        delete_key = int(delete_key)
        avl_map.delete(delete_key)
        avl_map.display(f"[삭제 {delete_key}] : ")
    else:
        print("잘못된 입력입니다. 숫자 형식의 키를 입력하세요.")
