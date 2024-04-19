def  Multiplicar(a, b ):
  resultado = a*b
  return resultado

def  Soma( a,  b ):
  resultado = a+b
  return resultado

def divisao(a, b):
  return a / b

def Subtracao( a,  b):
  resultado = a-b
  return resultado 


if __name__ == '__main__':
  funcao = int(input("Digite a função que deseja | 1 - Multiplicação, 2- Soma, 3-Subtração,4-Divisão"))

  if(funcao == 1):
    a = int(input("Digite o valor do primeiro número"))
    b = int(input("Digite o valor do segundo número"))
    print(Multiplicar(a,b))
  elif (funcao == 2):
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(Soma(a, b))
  elif (funcao == 3):
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print(Subtracao(a,b))
  elif (funcao == 4):
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    try:
      print(divisao(a, b))
    except ZeroDivisionError:
      print('Não é possível dividir por 0')
  else :
    print("Digitou incorreto")
