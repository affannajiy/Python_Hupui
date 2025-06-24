#Activity1
'''
listFoo = [3, 6, 9, 12, 15, 18, 21]
listFaa = [4, 8, 12, 16, 20, 24, 28]

#a
listFum = listFoo[0:3] + listFaa[3:7]
print(listFum)

#b
listFee = listFoo[1::2] + listFaa[::2] #[1::2] means 1 is the initial index and 2 is for the step value
print(listFee)

#c
removed = listFoo.pop(4)
listFaa.insert(1, removed)
listFaa.append(removed)
print(listFoo)
print(listFaa) '''

#Activity2
#1
'''
def func_a():
  print('inside func_a')
def func_b(y):
  print('inside func_b')
  return y
def func_c(z):
  print('inside func_c')
  return z()
print(func_a())
print(5+func_b(2))
print(func_c(func_a))

'''
'''
#2
def f(y):
  y=y+3
  x = 1
  x += 1
  print(x)
  print(y)
def g(y):
  print(x)
  print(x+1)
def h(y):
  return x+1
x = 5;f(x)
print('after call 1',x)
g(x);print('after call 2',x)
h(x);print('after call 3',x)
'''

#3
def f(x):
  x = x + 1
  print('in f(x): x =', x)
  return x
def g(x):
  def h(x):
    x = x+1
    print("in h(x): x = ", x)
  x = x + 1
  print('in g(x): x = ', x)
  h(x)
  return x
x = 3;z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)
x = 3;z = g(x)
print('in main program scope: x =', x)
print('in main program scope: z =', z)

'''
#Activity3
def GET_INPUT():
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    operation = input("Enter operation [ADD, SUBTRACT, MULTIPLY, DIVIDE]: ").upper()
    return num1, num2, operation

def ADD(num1, num2):
    return num1 + num2

def SUBTRACT(num1, num2):
    return num1 - num2

def MULTIPLY(num1, num2):
    return num1 * num2

def DIVIDE(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def CALC():
    num1, num2, operation = GET_INPUT()

    if operation == "MULTIPLY":
        result = MULTIPLY(num1, num2)
    elif operation == "DIVIDE":
        result = DIVIDE(num1, num2)
    elif operation == "ADD":
        result = ADD(num1, num2)
    elif operation == "SUBTRACT":
        result = SUBTRACT(num1, num2)
    else:
        result = "Invalid operation"
  
    print("Result:", result)

# Call calculator
CALC() '''