# jewels를 리스트로 바꾸고 stones for문 돌려서 같은 문자 나오면 카운트 되도록 함

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        list_jewels = list(jewels)
        
        stone = 0

        for s in stones:
            if s in list_jewels:
                stone += 1
        return stone