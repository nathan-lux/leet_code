class Solution(object):
    ## this one is nicer and entirely in place without relying on sort()
    ## this however does not do it in place as it uses append
    ## a more space efficient solution would be to push while deleting the last
    ## element
    def merge2(self, nums1, m, nums2, n):
        ## loop through nums1
        ## if nums2[0] < nums1[i] and nums2[0] != null
            ## insert nums2[0] at i
            ## pop nums2[0]
            ## pop nums1[-1]
        for i in range(len(nums1)):
            if len(nums2) > 0 and nums2[0] < nums1[i]:
                nums1.insert(i, nums2[0])
                nums2.pop(0)
                nums1.pop(-1)
        for i in range(len(nums2)):
            if nums1[-1] == 0:
                nums1.pop(-1)
        for i in nums2:
            nums1.append(i)

        print(nums1)

def main():
    sol = Solution()
    sol.merge2([1,2,3,0,0,0], 3, [2,5,6], 3)
    sol.merge2([1], 1, [], 0)
    sol.merge2([0], 0, [1], 1)
    sol.merge2([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)

main()
        
