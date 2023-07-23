class Solution(object):
    ## an n^2 implementation that is very clunky and relies on two loops and
    ## built in python sort function
    def merge1(self, nums1, m, nums2, n):
        ## solution 1
        # j = 0
        # while j < n:
        #     for i in range(len(nums1)):
        #         if nums1[i] == 0:
        #             nums1[i] = nums2[j]
        #             j += 1

        # # nums1.sort()

    
    ## a quicker solution (m+n?) which also uses sort but uses list
    ## comprehension to make the code shorter
    def merge3(self, nums1, m, nums2, n):
        for i in nums2:
            nums1.append(i)
        nums1 = [i for i in nums1 if i != 0]
        nums1.sort()

    ## this one is nicer and entirely in place without relying on sort()
    def merge2(self, nums1, m, nums2, n):
        # for i in range(n):
        #     if nums2[0] < nums1[i]:
        #         nums1.insert(i, nums2[0])
        #         nums2.pop(0)
        #         nums1.pop(-1)

        # if nums1[-1] == 0 and len(nums2) > 0:
        #     for i in nums2:
        #         nums1.append(i)

        # nums1 = [i for i in nums1 if i != 0]


def main()
    sol = Solution()
    sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    sol.merge([1], 1, [], 0)
    sol.merge([0], 0, [1], 1)
        
