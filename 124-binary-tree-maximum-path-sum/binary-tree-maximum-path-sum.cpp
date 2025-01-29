/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    map<TreeNode*, int> dp;
    int maxVal = INT_MIN;
    int dfs(TreeNode* root){
        if(root == nullptr) return 0;
        
        int maxEl = INT_MIN;

        maxEl = max(maxEl, root->val);
        
        
        if(root->left){
            maxVal = max(maxVal, maxPathSum(root->left));
            maxEl = max(maxEl, root->val + dp[root->left]);
        }
        if(root->right){
            maxVal = max(maxVal, maxPathSum(root->right));
            maxEl = max(maxEl, root->val + dp[root->right]);
        }

        if(root->left && root->right){
            maxVal = max(maxVal, dp[root->left] + dp[root->right] + root->val);
        }

        dp[root] = maxEl;
        maxVal = max(maxVal,maxEl);

        return maxEl;
    }
    int maxPathSum(TreeNode* root) {
        dfs(root);
        return maxVal;
    }
};