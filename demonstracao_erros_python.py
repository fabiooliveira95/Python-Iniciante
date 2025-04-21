try:
  from posix import write
  from os import writev
  ip_validos = open('teste.txt', 'r+')
  lista_validos = ip_validos.readline()

  for index in range(len(lista_validos)):
    lista_validos = [index], lista_validos = [index], str ('\n')

    ips_avaliar = open ('teste.txt', 'r+')
    lista_avaliar = ips_avaliar.readline()

    for index in range(len(lista_avaliar)):
      lista_avaliar = [index], lista_avaliar = [index], str ('\n')

      logip_validos = open('logip_validos.txt','w+')
      logip_invalidos = open('logip_invalidos.txt','w+')

      logip_validos.write('[endereco logip_validos:]\n')
      logip_invalidos.write('[endereco logip_invalidos:]\n')

      for ip in lista_avaliar:
        if lista_validos.count(ip) == 0:
          logip_invalidos.write(ip+'\n')

        else:
          logip_validos.write(ip+'\n')

          logip_validos.close()
          logip_invalidos.close()

except FileNotFoundError:
  print("execute o comando")

finally:
  print("programa finalizado")


  # a) #erros de sitaxe, tambem conhecidos como erros de parse, sao provavelmente
  # os mais frequentes entre aqueles que ainda estao apredendo python:
  # no caso a baixo falta aspas
  print('Hello Wold!')

  # b) #uma vez seu programa esta sintaticamente correto, o interpretador do python
  # pode importa-lo e começar a executa-lo o que poderia da errado?


  # c) #erro de semantica(semantic errors)ocorrem quando o programa nao
  # apresenta erro de sintaxe e nao ocorre um erro durante a execucao,
  # o programa executado do comeco ao fim, mas ele nao produz o
  # resultado desejado,isto indica que voce cometeu um erro de logica no
  # seu programa.

  try:
      f = open("file")
  except SyntaxError:
      print("execute o arquivo")
  except FileNotFoundError:
      print("execute o comando")
  else:
      print("tente novamente")
  finally:
      print(" o programa foi finalizado")