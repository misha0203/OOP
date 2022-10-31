def get_list() -> list:
    return list(range(0, 100, 2))
list = get_list()

class Solution:
    # list = get_list()
    def __init__(self):...
    def find_target(self, list, target):
        low = 0
        high = len(list) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if list[mid] == target:
                return mid
            elif list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


res = Solution()
print(res.find_target(list, 8))
