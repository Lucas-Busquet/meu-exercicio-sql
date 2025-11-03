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

# ETAPA 6: Atualizando a disponibilidade de um livro
print("[ETAPA 6] Atualizando disponibilidade de um livro...")

# Atualizar o livro "1984" para indisponível
cursor.execute('''
    UPDATE Livros 
    SET disponivel = 0 
    WHERE titulo = "1984"
''')

conn.commit()
print("Disponibilidade do livro '1984' atualizada para indisponível!")

# Verificar atualização
cursor.execute('SELECT titulo, disponivel FROM Livros WHERE titulo = "1984"')
resultado = cursor.fetchone()
status = 'Sim' if resultado[1] == 1 else 'Não'
print(f"  Status atual: {resultado[0]} - Disponível: {status}")

# ETAPA 7: Ordenar livros por ano (decrescente)
print("[ETAPA 7] Ordenando livros por ano (mais recente → mais antigo)...")

cursor.execute('SELECT titulo, autor, ano FROM Livros ORDER BY ano DESC')
livros_ordenados = cursor.fetchall()

print("Livros Ordenados por Ano:")
print("-" * 80)
for livro in livros_ordenados:
    print(f"{livro[2]} - {livro[0]} por {livro[1]}")

# ETAPA 8: Deletando livro publicado antes de 1940
print("[ETAPA 8] Deletando livro publicado antes de 1940...")

# Buscando livro antigo
cursor.execute('SELECT titulo, ano FROM Livros WHERE ano < 1940')
livro_antigo = cursor.fetchone()

if livro_antigo:
    print(f"  Livro a ser deletado: {livro_antigo[0]} ({livro_antigo[1]})")
    
    # Deletar o livro
    cursor.execute('DELETE FROM Livros WHERE ano < 1940')
    conn.commit()
    print(f"{cursor.rowcount} livro(s) deletado(s)!")
else:
    print("  Nenhum livro encontrado com ano anterior a 1940.")

# ETAPA 9: Criar tabela Usuario
print("[ETAPA 9] Criando a tabela de Usuario...")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

conn.commit()
print("Tabela Usuario criada com sucesso!")

# ETAPA 10: Adicionar coluna 'idade' na tabela Usuario
print("[ETAPA 10] Adicionando coluna 'idade' na tabela Usuario...")

try:
    cursor.execute('ALTER TABLE Usuario ADD COLUMN idade INTEGER')
    conn.commit()
    print("Coluna 'idade' adicionada com sucesso!")
except sqlite3.OperationalError as e:
    print(f"  Aviso: Coluna pode já existir - {e}")

print("\n[ETAPA 11] Inserindo 5 usuários...")

usuarios = [
    ("Ana Silva", 28),
    ("Carlos Santos", 35),
    ("Mariana Costa", 22),
    ("Pedro Oliveira", 41),
    ("Julia Ferreira", 30)
]

cursor.executemany('''
    INSERT INTO Usuario (nome, idade)
    VALUES (?, ?)
''', usuarios)

conn.commit()
print(f"{cursor.rowcount} usuários inseridos com sucesso!")

# Mostrar usuários cadastrados
cursor.execute('SELECT * FROM Usuario')
print("Usuários Cadastrados:")
print("-" * 50)
for usuario in cursor.fetchall():
    print(f"  ID: {usuario[0]} | Nome: {usuario[1]} | Idade: {usuario[2]}")

# Fechando a conexão
conn.close()
print("Conexão encerrada")