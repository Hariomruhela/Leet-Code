/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    map= new Map()
    for(i=0;i<=nums.length;i++){
        const compliment=target-nums[i]
        if (map.has(compliment)) {
        return [map.get(compliment), i];
    }
        map.set(nums[i],i)
    }
};