odd_nums = int(15)

odd_to_15 = (nums for nums in range(1, odd_nums + 1, 2) if nums % 2 != 0)

for elem in odd_to_15:
    print(elem)
