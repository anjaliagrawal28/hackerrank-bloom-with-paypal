import math
import os
import random
import re
import sys

# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    tiles=0
    dir=[[1,1],[1,0],[0,1],[-1,-1],[-1,0],[0,-1],[-1,1],[1,-1]]
    obs={}
    if(obstacles): 
        for o in obstacles:
            obs[o[0],o[1]]=1

    for move in dir:
        i,j=r_q,c_q
        i+=move[0]
        j+=move[1]
        while(i<=n and j<=n and i>0 and j>0):
            
            if((i,j)in obs):
                break
            else:
                tiles+=1
            i+=move[0]
            j+=move[1]

    return tiles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
