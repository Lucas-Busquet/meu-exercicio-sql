import sqlite3

# Conectando ao banco de dados (ou criando-o se não existir)
conn = sqlite3.connect('livraria.db')
cursor=conn.cursor()

print("="*50)
print("ETAPA 3: Criar tabela de livros")
print("="*50 )

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL UNIQUE,
        autor TEXT,
        ano INTEGER,
        genero TEXT,
        disponivel INTEGER DEFAULT 1
    )
''')
conn.commit()
print("Tabela Livros criada")

# Fechando a conexão
conn.close()
print("Conexão encerrada")