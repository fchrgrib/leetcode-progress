/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */



var increasingBST = function(root) {
    if(root.right == undefined && root.left == undefined) return root;
    let arr = [];
    function getAll(c){
        if(c == undefined) return;
        arr.push(c.val);

        getAll(c.left);
        getAll(c.right);
    }

    getAll(root);
    arr.sort((a, b) => a - b)
    console.log(arr)
    
    
    let tmp = new TreeNode(arr[0], undefined, new TreeNode());
    let tmp2 = tmp;
    for(let i = 1; i<arr.length;i++){
        tmp2.right = new TreeNode(arr[i], undefined, undefined);
        tmp2 = tmp2.right;
    }

    return tmp;
};