class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        l = 0
        count = {}

        # Count characters in s1
        for c in s1:
            count[c] = count.get(c, 0) + 1

        window = {}

        for r in range(len(s2)):

            # Add s2[r] to the window
            window[s2[r]] = window.get(s2[r], 0) + 1

            window_size = r - l + 1

            # If window is too big, remove s2[l]
            if window_size > s1_len:
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]  
                l += 1

            # Check if window has same character counts as s1
            if window == count:
                return True

        return False