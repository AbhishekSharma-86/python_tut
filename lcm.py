def lcm(x,y):
    i=1
    a=1
    b=1
    while(True):
        a=x*i
        b=y*i
        if a==b:
            ans=a
        else:
            i+=1
    return ans
    
        
z=lcm(16,24)
print(z)


