class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            print("Queue is full")
        self.display_queue()

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            dequeued_item = self.array[self.front]
            self.array[self.front] = None
            self.display_queue()
            return dequeued_item
        else:
            print("Queue is empty")
            self.display_queue()

    def display_queue(self):
        print("Queue contents:", self)

    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front + 1 : self.rear + 1])
        else:
            return str(self.array[self.front + 1 : self.capacity] + self.array[0 : self.rear + 1])


def main():
    q = CircularQueue(10)
    print("사용할 명령어:")
    print("'e <값>' : enqueue (예: e 5)")
    print("'d' : dequeue")
    print("'q' : 프로그램 종료")

    while True:
        command = input("명령어 입력: ").strip()
        if command.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
        elif command.startswith('e '):
            # 명령어 분리 후 값을 정확히 하나만 추가하도록 설정
            try:
                _, value = command.split(maxsplit=1)  # 공백 기준으로 나누어 value 추출
                q.enqueue(value)
            except ValueError:
                print("올바른 입력 형식: e <값>")
        elif command == 'd':
            dequeued_value = q.dequeue()
            if dequeued_value is not None:
                print(f"삭제된 값: {dequeued_value}")
        else:
            print("잘못된 명령어입니다. 'e <값>' 또는 'd'를 사용하세요.")


if __name__ == "__main__":
    main()
