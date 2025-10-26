# 1. Two Sum

**Initial notes**

I first brute-forced this problem with a solution that compared each number with every other, but that solution was wrong because it returned a value even if the sum was formed by adding a number with itself. So, I included a check to ensure that wasn't the case. This gave me a O(n^2) solution.

I asked an LLM to critique my solution and nudge me towards a better solution. From that conversation, I realized that a hash map (dictionary) would allow me to check if the complement of the number at each index position was present in the list. Since lookups are O(1) in a hash map, the time complexity of my solution would be O(n). The space complexity would also be O(n) since in the worst case, each element of the list would have to be added to the dictionary.