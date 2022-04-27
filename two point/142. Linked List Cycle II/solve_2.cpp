/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode * fast = head;
        ListNode * slow = head;

        do
        {
            // 到顶
            if(!fast || !fast->next) return nullptr;
            fast = fast->next->next;
            slow = slow->next;
        }while(fast != slow);

        // 第一次相遇后，fast = head，然后再一步步相遇
        fast = head;
        while(fast != slow)
        {
            fast = fast->next;
            slow = slow->next;
        }

        return fast;
    }
};