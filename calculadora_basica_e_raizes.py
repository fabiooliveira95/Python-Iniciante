#
print("fabio oliveira")

a = 5
b = 3
c = 5
print(a * b, c)

a = int(input("Digite o promeiro numero:"))
b = int(input("Digite o segundo numero:"))

operacao = input("Digite a operacao a realizar (/, *, +, -):")
if operacao == "+":
     print(a+b)
elif operacao == "-":
     print(a-b)
if operacao == "*":
     print(a*b)
elif operacao == "/":
     print(a/b)
else:
     print("operacao invalida!")
     resultado = 0
print("resultado: ", resultado)


for x in range (11):
       print(x)

       list1 = [2, 30, 41, 67, 8, 97, 6, 41]

       even_count, odd_count = 0, 0
       for num in list1:

           if num % 2 == 0:
               even_count += 1
           else:
               odd_count += 1

       print("Even numbers in the list1: ", even_count)
       print("odd numbers in the list1: ", odd_count)


       # calcular as raizes de uma equacao do 2° grau

       def raizes(a, b, c):
           D = ("""a=1,b=-5,c=6
               a=1,b=0,c=-9
               a=5,b=-45,c=0
               a=1,b=-1,c=-12
               a=1,b=-6,c=10""")
           x1 = (-b + D ** (1 / 2)) / (2 * a)
           x2 = (-b - D ** (1 / 2)) / (2 * a)

           print('\nValor de x1: {0}'.format(x1))
           print('Valor de x2: {0}'.format(x2))


       if __name__ == '__main__':
           while True:
               print('calculando as raizes de uma equacao de 2° grau\n')
               a = float(input('Entre com o valor de a: '))
               b = float(input('Entre com o valor de b: '))
               c = float(input('Entre com o valor de c: '))

               continua = (input('Deseja sair? Digite N ou enter para calculo: '))

               if (continua == 'N'):
                   break

                   nome = input("Digite seu nome: ").upper()
                   print("Parametro UM: ", nome[:: 1])