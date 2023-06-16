#myFile = open('hello.txt', 'r')
#file = myFile.read()
#print(file)
#myFile.close()

#with open('hello2.txt', 'w') as somefile:
 #   somefile.write('goodbye world')

#with open('test1.txt', 'w') as file:
 #   file.write('bye world')

#with open('test1.txt', 'a') as file:
#   file.write('\ngood world')

#чтение файла
#'r'
# readline()- считывает одну строку из файла
#read ()-считывает все содержимое файла в одну строку
# readlines()-считывает все строки файла в список

#with open('hello.txt') as f:
#   a = f.readlines()
#    b = list(map(int, a))
#   print(b [2])

#with open('hello.txt') as f:
#    a = f.readlines()
#    b = [int(x) for x in a]
#    print(b)

#with open('hello.txt') as f:
#    s = f.readlines()
#    a = list(map(int, s))
#    res = []
#    for i in a:
#        if str(i).count('0') >=2 and i % 5 == 0:
#            res.append(i)
#print(max(res), len(res))

#with open('hello.txt') as f:
#    s = [int(x) for x in f]
#    res = []
#    for i in range(1, len(s)):
#        if(abs(s[i]) % 10 == 7 or abs(s[i-1]) % 10 == 7) and (s[i] + s[i-1]) % 12 == 0:
#            res.append(s[i] + s[i-1])
#print(len(res), max(res))



