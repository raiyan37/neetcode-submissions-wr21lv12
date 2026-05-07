class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n) // 2

        lo, hi = 0, m

        while lo <= hi:
            mid1 = (lo + hi) // 2   # partition index for nums1
            mid2 = half - mid1       # partition index for nums2

            # values just left and right of each partition
            l1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            r1 = nums1[mid1]     if mid1 < m else float("inf")
            l2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            r2 = nums2[mid2]     if mid2 < n else float("inf")

            if l1 <= r2 and l2 <= r1:
                # found correct partition
                if (m + n) % 2 == 1:
                    return float(min(r1, r2))
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                hi = mid1 - 1
            else:
                lo = mid1 + 1