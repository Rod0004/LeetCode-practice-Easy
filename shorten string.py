def compress_string(s : str) -> str:
    if not s:
        return s

    compressed = []
    count = 1
    for i in range(1, len(s)):  # Corrected the range bound
        if s[i] == s[i - 1]:  # If the current character is the same as the previous one, increment the counter
            count += 1
        else:
            if count > 2:  # 修正了条件判断
                compressed.append(f"{count}x{s[i - 1]}")  # 使用 f-string 修正了字符串格式化
            else:
                compressed.append(s[i - 1] * count)
            count = 1  # 修正了字符的添加

    # Handle the last sequence of characters  # 添加了处理最后一组字符的逻辑
    if count > 2:
        compressed.append(f"{count}x{s[-1]}")
    else:
        compressed.append(s[-1] * count)

    return "".join(compressed)


print(compress_string("aabcaaade"))