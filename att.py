'''
# Programa  valorImpresso
a = 2
b = 5
c = 0
while c < 5 :
  c += 1
  a = a + b
  b = a
print(b)
# final do programa
'''
'''

   # Programa progMeses    
vetMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
num = int(input('Digite o número do mês desejado:'))
if num>=1 and num<=12 :
      print('O mês ', num, ' é ', vetMeses[num-1])
else :
      print('Mês inválido')

'''
'''
#Programa proSemana

vetSemana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
num = int(input("Digite o número do dia (1 a 7):"))
if num>= 1 or num <=7:
     print("O dia", num, "é", vetSemana[num-1])
else:
    print("Dia inválido")
'''


# Início do Programa
A = 20
B = 14
for c in range(0,3) :
  aux = A
  A   = B
  B   = aux
print(A)
# Final do Programa

