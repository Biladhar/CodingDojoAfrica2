# BASIC :
for i in range (151) :
    print(i)


# Multiple of five
for i in range(5,1000):
    if i % 5 ==0 :
        print(i)
    else :
        continue


# Counting the dojo way
for i in range (1,100) : 
    if i % 10 == 0 :
        print("Coding Dojo")
    elif i % 5 == 0 :
        print ("coding")
    else :
        print (i)


# Whoa That Sucker's Huge
sum = 0
for i in range (500000):
    if i%2 != 0 :
        sum += i
    else :
        continue
print(sum)

#Couting by four
for i in range (2018, 0 , -4):
    print (i)

# Flexible counter
def flexibleCounter(a,b,c):
    for i in range (a , b+1) :
        if i % c == 0 :
            print(i)
        else :
            continue
        
flexibleCounter(2,9,3)