import time

def hanoi_tower(n, fr, tmp, to):
    global call_count
    if n == 1:
        print("원판 1: %s -> %s" % (fr, to))
        call_count += 1
    else:
        hanoi_tower(n - 1, fr, to, tmp)
        print("원판 %d: %s -> %s" % (n, fr, to))
        call_count += 1
        hanoi_tower(n - 1, tmp, fr, to)

def solve_hanoi(n):
    global call_count
    call_count = 0
    start = time.time()
    
    hanoi_tower(n, 'A', 'B', 'C')
    
    end = time.time()
    print("호출 수: ", call_count)
    print("실행 시간 = ", end - start)

n = int(input("하노이 타워 높이: "))
solve_hanoi(n)
