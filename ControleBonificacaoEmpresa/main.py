from funcionarioEgerente import *
from controleBonificacao import *

#===== Criação de funcionários =====#
funcionario1 = Funcionario("João", "101.212.442-88", 2867.90)
funcionario2 = Funcionario("Marcos", "111.442.471-44", 1212.20)
funcionario3 = Funcionario("Brenda", "001.154.613-10", 5879.88)
funcionario4 = Funcionario("Sofia", "101.245.236-09", 7956.99)
funcionario5 = Funcionario("Lucas", "012.445.481-03", 7249.45)

#===== Criação de gerentes =====#
gerente1 = Gerente("Carlos", "003.016.787-66", 9243.00, "abcde12345", 3)
gerente2 = Gerente("Rebeca", "011.012.250-09", 17839.65, "df6f58808ebfd3e609c234cf2283a989", 2)

#===== Instância da classe ControleDeBonificacoes =====#
controleDeBonificacoes = ControleDeBonificacoes()

#===== Salários antes da bonificação =====#
print(f"{funcionario1.nome} portante do CPF: {funcionario1.cpf}, tem o salário de R${funcionario1.salario} (Antes da bonificação)\n")

print(f"{funcionario2.nome} portante do CPF: {funcionario2.cpf}, tem o salário de R${funcionario2.salario} (Antes da bonificação)\n")

print(f"{funcionario3.nome} portante do CPF: {funcionario3.cpf}, tem o salário de R${funcionario3.salario} (Antes da bonificação)\n")

print(f"{funcionario4.nome} portante do CPF: {funcionario4.cpf}, tem o salário de R${funcionario4.salario} (Antes da bonificação)\n")

print(f"{funcionario5.nome} portante do CPF: {funcionario5.cpf}, tem o salário de R${funcionario5.salario} (Antes da bonificação)\n")

print(f"{gerente1.nome} portante do CPF: {gerente1.cpf}, tem o salário de R${gerente1.salario} (Antes da bonificação)\n")

print(f"{gerente2.nome} portante do CPF: {gerente2.cpf}, tem o salário de R${gerente2.salario} (Antes da bonificação)\n")

#===== Registro de todas as pessoas na classe ControleDeBonificacoes =====#
controleDeBonificacoes.registra(funcionario1.getBonificacao())
controleDeBonificacoes.registra(funcionario2.getBonificacao())
controleDeBonificacoes.registra(funcionario3.getBonificacao())
controleDeBonificacoes.registra(funcionario4.getBonificacao())
controleDeBonificacoes.registra(funcionario5.getBonificacao())
controleDeBonificacoes.registra(gerente1.getBonificacao())
controleDeBonificacoes.registra(gerente2.getBonificacao())

#===== Salários depois da bonificação =====#
print(f"{funcionario1.nome} portante do CPF: {funcionario1.cpf}, tem o salário de R${funcionario1.salario} (Depois da bonificação)\n")

print(f"{funcionario2.nome} portante do CPF: {funcionario2.cpf}, tem o salário de R${funcionario2.salario} (Depois da bonificação)\n")

print(f"{funcionario3.nome} portante do CPF: {funcionario3.cpf}, tem o salário de R${funcionario3.salario} (Depois da bonificação)\n")

print(f"{funcionario4.nome} portante do CPF: {funcionario4.cpf}, tem o salário de R${funcionario4.salario} (Depois da bonificação)\n")

print(f"{funcionario5.nome} portante do CPF: {funcionario5.cpf}, tem o salário de R${funcionario5.salario} (Depois da bonificação)\n")

print(f"{gerente1.nome} portante do CPF: {gerente1.cpf}, tem o salário de R${gerente1.salario} (Depois da bonificação)\n")

print(f"{gerente2.nome} portante do CPF: {gerente2.cpf}, tem o salário de R${gerente2.salario} (Depois da bonificação)\n")

#=====  Soma de todos os salários (com bonificação) =====#
print(f"O valor total dos salários, com a bonificação de final de ano desta empresa será de: R${controleDeBonificacoes.getTotalBonificacoes()}")