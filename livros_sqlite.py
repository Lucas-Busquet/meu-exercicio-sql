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

# ETAPA 4: Inserir 5 livros fictícios
print("[ETAPA 4] Inserindo 5 livros fictícios...")

livros = [
    ("1984", "George Orwell", 1949, "Ficção Distópica", 1),
    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia", 1),
    ("Dom Casmurro", "Machado de Assis", 1899, "Romance", 1),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil", 0),
    ("A Revolução dos Bichos", "George Orwell", 1945, "Fábula Política", 1)
]

# Inserindo os livros no banco de dados
cursor.executemany('''
    INSERT OR IGNORE INTO Livros (titulo, autor, ano, genero, disponivel)
    VALUES (?, ?, ?, ?, ?)
''', livros)    

conn.commit()
print("livros inseridos com sucesso") 

#mostrar os livros inseridos
cursor.execute('SELECT * FROM Livros')
print("\nLivros cadastrados:")
for livro in cursor.fetchall():
    print(f"  ID: {livro[0]} | {livro[1]} - {livro[2]} ({livro[3]})")
  
# ETAPA 5: Consultar os livros disponíveis
print("[ETAPA 5] Consultando livros disponíveis...")

cursor.execute('SELECT * FROM Livros WHERE disponivel = 1')
livros_disponiveis = cursor.fetchall()

print("Livros Disponíveis:")
print("-" * 80)
for livro in livros_disponiveis:
    print(f"ID: {livro[0]} | {livro[1]} | {livro[2]} | Ano: {livro[3]} | {livro[4]}")    


# Fechando a conexão
conn.close()
print("Conexão encerrada")