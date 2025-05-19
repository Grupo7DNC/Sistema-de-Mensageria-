# 📊 Categorização de Empresas por CNAE com Airflow e RabbitMQ

> Projeto desenvolvido para automatizar a classificação de empresas com base no CNAE, integrando Apache Airflow, MongoDB e RabbitMQ.

---

## 👤 Autor

Carlos Filho,
Julio Alcantra, 
Tawany Barbosa e 
Thiago Machado

## 🏫 Instituição

Escola DNC

## 📅 Data

05/04/2025

---

## 📌 Sumário

- [1. Business Understanding](#1-business-understanding)
- [2. Data Understanding](#2-data-understanding)
- [3. Data Preparation](#3-data-preparation)
- [4. Modeling](#4-modeling)
- [5. Evaluation](#5-evaluation)
- [6. Deployment](#6-deployment)
- [7. Notas Técnicas](#7--notas-técnicas)

---

## 1. Business Understanding

### 1.1 Objetivo do Negócio

O objetivo deste projeto é automatizar a **classificação de empresas por CNAE** (Classificação Nacional de Atividades Econômicas), a partir de bases atualizadas periodicamente. Sempre que uma **nova empresa** for detectada nos dados, uma **notificação** será enviada e a empresa será incluída na **fila de processamento**, categorizada por seu setor (com base no CNAE).

A automação do processo será realizada com o uso de **Airflow** para orquestração e **RabbitMQ** para gerenciar as filas por categoria.

- 📅 Dados atualizados periodicamente
- 🔔 Notificações de novas empresas
- 🧵 Fila de processamento segmentada por setor


### 1.2 Avaliação da Situação

- **Stakeholders:** Equipes de dados, ETL, risco e gestão.
- **Tecnologias utilizadas:**
    - Apache Airflow  (orquestração)
    - Mongo DB via Docker (Infraestrutura de Banco de Dados)
    - Mongo Compass (Interface Gráfica)
    - RabbitMQ (mensageria)
    - Python (desenvolvimento)
    - Pandas & NumPy (manipulação dos dados)
- **Benefícios esperados:**
  - 🚀 Eficiência no fluxo de dados
  - 🔄 Atualização automática
  - 📦 Categorias bem definidas
- **Restrições:** As bases de dados podem conter registros inconsistentes ou desatualizados, exigindo verificação contínua de qualidade.

### 1.3 Metas

- Dados Seguros e de Qualidade
- Identificar e categorizar automaticamente empresas novas por CNAE
- Monitorar a chegada de novos registros periodicamente
- Enviar os dados organizados em filas temáticas via RabbitMQ

### 1.4 Plano do Projeto

1. 📥 Coletar e validar dados de entrada
2. 🔎 Identificar registros novos
3. 🏷️ Categorizar por CNAE
4. 📨 Enviar dados organizados para filas específicas no RabbitMQ
5. 🛠️ Automatizar via Airflow (com DAG diária)
6. 🧩 Monitorar logs e filas para garantir robustez

---

## 2. Data Understanding

### 2.1 Coleta Inicial dos Dados
As bases de dados são arquivos CSV fornecidos por um sistema externo que contém  CNPJ, Empresas, Simples, Socios, Qualificações, Snapshot, Naturezas, Estabelecimentos, Municipios, Paises, Socios, CNAE principal e secundário, entre outros campos.

Arquivos:

- CNPJ
- Simples
- Socios
- Qualificações
- Snapshot
- Naturezas
- Estabelecimentos 
- Empresas
- CNAE principal e secundário
- Endereço

### 2.2 Descrição dos Dados
Os campos principais analisados são: 

| Campo             | Tipo   |
|-------------------|--------|
| CNPJ              | String | 
| Nome              | String | 
| Empresas          | String | 
| Estabelecimentos  | String |             |
| Endereço          | String |
| CNAE              | String |

### 2.3 Exploração dos Dados

- 📊 Frequência dos CNAEs
- 🗺️ Distribuição por Estados
- 🆕 Empresas novas detectadas em cada lote

### 2.4 Qualidade dos Dados

- ❌ Ausência de CNAEs
- 🔁 CNPJs duplicados
- ✅ Limpeza e padronização aplicadas

---

## 3. Data Preparation

### 3.1 Seleção de Dados

Utilizados: CNPJ, Nome, CNAE_Principal
Os demais campos foram descartados para manter o foco do projeto.

### 3.2 Limpeza dos Dados

- Remoção de duplicatas
- Preenchimento de CNAEs ausentes com `"Não informado"`
- Conversão de tipos

### 3.3 Construção dos Dados

- Criação do campo `categoria` com base no mapeamento CNAE → setor

### 3.4 Integração

- Comparação de bases, unindo os dados novos com uma base anterior para detectar empresas novas

### 3.5 Formatação dos Dados

- Dados formatados em JSON para envio ao RabbitMQ

---

## 4. Modeling

### 4.1 Técnicas de Modelagem

🔧 Mapeamento determinístico (sem aprendizado de máquina)

### 4.2 Design de Testes

- Testes unitários com registros simulados para CNAE e verificação de:
  - 📍 Identificação de empresas novas
  - 📤 Envio correto por categoria

### 4.3 Construção de Modelo

- Scripts Python categorizando empresas per CNAEs
- Envio para RabbitMQ com base no setor
- Criação de fila: 
  - `espresas`

### 4.4 Avaliação de Modelo

Testes em lote e em produção confirmam: 
- ✅ 100% de identificação
- 📦 100% de envio correto para a fila

---

## 5. Evaluation

### 5.1 Avaliação dos Resultados

Resultados atendem os critérios:
- Empresas novas detectadas e categorizadas
- Sistema opera sem falhas em lote

### 5.2 Revisão do Processo

Processo segue o objetivo original com:
- 🧪 Validação contínua
- 🔄 Integração com pipeline em produção

### 5.3 Próximos Passos

- 🌍 Escalar para outros estados
- 🤖 Introduzir recomendação automatizada de crédito com base no CNAE

---

## 6. Deployment

### 6.1 Pipeline via Airflow

- DAG mensal executa:
  - Leitura de novos dados
  - Comparação com base anterior
  - Categorização
  - Envio para RabbitMQ

### 6.2 Monitoramento

- Logs do Airflow
- Dashboards do RabbitMQ
- Verificação e reprocessamento de filas mortas

### 6.3 Relatótio Final

| Item        | Resultado                         |
|-------------|-----------------------------------|
| ✅ Objetivo | Dados de Qualidade e Segurança        |
| ⚙️ Ferramentas | Airflow, Python, MongoDB, RabbitMQ |
| 💰 Custo     | Baixo (open-source)              |
| 📈 Status    | Em produção                      |

### 6.4 Revisão do Projeto

| ✅ Funcionou bem                  | ⚠️ Melhorias sugeridas                   |
|-------------------------------|---------------------------------------|
| Automação mensal via Airflow  | Considerar CNAEs secundários       |
| Categorização precisa         | Criação de uma base de treinamento futura para classificação com IA |

---

## ✅ Notas Técnicas

### 📦 Tecnologias

- Apache Airflow
- RabbitMQ
- MongoDB + Mongo Compass
- Docker + Docker Compose
- Python (Pandas, NumPy)
- JSON: Formatação para envio

### 🔁 Ciclo de Execução da DAG

1. Realiza o download dos arquivos mais recentes
2. Transforma os dados em csv
3. Realiza tratamento inicial dos dados e insere os registros no banco de dados de camada bronze
4. Publica os dados processados em uma fila de mensagens RabbitMQ
5. Executa a limpeza e descarte de dados temporários ou obsoletos das collections armazenadas na camada bronze

