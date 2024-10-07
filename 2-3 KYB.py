class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]

    def __str__(self):
        return str(self.array[0:self.top + 1][::-1])

    def size(self):
        return self.top + 1


map = [
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '0', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '0', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '1', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '0', '0', '0', '0', '1', '0', 'x'],
    ['1', '1', '1', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]

MAZE_SIZE = 10

def isValidPos(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def DFS():
    print('DFS: ')
    stack = ArrayStack(100)  
    stack.push((0, 1))        
    distance = 0              

    while not stack.isEmpty():  
        here = stack.pop()      
        print(f'현위치: {here}', end=' -> ')
        (x, y) = here

        if map[y][x] == 'x':    
            print(f'\n출구 발견  이동 거리 = {distance}')
            return True
        else:
            map[y][x] = '.'      
            distance += 1        
            
            if isValidPos(x, y - 1): stack.push((x, y - 1))  
            if isValidPos(x + 1, y): stack.push((x + 1, y)) 
            if isValidPos(x, y + 1): stack.push((x, y + 1))  
            if isValidPos(x - 1, y): stack.push((x - 1, y))  

        print(f'현재 스택: {stack}')

    print("출구 찾기 실패.")
    return False

result = DFS()
if not result:
    print('미로 탐색 실패')
