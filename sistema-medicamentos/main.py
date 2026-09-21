import csv

arquivo = "medicamentos.csv"



def carregar():
    medicamentos = []

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)

            for medicamento in leitor:
                medicamentos.append(medicamento)

    except FileNotFoundError:
        pass

    return medicamentos



def salvar(medicamentos):
    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        campos = ["nome", "categoria", "quantidade"]

        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(medicamentos)



def buscar_medicamento(medicamentos, nome):
    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome.lower():
            return medicamento

    return None


medicamentos = carregar()

while True:
    print("\n--- FARMÁCIA ---")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("3 - Buscar medicamento")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

 
    if opcao == "1":
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        quantidade = input("Quantidade em estoque: ")

        medicamentos.append({
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade
        })

        salvar(medicamentos)

        print("Medicamento cadastrado!")

 
    elif opcao == "2":
        if len(medicamentos) == 0:
            print("Nenhum medicamento cadastrado.")
        else:
            for medicamento in medicamentos:
                print("\nNome:", medicamento["nome"])
                print("Categoria:", medicamento["categoria"])
                print("Quantidade:", medicamento["quantidade"])

  
    elif opcao == "3":
        nome = input("Digite o nome do medicamento: ")

        medicamento = buscar_medicamento(medicamentos, nome)

        if medicamento == None:
            print("Medicamento não encontrado.")
        else:
            print("\nNome:", medicamento["nome"])
            print("Categoria:", medicamento["categoria"])
            print("Quantidade:", medicamento["quantidade"])

  
    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")

        while True:

            print("TESTE FUNCIONOU")