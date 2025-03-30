import random
from collections import defaultdict

# 获取输入并确定顺序
a, b = map(int, input("请输入两个正整数（用空格分隔）：").split())
start, end = sorted((a, b))

# 计算等效整数区间 [[用户提示]]
m = (start + 1) // 2
n = end // 2

# 确定有效偶数区间
min_even = 2 * m
max_even = 2 * n

if min_even > max_even:
    print("输入范围内没有偶数，请重新输入！")
else:
    # 生成200万随机偶数（均匀分布）[[2]][[6]]
    random_evens = [random.randint(m, n) * 2 for _ in range(2000000)]
    
    # 字典统计次数 [[5]][[9]]
    count_dict = defaultdict(int)
    for num in random_evens:
        count_dict[num] += 1
    
    # 输出结果（按数值排序）
    print(f"\n产生2000000个{start}~{end}之间的随机偶数，统计如下：")
    print("数值\t次数\t百分比")
    for num in sorted(count_dict.keys()):
        percentage = count_dict[num] / 2000000 * 100
        print(f"{num}\t{count_dict[num]}\t{percentage:.2f}%")