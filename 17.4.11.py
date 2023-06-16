N_max = int(input("Определите размер очереди:"))

queue = [0 for _ in range(N_max)]
order = 0
head = 0
tail = 0

def is_epty():
    return  head == tail and queue[head] == 0

def size():
    if is_epty():
        return 0
    elif head == tail:
        return N_max
    elif head > tail:
        return N_max -head +tail
    else:
        return tail - head


    def add():
        global  tail, order
        order += 1
        queue[tail] = order
        print("Задача №%d в приоритете" %(queue)[head])
        queue[head] = 0
        head = (head + 1) % N_max

    while True:
        cmd = input("Введите команду:")
        if cmd == "empty":
            if is_empty():
                print("Очередь пустая")
            else:
                print("В очереди есть задачи")
        elif cmd == "size":
            print("Количество задач в очереди" , size())
        elif cmd == "add":
            if size() != N_max:
                add()
            else:
                print("Очередь переполнена")
        elif cmd == "show":
            if is_empty():
                print("Очередь пустая")
            else:
                show()
        elif cmd == "do":
            if is_empty():
                print("Очередь пустая")
            else:
                do()
        elif cmd == "exit":
            for _ in range(size()):
                do()
            print('Очередь пустая. Завершение работы')
            break
        else:
            print("Введена неверная команда")



N_max = int(input("Определите размер очереди:"))

queue = [0 for _ in range(N_max)]
order = 0
head = 0
tail = 0

def is_empty():

    return head == tail and queue[head] == 0

def size():
    if is_empty():
        return 0
    elif head == tail:
        return N_max
    elif head > tail:
        return N_max - head + tail
    else:
        return tail - head


def add():
    global tail, order
    order += 1
    queue[tail] = order
    print("Задача №%d добавлена" % (queue[tail]))


    tail = (tail + 1) % N_max

def show():
    print("Задача №%d в приоритете" % (queue[head]))

def do():
    global head
    print("Задача №%d выполнена" % (queue[head]))
    queue[head] = 0
    head = (head + 1) % N_max

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if is_empty():
            print("Очередь пустая")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")