class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        st = 0
        en = len(numbers)-1
        while True:
            if numbers[st] + numbers[en] < target:
                st += 1
            elif numbers[st] + numbers[en] > target:
                en -= 1
            else:
                return [st+1, en+1]