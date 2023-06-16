#import requests


#r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html') # делаем запрос на сервер по переданному адресу
#print(r.content)

#import requests

#r =requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
#print(r.status_code)

#import requests

#r = requests.get('https://baconipsum.com/api/?type=meat-and-filler') #  попробуем поймать json ответ
#print(r.content)

#Меняем код и превратим данный текст в список

#import requests
#import json # импортируем необходимую библиотеку

#r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
#texts = json.loads(r.content) # делаем из полученных байтов python объект для удобной работы
#print(type(texts)) # проверяем тип сконвертировнных данных

#for text in texts : # выводим полученный текст . Но для того чтобы он влез в консоль оставим только первые 50 символов.
 #    print(text[:50], '\n')

 # Словарь

#import requests
#import json

#r = requests.get('https://api.github.com')

#print(r.content)



#import requests
#import json

#r = requests.get('https://api.github.com')

#d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы

#print(type(d))
#print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений


# POST -запросы

#import requests

#r = requests.post('https://httpbin.org/post', data = {'key': 'value'}) # отправляем пост запрос
#print(r.content) # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет

#import requests
#import json

#data = {'key': 'value'}

#r = requests.post('https://httpbin.org/post', json=json.dumps(data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
#print(r.content)

# Home work

import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
r = json.loads(r.content)
print(r [0])