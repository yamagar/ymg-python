def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer = answer * i
    return answer

def factorial_recursive(n):
    if ( n < 2 ): return 1
    return n * factorial_recursive(n-1)

def fib(n):
    if n < 3 :return 1
    return fib(n-2) + fib(n-1)

def fib_memo(n):
    memo = {1:1, 2:1}
    def _fib_memo(n):
        if n in memo: return memo[n]
        memo[n] = _fib_memo(n-2) + _fib_memo(n-1)
        return memo[n]
    return _fib_memo(n)


print(factorial(5)) #120を表示予定
print(factorial_recursive(5)) #120を表示予定
print(fib(1)) # 1 
print(fib(2)) # 1 
print(fib(3)) # 2
print(fib(4)) # 3
print(fib(5)) # 5
print(fib(10)) # 55
#print(fib(100)) # 全然終わらない。。。。ハイマシンスペックでないとだめ。
print(fib_memo(100))
