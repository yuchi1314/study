"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
"""
def makeArrayConsecutive2(statues):
    statues.sort()
    a = 0
    for i in range(0,len(statues)-1):
        if statues[i+1] - statues[i] == 0:
            a += 0
        else:
            a += statues[i+1] - statues[i] - 1
    return a