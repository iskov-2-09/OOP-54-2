def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # j > i, чтобы не сравнивать элемент сам с собой
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # Если пара не найдена

nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(result)  # Вывод: [0, 1]
