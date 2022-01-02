if __name__ == "__main__":
	# Length of longest consecutive ones with atmost one 0 replacement with 1
	s = '111001'
	n = len(s)
	pf = [0]*n 
	sf = [0]*n 
	pf[0] = ord(s[0]) - ord('0')
	sf[n-1] = ord(s[n-1]) - ord('0')
	MaxNum = 0

	import sys
	cnt = s.count('1')
	if cnt == n: #for edge case where each index is '1'
		print(n)
		sys.exit()

	for i in range(1,n):
		if s[i] != '0':
			pf[i] = pf[i-1] + 1
	for i in range(n-2,-1,-1):
		if s[i] != '0':
			sf[i] = sf[i+1] + 1
	def left(i,pf):
		if i == 0:
			return 0
		else:
			return pf[i-1]
	def right(i,sf):
		if i == len(sf)-1:
			return 0
		else:
			return sf[i+1]
    
    #replaced 1 can be used from outside not necessarily from string itself
	for i in range(n):
		L = left(i,pf)
		R = right(i,sf)
		
		if MaxNum < L + R + 1:  
			MaxNum = L+R+1
		
	print(MaxNum)


    #If replaced 1 needed to be used from string itself from another index
	for i in range(n):
		L = left(i,pf)
		R = right(i,sf)
		if s[i] == '0':
            # L = left(i,pf)
            # R = right(i,sf)
			if L + R + 1 <= cnt:
				if L + R + 1 > MaxNum:
					MaxNum = L + R + 1
			else:
				if L + R > MaxNum:
					MaxNum = L + R 
		else:
			if L + R + 1 > MaxNum:
				MaxNum = L + R + 1
	print(MaxNum)



''''
class Solution:
    # @param A : string
    # @return an integer    # 111001
    def solve(self, s):
        n = len(s)   #6
        pf = [0]*n   # [0,0,0,0,0,0]
        sf = [0]*n 
        pf[0] = ord(s[0]) - ord('0')
        sf[n-1] = ord(s[n-1]) - ord('0')
        MaxNum = 0

        import sys
        cnt = s.count('1')  #cnt = 4
        if cnt == n: #for edge case where each index is '1'
            return n
            # sys.exit()

        for i in range(1,n):
            if s[i] != '0':
                pf[i] = pf[i-1] + 1
        for i in range(n-2,-1,-1):
            if s[i] != '0':
                sf[i] = sf[i+1] + 1
        def left(i,pf):
            if i == 0:
                return 0
            else:
                return pf[i-1]
        def right(i,sf):
            if i == len(sf)-1:
                return 0
            else:
                return sf[i+1]
        for i in range(n):
            L = left(i,pf)
            R = right(i,sf)
            if s[i] == '0':
                # L = left(i,pf)
                # R = right(i,sf)
                if L + R + 1 <= cnt:
                    if L + R + 1 > MaxNum:
                        MaxNum = L + R + 1
                else:
                    if L + R > MaxNum:
                        MaxNum = L + R 
            else:
                if L + R + 1 > MaxNum:
                    MaxNum = L + R + 1
        return MaxNum
'''