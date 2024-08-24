class Node:
    def __init__(self, value):
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
        self.val = value  # 노드의 값

def inorder_traversal(root):
    global s
    if root:  # 노드가 None이 아니면
        inorder_traversal(root.left)  # 왼쪽 서브트리 방문
        print(root.val, end='')  # 현재 노드 방문
        s += root.val
        inorder_traversal(root.right)  # 오른쪽 서브트리 방문

for test_case in range(1, 11):
    n = int(input())
    tree = {}
    nodes = {}

    for inp in range(n):
        input_ = list(map(str, input().split()))  # 노드번호 / value / left child / right child
        node_num = input_[0]
        value = input_[1]
        left = input_[2] if len(input_) > 2 else None
        right = input_[3] if len(input_) > 3 else None
        
        
        if node_num not in nodes:
            nodes[node_num] = Node(value)
        else:
            nodes[node_num].val = value
        
        if left and left != '.':
            if left not in nodes:
                nodes[left] = Node(None)
            nodes[node_num].left = nodes[left]
        
        if right and right != '.':
            if right not in nodes:
                nodes[right] = Node(None)
            nodes[node_num].right = nodes[right]
            
            
    root = nodes['1']  # 루트 노드는 항상 '1'
    
    
    print(f"#{test_case}", end=' ')
    s = ""
    inorder_traversal(root)
    print('')  # 줄 바꿈