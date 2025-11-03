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
print("\n[ETAPA 4] Inserindo 5 livros fictícios...")

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
cursor.execute("SELECT * FROM Livros")
print("Livros cadastrados:")
for livro in cursor.fetchall():
    print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Gênero: {livro[4]}, Disponível: {'Sim' if livro[5] == 1 else 'Não'}")
    
# Fechando a conexão
conn.close()
print("Conexão encerrada")