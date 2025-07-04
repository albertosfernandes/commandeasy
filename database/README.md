### Atributos

**Atributo**    **Tipo**    **Observação**
---
id              string      chave primária
descricao       string      texto amigável descritivo
comando         string      o comando a ser executado
tags            list        para filtros ou sugestões por categoria
referencia      string      links para docs
created_at      string      ISO 8601 timestamp         

---
##### Subir e criar o banco Dynamodb local
```
docker run -d -p 8000:8000 --name dynamodb amazon\dynamodb-local
```

Dentro do diretório infra, executar o main.tf
```
terraform init
```
em seguida:
```
terraform apply
```