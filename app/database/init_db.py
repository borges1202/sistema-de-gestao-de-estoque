from connection import conectar

conexao = conectar()
cursor = conexao.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

conexao.commit()

#Essa tabela organiza os produtos.
cursor.execute("""
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

#Essa tabela caracteriza os produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sku TEXT NOT NULL UNIQUE,
    descricao TEXT,
    quantidade INTEGER NOT NULL DEFAULT 0 CHECK (quantidade >= 0),
    estoque_minimo INTEGER NOT NULL DEFAULT 0 CHECK (estoque_minimo >= 0),
    categoria_id INTEGER NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
)
""")

#Essa é a tabela mais importante para rastreabilidade.
cursor.execute("""
CREATE TABLE IF NOT EXISTS movimentacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('ENTRADA', 'SAIDA')),
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    estoque_anterior INTEGER NOT NULL CHECK (estoque_anterior >= 0),
    estoque_atual INTEGER NOT NULL CHECK (estoque_atual >= 0),
    observacao TEXT,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (produto_id) REFERENCES produtos(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
""")

conexao.commit()
conexao.close()