# Asking for expression
input = input("Expression: ")

x, y ,z = input.split()

match y:
    case "+":
        print(float(x) + float(z))
    case "-":
        print(float(x) - float(z))
    case "*":
        print(float(x) * float(z))
    case "/":
        print(round(float(x) / float(z), 1))
