## フィボナッチ数列を計算する関数
def fibonacci_number(n):
    if n < 3:
        return 1

    return fibonacci_number(n - 2) + fibonacci_number(n - 1)