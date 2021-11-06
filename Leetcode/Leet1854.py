class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        maxValue = 0
        earliestYear = 1950
        arr = [0 for i in range(101)] #d = [1950,2050]
        
        for i in logs:
            for year in range(i[0],i[1]):
                arr[year - 1950] += 1
        return arr.index(max(arr)) + 1950