source = int(input())

source_list = [int(i) for i in str(source)]
source_set = set(source_list)

'''
amplified
'''
amplified = 0
for i in source_set:
    amplified += i
'''
base
'''
base = len(source_set)
if base == 1:
    base = 10
'''
target
'''
target = ""
x = amplified
while x != 0:
    target = str(x%base) + target
    x = x //base

print(amplified,base,target)