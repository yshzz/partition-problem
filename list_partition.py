from typing import List


def is_partitionable(nums: List[int]) -> bool:
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return False

    sub_list_sum = total_sum // 2
    n = len(nums)

    partition_data = [[False] * (sub_list_sum + 1) for _ in range(n + 1)]
    partition_data[0][0] = True

    for i in range(1, n + 1):
        curr = nums[i - 1]
        for j in range(sub_list_sum + 1):
            if j < curr:
                partition_data[i][j] = partition_data[i - 1][j]
            else:
                partition_data[i][j] = partition_data[i - 1][j] or partition_data[i - 1][j - curr]

    return partition_data[n][sub_list_sum]
