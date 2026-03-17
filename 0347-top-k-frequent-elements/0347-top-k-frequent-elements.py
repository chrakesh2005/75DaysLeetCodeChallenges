class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sorted_nums = sorted(freq, key=freq.get, reverse=True)
        return sorted_nums[:k]