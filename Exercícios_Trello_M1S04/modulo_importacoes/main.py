import func_calculadora as calc
import func_datas as data



escolha = input("Qual operação básica deseja fazer?\n1.Somar\n2.Subtrair\n3.Multiplicar\n4.Dividir\n")

if escolha == "1":
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))
        resultado = calc.soma(num1,num2)
        print(f"Resultado = {resultado}")
elif escolha == "2":
        num1 = int(input(("Digite o primeiro valor: ")))
        num2 = int(input(("Digite o segundo valor: ")))
        resultado = calc.subtracao(num1,num2)
        print(f"Resultado = {resultado}")
elif escolha == "3":
        num1 = int(input(("Digite o primeiro valor: ")))
        num2 = int(input(("Digite o segundo valor: ")))
        resultado = calc.multiplicacao(num1,num2)
        print(f"Resultado = {resultado}")   
elif escolha == "4":
        num1 = int(input(print("Digite o primeiro valor: ")))
        num2 = int(input(print("Digite o segundo valor: ")))
        resultado = calc.divi(num1,num2)
        print(f"Resultado = {resultado}") 
else:
        print("Você não escolheu um número inválido, tente novamente !")

print(f"Você fez essa operação: {data.data_hoje()}")
