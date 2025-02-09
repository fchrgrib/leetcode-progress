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
    priority_queue<int, vector<int>, greater<int>> pq;
    void bc(TreeNode* root){
        if(!root) return;
        pq.push(root->val);
        bc(root->left);
        bc(root->right);
    }
    TreeNode* increasingBST(TreeNode* root) {
        bc(root);
        TreeNode* t = new TreeNode(pq.top());
        pq.pop();
        TreeNode* t1 = t;
        while(!pq.empty()){
            t1->right = new TreeNode(pq.top());
            t1 = t1->right;
            pq.pop();
        }
        return t;
    }
};