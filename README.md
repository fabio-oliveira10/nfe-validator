# Validador de XML de NF-e

Aplicação desenvolvida em Python para automatizar a leitura de arquivos XML de Nota Fiscal Eletrônica (NF-e), validar regras fiscais básicas e gerar relatórios de inconsistências em CSV e Excel.

O projeto foi criado para praticar automação aplicada à área Fiscal, estruturando um fluxo completo de processamento de documentos fiscais, desde a leitura do XML até a geração de relatórios para apoio à conferência.

---

## Visão Geral

A aplicação percorre automaticamente uma pasta contendo arquivos XML de NF-e, extrai informações relevantes da nota fiscal, executa validações de conformidade e consolida os resultados em relatórios.

Ao final da execução, são gerados arquivos CSV e Excel contendo todas as inconsistências identificadas, além de um resumo estatístico da análise.

---

## Escopo Atual

O projeto foi desenvolvido utilizando arquivos XML simplificados para fins de estudo e demonstração.

As validações implementadas representam regras básicas de conformidade fiscal e servem como base para futuras evoluções, como validações oficiais de CNPJ, leitura de SPED e cruzamento entre documentos fiscais.

---

## Funcionalidades

### Leitura dos XMLs

* Leitura automática de arquivos XML de NF-e
* Extração de informações do emitente
* Extração de informações do destinatário
* Extração dos produtos da nota
* Extração dos valores totais

### Validações Fiscais

* Validação de CFOP
* Validação de NCM
* Validação básica de CNPJ
* Conferência entre o total da nota e a soma dos produtos
* Tratamento de campos obrigatórios ausentes

### Relatórios

* Geração automática de relatório em CSV
* Geração automática de relatório em Excel (.xlsx)
* Organização das inconsistências por regra fiscal
* Resumo estatístico da execução

---

## Fluxo da Aplicação

```text
Arquivos XML
      │
      ▼
Leitura dos XMLs
      │
      ▼
Extração das Informações
      │
      ▼
Validações Fiscais
      │
      ▼
Consolidação dos Erros
      │
      ▼
Relatórios CSV e Excel
```

---

## Tecnologias Utilizadas

| Tecnologia  | Aplicação                         |
| ----------- | --------------------------------- |
| Python      | Desenvolvimento da solução        |
| ElementTree | Leitura e processamento dos XMLs  |
| Decimal     | Precisão nos cálculos financeiros |
| CSV         | Geração do relatório em CSV       |
| OpenPyXL    | Geração do relatório em Excel     |

---

## Estrutura das Informações Geradas

Cada inconsistência identificada contém:

* Arquivo analisado
* Status da validação
* Regra fiscal
* Campo validado
* Alvo da validação
* Mensagem da inconsistência

Ao final da execução, também são apresentados:

* Total de arquivos analisados
* Quantidade de arquivos válidos
* Quantidade de arquivos com inconsistências
* Taxa de aprovação
* Quantidade de erros por tipo de validação

---

## Regras de Validação

Durante o processamento dos XMLs são realizadas verificações como:

* Conferência da soma dos produtos com o valor total da nota
* Verificação da existência do CFOP
* Validação do CFOP contra lista de códigos permitidos
* Verificação da existência do NCM
* Validação do prefixo do NCM
* Validação básica do tamanho do CNPJ
* Tratamento de campos obrigatórios ausentes

---

## Desafios Resolvidos

* Organização do projeto em módulos independentes
* Leitura estruturada de arquivos XML
* Tratamento de campos ausentes sem interrupção da execução
* Padronização das validações fiscais
* Geração automatizada de relatórios em múltiplos formatos
* Consolidação estatística dos resultados da auditoria

---

## Como Executar

### Instalação

```bash
pip install openpyxl
```

### Execução

```bash
python main.py
```

Os arquivos XML devem ser colocados na pasta `data/input`.

Após a execução, os relatórios são gerados automaticamente na pasta `data/output`.

---

## Possíveis Evoluções

* [ ] Validação oficial de CNPJ utilizando os dígitos verificadores
* [ ] Suporte ao XML oficial da NF-e com namespaces
* [ ] Leitura de arquivos SPED Fiscal
* [ ] Cruzamento entre XML e SPED
* [ ] Dashboard para acompanhamento das validações
* [ ] Utilização de Pandas para análise dos resultados

---

## Autor

**Fábio Oliveira**

Estudante de Ciências Contábeis – FIPECAFI
