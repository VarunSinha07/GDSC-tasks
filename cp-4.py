def max_sum(li):
    max_so_far = li[0]
    max_ending_here = li[0]

    for num in li[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
    
li = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum(li)) 