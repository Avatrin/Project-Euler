numbers = range(1,10)
up = ['a','b','c']
up1 = ['d','c','e']
down = ['f','e','g']
down1 = ['h','g','i']
left = ['j','i','b']
ring = [up,up1,down,down1,left]
nums = {'a':10}

def new_num(node):
    new_list = ring[node:] + ring[:node]
    out_list= []
    for i in range(len(ring)):
        out_list.extend([str(nums[j]) for j in new_list[i]])
    return(int(''.join(out_list)))

import time as time
start = time.time()
import itertools as it
maxi = 0
for i in it.permutations('bcdefghij'):
    ind = 0
    for j in i:
        nums[j]=numbers[ind]
        ind += 1
    equality = sum([nums[i] for i in up])
    if nums['d']+nums['c']+nums['e']==equality and nums['f']+nums['e']+nums['g']==equality:
            if nums['h']+nums['g']+nums['i']==equality and nums['j']+nums['i']+nums['b']==equality:
                lowest_node_value = min([nums[ring[i][0]] for i in range(len(ring))])
                if nums[ring[1][0]]==lowest_node_value:
                    new_numb = new_num(1)
                elif nums[ring[2][0]]==lowest_node_value:
                    new_numb = new_num(2)
                elif nums[ring[3][0]]==lowest_node_value:
                    new_numb = new_num(3)
                else:
                    new_numb = new_num(4)
                if new_numb>maxi and len(str(new_numb))==16:
                    maxi = new_numb

print(maxi,time.time()-start)
