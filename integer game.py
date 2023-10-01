def max_product_after_partition(n: int) -> int:
    if n < 2:
        return 0  # 0 和 1 不能被拆分

        # 初始化dp数组
    dp = [0, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))

    return dp[n]

def main():
    # 读取用户输入的正整数n
    n = int(input("请输入一个正整数 n: "))
    # 调用函数并输出结果
    print(f"拆分 {n} 后得到的最大乘积为: {max_product_after_partition(n)}")


if __name__ == "__main__":
    main()