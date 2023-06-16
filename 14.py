#def print_2_add_2():
  # result = 2 + 2
   #print(result)
#def hello_world():
    #print('Hello World')


#def revers_star(n):
    #for i in range(n, 0, -1):
        #print("*" *i)
#revers_star(5)

def pow_func(base, n=2):
    print(base ** n)
print(pow_func(3))

def pow_func(base, n=2):
    print(base ** n)
    return None
print(pow_func(3))

def pow_func(base, n=2):
    inside_result=base ** n
    return inside_result
print(pow_func(3))


def get_multipliers(a):
   count = 0
   for n in range(1, a + 1):
       if a % n == 0:
           count += 1

   return count

print(get_multipliers(5))
print(get_multipliers(4))

def chek_polindrome(str_):
    str_= str_.lower()
    str_= str_. replace(" ", "")
    if str_ == str_[::-1]:
        return True
    else:
        return False
print(chek_polindrome("test"))
print(chek_polindrome("Кит на море не романтик"))


