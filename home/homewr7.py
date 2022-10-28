def get_list() -> list:
    return list(range(0, 1000, 2))
def search(arr, low, high, desired):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == desired:
            return mid
        elif arr[mid] > desired:
            return search(arr, low, mid - 1, desired)
        else:
            return search(arr, mid + 1, high, desired)
    else:
        return -1
desired = int(input('Введите четное число: '))
class Solution:
    def find_target(self):
        target = desired
        list = get_list()
        result = search(list,0,len(list)-1, target)
        if result != -1:
            print(f'Введенное число {target} имеет индекс {result} в последовательности\n {list}')
        else:
            print(f'Введенное число не представлено в последовательности\n {list}')
a = Solution()
a.find_target()
