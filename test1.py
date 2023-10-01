def break_integer(n):
    if n <= 1:
        return 1

    dp = [0, 1]

    for i in range(2, n + 1):
        max_product = 0
        print(f"i = {i}, dp = {dp}")  # 在每次外层循环开始时打印 i 和 dp[] 的值
        for j in range(1, i):
            print(f"  j = {j}, i - j = {i - j}, dp[i - j] = {dp[i - j]}")  # 在每次内层循环开始时打印 j, i - j 和 dp[i - j] 的值
            max_product = max(max_product, max(j * (i - j), j * dp[i - j]))
        dp.append(max_product)

    return dp[n]


# 以 n=10 运行函数并打印中间变量的值
break_integer(10)
