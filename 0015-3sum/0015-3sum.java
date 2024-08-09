class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List <List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length;
        for(int i=0;i<n;i++){
            if(nums[i]>0)break;
            else if(i!=0 && nums[i]==nums[i-1])continue;
            
            
            int j=i+1,k=n-1;
            
            while(j<k){
                int sum = nums[i]+nums[j]+nums[k];
                if(sum<0)j++;
                
                else if(sum>0)k--;   
                
                else{
                    List<Integer> temp = Arrays.asList(nums[i],nums[j], nums[k]);
                    ans.add(temp);
                    j++;
                    while(j<k && nums[j]==nums[j-1])j++;
                    k--;
                    while(j<k && nums[k]==nums[k+1])k--;
                }
            
        }
    }return ans;
}}