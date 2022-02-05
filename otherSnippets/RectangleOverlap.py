'''
a,b,c,d,e,f,g,h - all integers denoting cordinates of two rectangles
(a,b) -> bottom left cordinate of first rectangle
(c,d) -> top right cordinate of first rectangle
(e,f) -> bottom left cordinate of second rectangle
(g,h) -> top right cordinate of second rectangle


input
A = 0   B = 0
C = 4   D = 4
E = 2   F = 2
G = 6   H = 6

o/p -> 1

input 
A = 0   B = 0
C = 4   D = 4
E = 2   F = 2
G = 3   H = 3

o/p -> 1


Approach I used: just consider the cases in which rectangle won't overlap
'''

class Solution:
    def solve(self, A, B, C, D, E, F, G, H):
        if F >= D:
            return 0
        elif B >= H:
            return 0
        elif E >= C:
            return 0
        elif A >= G:
            return 0
        return 1
        