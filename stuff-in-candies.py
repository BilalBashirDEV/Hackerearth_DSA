
def extra_candy (n, candies, extra_candies):
    # Write your code here
    rs=[]
    max=0
    for i in range(n):
        if candies[i]>max:
            max=candies[i]
    for i in range(n):
        if extra_candies+candies[i] >= max:
            rs.append(1)
        else:
            rs.append(0)



    return rs

n = int(input())
candies = list(map(int, input().split()))
extra_candies = int(input())

out_ = extra_candy(n, candies, extra_candies)
print (' '.join(map(str, out_)))
