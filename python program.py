
##n=int(input('enter a range'))
##for i in range(1,n+1):
##    for j in range(1,n+1):
##     print('*',end=' ')
##    print() 


##n=int(input('enter a name'))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##      print('*',end=' ')
##    print()
##        


##n=int(input('enter a range'))
##a=0
##b=1
##for i in range(3,n+1):
##    s=a+b
##    a=b
##    b=s
##    if b>=n:
##        print(a)
##        break



##n=int(input('enter a range'))
##a=0
##b=1
##print(a,b,end=" ")
##count=3
##while count<n:
##    s=a+b
##    print(s,end=" ")
##    a=b
##    b=s
##    count+=1

##n=int(input('enter a number'))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print('*',end=" ")
##    print()


##n=int(input('enter a number'))
##i=1
##while i<=n:
##    for j in range(i):
##        print('@',end=' ')
##        j+=1
##    print()
##    i+=1


##n=int(input('enter a number'))
##for i in range(1,n+1):
##    for j in range(n,i-1,-1):
##        print('*',end=" ")
##    print()


##n=int(input('enter a number'))
##for i in range(1,n+1):
##    for k in range(n,i,-1):
##        print(' ',end=' ')
##    for j in range(1,i+1):
##        print('*',end=' ')
##    print()

##
##n=int(input('enter a name'))
##for i in range(1,n+1):
##    for k in range(n,i,-1):
##        print(' ',end=' ')
##    for j in range(1,i+1):
##        print('*',end=' ')
##    print()
##
##n=int(input('enter a number'))
##for i in range(n):
##    for k in range(n,i,-1):
##        print(' ',end=' ')
##    for j in range(n):
##        print('*',end=' ')
##    print()
##

##n=int(input('enter a number'))
##for i in range(1,n+1):
##    for k in range(n,i,-1):
##        print(' ',end=' ')
##    for j in range(1,i+1):
##        print('*',end=' ')
##    print()
##    



##n=int(input('enter a number'))
##for i in range(n):
##    for k in range(n,i,-1):
##        print(' ',end=' ')
##    for j in range(n):
##        print('*',end=' ')
##    print()
##

##n=int(input('enter a number'))
##i=1
##while i<=n:
##    for j in range(i):
##        print('*',end=' ')
##        j+=1
##    print()
##    i+=1

##def great():
##    print('dinesh')
##    print('sai')
##great()
##
##great()

##def add(x,y):
##     c=x+y
##     print(c)
##add(5,5)

##def sub(x,y):
##    c=x-y
##    print(c)
##sub(5,8)
##        
##def add(x,y):
##    c=x+y
##    print(c)
##add(5,8)
##

##def human(name,age):
##    print(name)
##    print(age+5)
##human('dinesh',18)



##def human(name,age):
##    print(name)
##    print(age+5)
##human(age=16,name='sai')
##
##def add(x,y):
##    z=x+y
##    print(z)
##add(10,20)

##def human(name,age):
##    print(name)
##    print(age)
##human('dinesh',16)

##def human(name,age=16):
##   print(name)
##   print(age)
##human('dinesh')


##def add(x,*y):
##    c=x
##    for i in y:
##          c+=i
##    print(c)
##add(1,2,3,4,5,6,7,8,9,10)

##def add(x,*y):
##    c=x
##    for i in y:
##        c+=i
##    print(c)
##add(100,200,300,400,500,600,700,800,900,1000)
##
##

##
##def add(x,y):
##    c=x+y
##    return(c)
##result=add(4,9)
##def sub():
##    a=result-1
##    print(a)
##sub()

##def is_even_odd(n):
##    if n%2==0:
##       print('even')
##    else:
##       print('odd')
##n=6
##is_even_odd(n)
##
##
##def is_even_odd(n):
##    if n%2==0:
##        print('even')
##    else:
##        print('odd')
##n=6
##is_even_odd(n)
##
##def is_prime(n):
##    fc=0
##    for i in range(1,n+1):
##        if n%i==0:
##            fc+=1
##    if fc==2:
##        return True
##    else:
##        return False
##def right_prime(n):
##    i=n+1
##    while 1:
##       if is_prime(i):
##        return i
##       i+=1
##def left_prime(n):
##    j=n-1
##    while 1:
##        if is_prime(j):
##         return j
##        j+=1
##def near_prime(n):
##    if is_prime(n):
##        prime(n)
##    else:
##        x=right_prime
##        y=left_prime
##        if abs(n-x)<abs(n-y):
##           print(x)
##       elif  abs(n-x)>abs(n-y):
##            prime(y)
##       else:
##         print(y,x)
##n=10
##near_prime(10)

##def dinesh():
##    a=100
##    print(a)
##dinesh()
##        
##
##def ark():
##    n=int(input('enter a number'))
##    for i in range(1,n+1):
##        for k in range(n,i,-1):
##            print(' ',end=' ')
##        for j in range(1,i+1):
##            print('*',end=' ')
##        print()
##ark()
##
##ark()

##ark()
##

##def add(a,b):
##    c=a+b
##    return(c)
##food=add(5,5)
##def sub():
##    k=food-1
##    print(k)
##sub()

##def add(a,b):
##    c=a+b
##    print(c)
##a=int(input('enter a namber'))
##b=int(input('enter a number'))
##add(a,b)
##
##add(4,4)

##def add(a,b):
##    c=a+b
##    return(c)
##a=int(input('enter a number'))
##b=int(input('enter  a number'))
##print(add(a,b))
##print(add(5,5))

##def add(a,b):
##    c=a+b
##    print(c)
##add(4,7)
##
##def sub(a,b):
##    c=a-b
##    print(c)
##sub(2,4)
##
##def mul(a,b):
##    c=a*b
##    print(c)
##mul(20,20)
##
##def div(a,b):
##    c=a/b
##    print(c)
##div(2,4)
##
##def main():
##    add(5,3)
##    sub(2,4)
##    mul(20,20)
##    div(a/b)
##print(____name____)
##if ___name___=='___main____':
##    main()
##    
##

##a=10
##print(a)
##def sai():
##    a=20
##    print(a)
##sai()
##print(a)
##

##
##a=10
##print(a)
##def k():
##    global b
##    b=30
##    print(b)
##k()
##print(b)
##    

##def add(a,b):
##    return a+b
##def sub(a,b):
##    return a-b
##def mul(a,b):
##    return a*b
##def div(a,b):
##    return a/b
##a=int(input('enter a number'))
##b=int(input('enter a number'))
##
##print(add(a,b))
##print(sub(a,b))

##
##def add(a,b):
##    return a+b
##def sub(a,b):
##    return a-b
##def mul(a,b):
##    return a*b
##def div(a,b):
##    return a/b
##
##a=int(input('enter a number'))
##b=int(input('enter a number'))
##c=int(input('enter a 1:add,2:sub,3:mul,4:div'))
##if c==1:
##    print(add(a,b))
##elif c==2:
##    print(sub(a,b))
##elif c==3:
##    print(mul(a,b))
##elif c==4:
##    print(div(a,b))
##else:
##    print('wrong number')

##a=int(input('enter a number'))
##b=int(input('enter a number'))
##d=int(input('enter a number'))
##c= a**2+b**2+d**2
##print(c)

##a,b,c=map(int,input().split())
##d=a**2-b**2-c**2
##print(d)


##a=50
##print(eval('a+1'))
##print(a)

##def sai():
##    for i in range(n):
##        for k in range(n,i,-1):
##            print(' ',end=' ')
##        for j in range(n):
##            print('*',end=' ')
##        print()
##n=int(input('enter a number'))    
##sai()

##n=5
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or i==n or j==1 or j==n: 
##           print("*",end=" ")
##        else:
##           print(" ",end=" ")
##    print()       


##n=5
##for i in range(1,n+1):
##    for k in range(n-i,0,-1):
##        print(' ',end=" ")
##    for j in range(1,n+1):
##        if i==1 or i==n or j==1 or j==n:
##            print('*',end=" ")
##        else:
##            print(' ',end=" ")
##    print()


##n=10
##for i in range(1,n+1):
##    for k in range(n-i,0,-1):
##        print(' ',end=" ")
##    for j in range(1,n+1):
##        if i==1 or i==n or j==1 or j==n:
##            print('*',end=" ")
##        else:
##            print(' ',end=" ")
##    print()

##n=5
##for i in range(n):
##    for j in range(65,65+n):
##        print(chr(j),end=" ")
##    print()

##n=20
##for i in range(n):
##    for j in range(65,65+n):
##        print(chr(j),end=" ")
##    print()

##n=26
##for i in range(1,n+1):
##    for j in range(65,65+i):
##        print(chr(j),end=' ')
##    print()

##n=26
##for i in range(1,n+1):
##    for j in range(65,65+i):
##        print(chr(j),end=' ')
##    print()

##n=10
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end=' ')
##    for k in range(n-i,0,-1):
##        print('*',end= ' ')
##    print()

##n=10
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end=' ')
##    for k in range(n-i,0,-1):
##        print('*',end=' ')
##    print()




















































