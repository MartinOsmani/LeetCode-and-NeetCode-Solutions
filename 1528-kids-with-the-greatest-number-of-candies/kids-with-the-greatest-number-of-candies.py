class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        candies_needed = max_candies - extraCandies
        result = []
        for kid in candies:
            if kid >= candies_needed:
                result.append(1)
            else:
                result.append(0)
        return result
                
                
