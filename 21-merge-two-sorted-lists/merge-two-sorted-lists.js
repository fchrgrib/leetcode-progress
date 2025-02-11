/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let arr = [];

    while(!(list1 == undefined)){
        arr.push(list1.val);
        list1 = list1.next;
    }

    while(!(list2 == undefined)){
        arr.push(list2.val);
        list2 = list2.next;
    }

    arr.sort((a,b) => a-b);
    if(arr.length ==0) return list1;

    

    let res=  new ListNode(arr[0], undefined);
    let tmp = res;

    for(let i = 1;i<arr.length;i++){
        tmp.next = new ListNode(arr[i], undefined);
        tmp = tmp.next;
    }

    return res;
};