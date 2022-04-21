def power(n, m):
    if m==0:
        return 1
    else:
        if m%2==0:
            temp = power(n, m//2)
            return (temp*temp)%10007
        else:
            temp = power(n, m-1)
            return (temp*n)%10007
