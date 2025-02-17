class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if (find(nums.begin(), nums.end(), 1) == nums.end()) return 1;
        priority_queue<int, std::vector<int>, std::greater<int>> pq;

        for(int i = 0;i<nums.size();i++)  pq.push(nums[i]);
        int target = 1;

        while(!pq.empty()){
            if(target == pq.top()) target++;
            pq.pop();
        }

        return target;
    }
};


// for i in range(len(nums)):
//             if nums[i]<=0:
//                 continue
//             if len(pq) == 0:
//                 heapq.heappush(pq, (nums[i], i))
//                 continue
//             print(pq)
//             if nums[i] == minEl:
//                 minEl = 2**31
//             if nums[i] - pq[len(pq) - 1][0] > 1:
//                 minEl = min(minEl, pq[len(pq) - 1][0]+1)
            
//             if pq[0][0] - nums[i] > 1 and nums[i] >=0:
                
//                 minEl = min(minEl, nums[i]+1)
            
//             if nums[i]>0:
//                 heapq.heappush(pq, (nums[i], i))

//         if minEl == 2 ** 31:
//             return pq[len(pq) - 1][0]+1

//         return minEl