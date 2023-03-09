class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = l1, None
        curr2, prev2 = l2, None

        while curr:
            next, curr.next = curr.next, prev
            prev, curr = curr, next
        
        head = prev

        while curr2:
            next2, curr2.next = curr2.next, prev2
            prev2, curr2 = curr2, next2

        head2 = prev2

        def convert_list_to_array(head):
            array = []
            while head is not None:
                array.append(head.val)
                head = head.next
            return array

        array = convert_list_to_array(head)
        string_array = [str(i) for i in array]
        result = "".join(string_array)
        #print(result)

        array2 = convert_list_to_array(head2)
        string_array2 = [str(j) for j in array2]
        result2 = "".join(string_array2)
        #print(result2)

        sum_res = int(result) + int(result2)
        #print(sum_res)

        sum_res_arr = list(map(int,str(sum_res)))
        sum_res_arr.reverse()

        def listToNode(lst):
            head = None
            while lst:
                head = ListNode(lst.pop(),head)
            return head
        
        answer = listToNode(sum_res_arr)

        return answer
