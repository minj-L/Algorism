# Try 1 45ms
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalArray = [[0 for innerZero in range(numRows)] 
        for outerZero in range(numRows)]

        pascalArray[0][0] = 1
        for idx1 in range(1, numRows):
            pascalArray[idx1][0] = 1
            for idx2 in range(1, idx1 + 1):
                pascalArray[idx1][idx2] = pascalArray[idx1 - 1][idx2 - 1] + pascalArray[idx1 - 1][idx2]

        result = [[x for x in inner_list if x != 0] for inner_list in pascalArray]
        return result