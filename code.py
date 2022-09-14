def add(a, b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def menu():
    print('1: Add\n2: Subtract\n3: Multiply\n4: Division\n5: Exit\n')

choice = 'null'

while choice != '5':
    menu()
    choice = input('Select: ')
    
    if choice == '1':
        a = int(input('Enter First Number: '))
        b = int(input('Enter Second Number: '))
        print(a, '+', b, '=', add(a,b))

    elif choice == '2':
        a = int(input('Enter First Number: '))
        b = int(input('Enter Second Number: '))
        print(a, '-', b, '=', sub(a,b))

    elif choice == '3':
        a = int(input('Enter First Number: '))
        b = int(input('Enter Second Number: '))
        print(a, 'x', b, '=', mul(a,b))

    elif choice == '4':
        a = int(input('Enter First Number: '))
        b = int(input('Enter Second Number: '))
        print(a, '/', b, '=', div(a,b))

    elif choice == '5':
        exit()
    
    else:
        print('Wrong Input')