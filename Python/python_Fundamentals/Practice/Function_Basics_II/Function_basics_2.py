

#^ 1 . Countdown 

def countdown (a):
    list = []
    for i in range(a , -1 , -1):
        list.append(i)
    return list

print(countdown(5))


#^ 2 . Print and return

def print_and_return(a):
    if not isinstance (a , list ) or len(a) != 2 :
        raise ValueError("function only accept liste of 2 numbers")
    for element in a :
        if not isinstance (element, (int, float)):
            raise ValueError ("all elemet from list must be numbers")
    print(a[0])
    return a[1]

try:
    print(print_and_return([3,5]))
    print(print_and_return([3,5,9]))
except ValueError as e :
    print(e)


#^ First plus length

def first_plus_length (my_list) : 
    if not isinstance(my_list,list) :
        raise ValueError ("Function only accept list")
    for element in my_list :
        if not isinstance(element,(int,float)) :
            raise ValueError ("All element must be numbers")
    a = my_list[0] + len(my_list)
    return a

try :
    print(first_plus_length([1,2,3,4,5]))
    print(first_plus_length([1,"hello",2,3]))
except ValueError as e :
    print(e)


#^ Value Grater than Second

def greater_than_second(my_list) :
    if not isinstance(my_list,list) :
        raise ValueError ("Function only accept list")
    for element in my_list :
        if not isinstance(element,(int,float)) :
            raise ValueError ("All element must be numbers")
    
    if len(my_list) < 2 :
        return False
    else :
        result = []
        for element in my_list :
            if element > my_list[1] :
                result.append(element)
            else :
                continue
        print(len(result))
        return result
    
try :
    print(greater_than_second([5,2,3,2,1,4]))
    print(greater_than_second([3]))
except ValueError as e :
    print(e)
    


#^ This Length, That Value 

def length_value(size,value):
    result =[]
    for i in range(size,0 , -1) :
        result.append(value)
    return result

print(length_value(4,7))
print(length_value(6,2))