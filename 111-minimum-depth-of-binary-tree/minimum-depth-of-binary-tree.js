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
 * @return {number}
 */
var minDepth = function(root) {

    const dfs = (root) => {
        if(root === null){
            return 0;
        }
        if(root !== undefined && root?.left === null && root?.right === null){
            return 1
        }

        let min_l = Infinity;
        let min_r = Infinity;

        if (root?.left !== null){
            min_l = 1 + dfs(root?.left);
        }
        if (root?.right !== null){
            min_r = 1+dfs(root?.right);
        }

        return min_l >min_r?min_r:min_l;
    }
    return dfs(root);
};