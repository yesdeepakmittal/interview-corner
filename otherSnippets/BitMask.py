def test_set(number,index):
    return bool((number>>index)&1)

def test_set2(number,index):
    return bool(number&(1<<index))

print(test_set(10,1))
print(test_set2(10,1))