# 📘 Configuração e Instalação 

## 📌 Sumário



Este repositório descreve os procedimentos técnicos para instalação e configuração dos seguintes componentes:

MongoDB via Docker

Mongo Compass (interface gráfica)

Apache Airflow com integração ao MongoDB

## ✅ Pré-requisitos
Docker instalado no sistema operacional
👉 https://docs.docker.com/

Acesso à linha de comando (terminal, shell ou prompt de comando)

## 🚀 Passo a Passo
### 1. Instalação do Docker
Siga as instruções disponíveis no site oficial:

🔗 Instalar Docker

### 2. Instalação do Mongo Compass
Acesse: Download Mongo Compass

Faça o download da versão adequada ao seu sistema.

Execute o instalador e siga as instruções.

### 3. Preparação dos Arquivos de Configuração
Você deve receber um arquivo .zip com os arquivos necessários (ex: docker-compose.yml, Dockerfile, etc).

Descompacte esse arquivo em um diretório à sua escolha.

### 4. Inicialização do Ambiente Docker
* Abra o terminal.

* Navegue até o diretório onde os arquivos foram descompactados:
```
cd: bash
cd <caminho_para_a_pasta_descompactada>
```

* Inicialize os serviços do Airflow:
```
docker compose build --no-cache
```

* Após isso, para iniciar os serviços do Airflow em modo detached (em segundo plano), execute:
``` 
docker compose up -d
```

* O ambiente Docker com Airflow e MongoDB estará agora em execução. Para acessar a interface web do Airflow, localize a porta mapeada para o serviço web no Docker Desktop ou através da inspeção dos containers. A URL será similar a http://localhost:<porta>.

* Credenciais Padrão do Airflow:
  - Username: ```airflow```
  - Password: ```airflow```
  
### 5. Configuração da Conexão MongoDB no Airflow
Acesse a interface web do Airflow.

Vá em Admin > Connections.

Clique em + Create e preencha para adicionar uma nova conexão:

- Conn Id: 	```mongodb_default```
- Conn Type: ```mongo``` Se a opção "Mongo" não estiver disponível, siga as instruções no próximo sub-passo para instalar o provider
- Host: ```mongo``` Este é o nome do serviço MongoDB definido no arquivo ```docker-compose.yml```
- Username:	```root```
- Password:	```example```
- Port: ```27017``` 

### 6. Configuração da Conexão RabbitMQ no Airflow
Acesse a interface web do Airflow.

Vá em Admin > Connections.

Clique em + Create e preencha para adicionar uma nova conexão:

- Conn Id: 	```rabbitmq_default```
- Conn Type: ```generic``` 
- Host: ```localhost``` Este é o nome do serviço RabbitMQ definido no arquivo ```docker-compose.yml```
- Username:	```user```
- Password:	```password```
- Port: ```5672``` 
- Schema: ```ampq```

**Instalação do Provider MongoDB (se necessário):**
  - Abra um novo terminal ou prompt de comando.
    
  - Navegue até o diretório onde os arquivos descompactados foram salvos:
        
     ```cd <caminho_para_a_pasta_descompactada>```
        
  - Execute o seguinte comando para acessar o container `airflow-apiserver`:
        
     ```docker exec -it airflow-airflow-apiserver-1 bash```
        
  - Dentro do container, execute o comando para instalar o provider MongoDB para Airflow:
        
     ```pip install apache-airflow-providers-mongo```
        
  - Saia do container:Bash
        
     ```exit```
        
  - Reinicie o serviço `airflow-apiserver` para aplicar as alterações:Bash
        
     ```docker-compose restart airflow-apiserver```
        
  - No campo "Extra Fields (JSON)", adicione a seguinte configuração:JSON
    
     ```{ "srv": null, "authSource": "admin", "ssl": false}```
    
  - Clique no botão "Save" para salvar a conexão MongoDB.

### 6. Configuração do Mongo Compass:

- Abra o aplicativo Mongo Compass instalado.
- Na tela inicial, clique em "Connect".
- Na janela de conexão, insira a seguinte URL de conexão:
    
    `mongodb://root:example@mongo:27017/admin`
    
- Clique no botão "Connect".
- O Mongo Compass deverá se conectar à instância MongoDB em execução no Docker.

### Conclusão:

Após seguir estes passos, o ambiente com MongoDB rodando em Docker, a interface gráfica Mongo Compass configurada para acesso e a conexão do MongoDB integrada ao Apache Airflow estarão estabelecidos e prontos para uso.






