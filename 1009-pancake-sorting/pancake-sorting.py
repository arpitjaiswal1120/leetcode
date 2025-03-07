class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        out = []



        
        n = len(arr)
        for i in range(n-1, -1, -1):
            max_pos = self.get_max_pos(arr[:i+1])
            if(max_pos == i):
                continue
            out.append(max_pos+1)
            out.append(i+1)
            arr = arr[:max_pos+1][::-1] + arr[max_pos+1:]
            arr = arr[:i+1][::-1] + arr[i+1:]
        return out
    
    def get_max_pos(self, arr):
        m = 0
        for i in range(1, len(arr)):
            if(arr[m] < arr[i]):
                m = i
        return m
    
        