class Solution(object):
    import heapq
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        hq = []
        inf = 10**7
        dist = [inf]*n
        dist[src] = 0

        adj = {i: [] for i in range(n)}
        for i,j,c in flights:
            adj[i].append([j,c])
        
        # stop, cost, destination
        hq = [[0, 0, src]]
        while(len(hq)>0):
            stops, cost, destination = hq.pop(0)
            if(stops>k):
                continue
            for nb, c in adj[destination]:
                if(dist[nb] > cost + c):
                    dist[nb] = cost + c
                    hq.append([stops+1, dist[nb], nb])
        if(dist[dst] == 10**7):
            return -1
        return dist[dst]
