def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(5, 10)
calc_sum(23, 69)

#INSHORT 
def calc_sum(a, b):
    return a + b

sum = calc_sum(1, 2)
print(sum)

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(1, 2, 3)


def calc_prod(a=1, b=8):
    print(a * b)
    return a * b 

calc_prod()

#ques
cities = ["pune", "abhay", "ritika", "sony"]
heroes = ["amol", "yash", "devansh"]

print(heroes[0], end = " ")
print(heroes[1], end = " ")   #iss se kya hoga ki amol yash 6 ek line mai aa jaye ge

def print_len(list):
    print(len(list))
    
print_len(cities)
print_len(heroes)

def print_list(list):
    for item in list:
        print(item, end = " ")
        
print_list(heroes)
print_list(cities)

#question

n = 5

def cal_fact(n):
    for i in range(1, n+1):
        fact *= i
        print(fact)
        
    cal_fact(4)
    cal_fact(9)

#question
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD = ", inr_val, "INR")
    
converter(2)  
converter(5)  

#RECURSION
def show(n):
    print(n)
    
show(5)

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    
show(5)
    
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(5))

# #QUESTION

# def cal_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n
    
# sum = calc_sum(10)
# print(sum)


#QUESTION 


def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
yo = ["hii", "abhay", "bro"]
print_list(yo)