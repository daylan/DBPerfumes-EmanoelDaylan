import sqlite3

def inserirperfume(tabela,id,nome,quantidade,id_volume,id_marca,id_fixacao):
    cursor.execute(f"INSERT INTO {tabela} VALUES({id},'{nome}',{quantidade},{id_volume},{id_marca},{id_fixacao})")
    banco.commit()

def inseririd_nome(tabela,id,nome):
    cursor.execute(f"INSERT INTO {tabela} VALUES({id},'{nome}')")
    banco.commit()

def inseririd_id(tabela,id1,id2):
    cursor.execute(f"INSERT INTO {tabela} VALUES({id1},{id2})")
    banco.commit()

path = r"C:\SQlite\Aulas"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()

tabela = "Marcas"
inseririd_nome(tabela,1,"Avon")
inseririd_nome(tabela,2,"Boticario")
inseririd_nome(tabela,3,"Natura")

tabela = "Fixacoes"
inseririd_nome(tabela,1,"Longo")
inseririd_nome(tabela,2,"Curto")
inseririd_nome(tabela,3,"Medio")

tabela = "Perfumes"
inserirperfume(tabela,1,"Cristal Sândalo Fresh",5,1,1,2)
inserirperfume(tabela,2,"Herstory Eau de Parfum",3,1,1,1)
inserirperfume(tabela,3,"Floratta Blue",2,3,2,3)
inserirperfume(tabela,4,"Egeo Dolce",1,2,2,1)
inserirperfume(tabela,5,"Meu Primeiro Humor",7,1,3,3)
inserirperfume(tabela,6,"Natura Homem Essence",8,3,3,2)

tabela = "Volumes"
inseririd_nome(tabela,1,"100ml")
inseririd_nome(tabela,2,"200ml")
inseririd_nome(tabela,3,"300ml")

tabela = "Essencia_perfume"
inseririd_id(tabela,1,6)
inseririd_id(tabela,2,5)
inseririd_id(tabela,3,4)
inseririd_id(tabela,1,3)
inseririd_id(tabela,2,2)
inseririd_id(tabela,3,1)

tabela = "Essencias"
inseririd_nome(tabela,1,"Floral")
inseririd_nome(tabela,2,"Amadeirado")
inseririd_nome(tabela,3,"Citrico")


