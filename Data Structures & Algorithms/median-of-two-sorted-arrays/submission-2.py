class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A,B = nums1, nums2
        if ( len(nums2) < len(nums1) ):
            A = nums2
            B = nums1
        l,r = 0,len(A)-1
        total = (len(A) + len(B))
        half = (total)//2
        while(True):
            m = l + (r-l)//2
            j = half - m - 2
            Aleft = A[m] if m>=0 else float('-inf')
            Aright = A[m+1] if m+1<len(A) else float('inf')
            Bleft = B[j] if j>= 0 else float('-inf')
            Bright = B[j+1] if j+1<len(B) else float('inf')

            if ( Aleft <= Bright and Bleft <= Aright ):
                if (total%2 == 0):
                    return (max(Aleft,Bleft) + min(Aright,Bright))/2
                else:
                    return min(Aright,Bright)
            else:
                if (Bleft > Aright):
                    l = m+1
                else:
                    r = m-1
        

            