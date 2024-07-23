responses = ['welcome to smart calc', 'my name is calc', 'thanks for using me', 'sorry, this is beyond my ability']


def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a, b):
    return a*b

def division(a, b):
    return a/b

def mod(a, b):
    return a%b

operations = {
  'ADD': add,
  'PLUS': add,
  'SUM': add,
  'ADDITION': add,
  'SUB': sub,
  'SUBTRACT': sub,
  'MINUS': sub,
  'DIFFERENCE': sub,
  'PRODUCT': multiply,
  'MULTIPLY': multiply,
  'MULTIPLICATION': multiply,
  'DIVISION': division,
  'MOD': mod,
  'REMAINDER': mod,
  'MODULAS': mod
}

def myname():
    print(responses[1])

def end():
    print(responses[2])
    input('press enter to exit')
    exit()

commands = {
  'NAME': myname,
  'EXIT': end,
  'END': end,
  'CLOSE': end
}

def extract(text):
    l = []

    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


print(responses[0])
print(responses[1])

while True:
    text = input('enter your queries: ')

    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract(text)
                r = operations[word.upper()](l[0], l[1])
                print(r)
            except:
                print('something went wrong, pls try again.')
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        print(responses[3])