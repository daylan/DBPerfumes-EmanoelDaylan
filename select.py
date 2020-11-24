import sqlite3

def titulo(n,s):
    print("=" * n)
    print(f"{s}".center(n))
    print("=" * n)

path = r"C:\SQlite\Aulas"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()

#marcas
cursor.execute("SELECT * FROM Marcas")
tabela = cursor.fetchall()
titulo(90,"Marcas De Perfume")
print("ID".ljust(5)+"Marca")
for linha in tabela:
    print(str(linha[0]).ljust(5), end="")
    print(linha[1])

#Perfumes
cursor.execute("SELECT * FROM Perfumes")
tabela = cursor.fetchall()
titulo(90,"Listar Perfumes Registrados")
print("ID".ljust(5)+"Nome".ljust(25)+"Quantidade".ljust(15)+"Volume".ljust(10)+"Marca".ljust(20)+"Fixacao".ljust(10)+"Fixação".ljust(10))
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(linha[1].ljust(25),end="")
    print(str(linha[2]).ljust(15),end="")

    cursor.execute(f"SELECT * FROM Volumes WHERE Volumes.id = {linha[3]}")
    tabela1 = cursor.fetchall()
    for linha1 in tabela1:
        print(linha1[1].ljust(10), end="")

    cursor.execute(f"SELECT * FROM Marcas WHERE Marcas.id = {linha[4]}")
    tabela1 = cursor.fetchall()
    for linha1 in tabela1:
        print(linha1[1].ljust(20), end="")

    cursor.execute(f"SELECT * FROM Fixacoes WHERE Fixacoes.id = {linha[5]}")
    tabela1 = cursor.fetchall()
    for linha1 in tabela1:
        print(linha1[1].ljust(10),end="")

    cursor.execute(f"SELECT * FROM Essencia_perfume WHERE Essencia_perfume.id_perfume_FK = {linha[0]}")
    tabela1 = cursor.fetchall()
    for linha1 in tabela1:
        cursor.execute(f"SELECT * FROM Essencias WHERE Essencias.id = {linha1[0]}")
        tabela2 = cursor.fetchall()
        for linha2 in tabela2:
            print(linha2[1].ljust(10),end="")
    print(" ")

