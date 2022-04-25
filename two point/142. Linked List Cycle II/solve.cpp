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
        ListNode *slow = head;
        ListNode *fast = head;

        do
        {
            // 肯定要判空的，说明没有环
            //! 我老想的很麻烦，想要 for() 来遍历
            //! if(!slow || !fast || !fast->next) return nullptr; 判断 slow 做啥
            if(!fast || !fast->next) return nullptr;
            slow = slow->next;
            fast = fast->next->next;
        }while(slow != fast);

        // 相遇了，有环, 把 fast 拉到开头再一步步遍历
        fast = head;
        while(fast != slow)
        {
            fast = fast->next;
            slow = slow->next;
        }
        return fast;
    }
};