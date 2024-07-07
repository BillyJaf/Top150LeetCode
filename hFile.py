"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        pointer = len(citations) - 1

        papers = 0

        while pointer >= 0:
            if citations[pointer] > papers:
                papers += 1

            if citations[pointer] <= papers:
                return papers
            
            pointer -= 1
        return papers
