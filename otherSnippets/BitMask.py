def test_set(number,index):
    return bool((number>>index)&1)

def test_set2(number,index):
    return bool(number&(1<<index))

print(test_set(10,1))
print(test_set2(10,1))

''''
Check if ith bit is set
'''
def mask(n,index):
    bitmask = 1 << index
    return bool(n & bitmask)

print(mask(32,5))

''''
Set given bit in a number
110011 -> 110111 for i = 2
'''
def set_bit(n,index):
    bitmask = 1<<index
    return n | bitmask

print(set_bit(51,2))

''''
Clear ith bit or Unset ith bit in a number
110011 -> 100011 for i = 4
'''
def unset_bit(n,index):
    bitmask = ~(1<<index)
    return bin(n & bitmask)

print(unset_bit(51,4))

'''
Toggle Bit
'''
def toggle(n,index):
    bitmask = 1 << index
    return bin(n ^ bitmask)

print('toggle',toggle(51,4))
print('toggle',toggle(51,3))