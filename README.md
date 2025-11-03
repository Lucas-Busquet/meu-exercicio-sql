 P1:
O codigo simula um gerenciamento de uma livraria que executa uma sequencia de operações CRUD em duas tabelas: Livros e Usuario.

Da etapa (3-12)
.É criada as tabelas Livros e Usuario
.Uso do INSERT e executemany para preencher as tabelas
.SELECT e WHERE para filtrar dados(livros disponíveis)
.Uso de UPDATE para alterar as disponibilidades dos livros
.Uso do Order By para ordenar os livros
.ALTER TABLE para adicionar uma nova coluna
.DELETE e DROP TABLE para remover registros e fazer limpeza do banco de dados

Respostas das Questoes teóricas:
P2:

1 - Os bancos de dados são a espinha dorsal de qualquer aplicação moderna porque fornecem um meio seguro, consistente e escalável para armazenar, gerenciar e recuperar dados. Eles garantem que informações críticas (como registros de usuários ou transações financeiras) sejam acessíveis simultaneamente por múltiplos usuários, mantendo a integridade dos dados. Fonte: https://aws.amazon.com/pt/what-is/database-management/

2 - As duas principais categorias são: Bancos de Dados Relacionais (SQL), que organizam dados em tabelas com esquemas rígidos e usam JOINs para conectar dados; e Bancos de Dados Não Relacionais (NoSQL), que oferecem modelos flexíveis (documentos, chave-valor, grafos) ideais para dados não estruturados. Fonte: https://www.ibm.com/think/topics/database

3 - Bancos relacionais são recomendados quando a integridade e a consistência dos dados são críticas. Cenários ideais incluem: Sistemas Transacionais (ACID) como bancos e e-commerce; Dados com relacionamentos complexos e bem definidos; Aplicações que exigem consultas complexas (JOINs) e normalização. Fonte: https://cloud.google.com/products/databases?utm_source=google&utm_medium=cpc&utm_campaign=latam-BR-all-pt-dr-BKWS-all-all-trial-p-dr-1710136-LUAC0015918&utm_content=text-ad-none-any-DEV_c-CRE_536282978381-ADGP_Hybrid+%7C+BKWS+-+PHR+%7C+txt+-+Databases-Databases-General+Databases-BR-KWID_470847304013-kwd-470847304013&utm_term=KW_google%20cloud%20database-ST_Google+cloud+database&gclsrc=aw.ds&gad_source=1&gad_campaignid=14062855621&gclid=CjwKCAiAwqHIBhAEEiwAx9cTeeVf-1AiOusRis6Zqthfm5MLlNdeDmCzB03sA11tO0yMtGKSFD98HRoCyp0QAvD_BwE 

4 - A performance do hardware é vital: CPU processa consultas e transações; Memória (RAM) armazena dados em cache, acelerando a recuperação e reduzindo o acesso lento ao disco; Disco (SSD/HDD) determina a velocidade de leitura e gravação (I/O) dos dados persistidos. Um gargalo em qualquer recurso afeta a capacidade de processamento paralelo e a latência de resposta. Fonte: https://learn.microsoft.com/en-us/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server?view=sql-server-ver17

5 - Escalabilidade é a capacidade de um sistema aumentar sua performance ou capacidade para lidar com um volume crescente de trabalho. Ela pode ser: Vertical (Scale-Up), que é adicionar mais recursos (CPU/RAM) a um único servidor; ou Horizontal (Scale-Out), que é distribuir a carga de trabalho entre vários servidores (clusters). Fonte:  https://aws.amazon.com/pt/what-is/database-management/

6 - A organização correta (conhecida como normalização) é essencial para eliminar a redundância de dados e evitar anomalias de atualização, inserção e exclusão. Isso garante a consistência do sistema, torna a manutenção mais fácil e otimiza o desempenho das consultas, pois o banco de dados tem que lidar com menos dados duplicados. Fonte: https://mosten.com/banco-de-dados-relacional/

7- A escolha depende das necessidades do projeto: SQL é melhor para projetos que exigem consistência estrita, esquemas fixos e relacionamentos complexos. NoSQL é melhor para projetos com esquemas flexíveis, grandes volumes de dados não estruturados e necessidade de alta escalabilidade horizontal (muitas leituras/gravações). https://www.freecodecamp.org/news/sql-vs-nosql-tutorial/

COMANDOS SQL

1 - SELECT - Sua finalidade é recuperar dados de uma ou mais tabelas em um banco de dados.

2 - DML - Data Manipulation Language.
DLL - Data Definition Language.

3 - Where - Serve para filtrar os registros retornados por um comando SQL ex: SELECT ou DELETE.

4 - Assegura que cada linha de uma tabela seja única e identificável além de garantir integridade pois nenhuma coluna da chave primária pode ter valor nulo.

5 - UPDATE - Modifica dados existentes.

6 - REMOVE - remove linhas existentes.

7 - ORDER BY - Ordena o conjunto de resultados de uma consulta SELECT. 

8 - LIMIT - Restringe o número de registros retornados por uma consulta.

Outros Conceitos:
1 - A camada de backend (servidor) atua como o intermediário lógico entre a interface do usuário (frontend) e o banco de dados

2 - É uma tabela virtual. Não armazena dados próprios mas sim o código para obtê-los

3 - ATOMICIDADE, CONSISTENCIA, ISOLAMENTO e DURABILIDADE.Garantem a confiabilidade das transações em bancos de dados relacionais

4 - O PPM estabelece que um usuário ou processo deve receber apenas as permissões necessárias para executar sua função, e nada mais. Em bancos de dados, isso significa que as aplicações ou usuários devem ter permissões restritas (ex: apenas SELECT e UPDATE em uma tabela, sem permissão para DROP). Isso é crucial para reduzir a superfície de ataque em caso de violação de segurança.
