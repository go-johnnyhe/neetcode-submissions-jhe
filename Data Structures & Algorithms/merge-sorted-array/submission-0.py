class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_pointer, n_pointer = m - 1, n - 1
        last_pointer = len(nums1) - 1

        while m_pointer >= 0 and n_pointer >= 0:
            num1, num2 = nums1[m_pointer], nums2[n_pointer]
            if num1 >= num2:
                nums1[last_pointer] = num1
                m_pointer -= 1
            else:
                nums1[last_pointer] = num2
                n_pointer -= 1
            last_pointer -= 1   
        while n_pointer >= 0:
            nums1[last_pointer] = nums2[n_pointer]
            last_pointer -= 1
            n_pointer -= 1
