# 🏭 Sistema de Gestão de Peças Industriais

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de **Algoritmos e Lógica de Programação**, com o objetivo de simular um sistema de automação industrial para controle de qualidade de peças.

O sistema realiza a validação automática das peças produzidas, classificando-as como **aprovadas** ou **reprovadas**, além de organizar o armazenamento em caixas e gerar relatórios detalhados.

---

## 🎯 Objetivo

Automatizar o processo de inspeção de peças, reduzindo erros humanos, aumentando a eficiência e melhorando o controle de produção.

---

## ⚙️ Funcionalidades

* ✅ Cadastro de peças (ID, peso, cor e comprimento)
* ✅ Validação automática com base em critérios de qualidade
* ✅ Identificação do motivo de reprovação
* ✅ Armazenamento automático em caixas (máximo de 10 peças)
* ✅ Fechamento automático de caixas
* ✅ Listagem de peças aprovadas e reprovadas
* ✅ Remoção de peças por ID
* ✅ Geração de relatório final

---

## 📏 Regras de Validação

Uma peça será considerada **APROVADA** somente se atender aos seguintes critérios:

* Peso entre **95g e 105g**
* Cor **azul** ou **verde**
* Comprimento entre **10cm e 20cm**

Caso contrário, será considerada **REPROVADA**, informando o(s) motivo(s).

---

## 📦 Sistema de Caixas

* Apenas peças aprovadas são armazenadas
* Cada caixa suporta até **10 peças**
* Ao atingir o limite, a caixa é automaticamente fechada
* Uma nova caixa é iniciada automaticamente

---

## 📊 Relatório Final

O sistema gera um relatório contendo:

* Total de peças aprovadas
* Total de peças reprovadas
* Motivos de reprovação
* Quantidade de caixas utilizadas

---

## ▶️ Como Executar o Projeto

### 🔧 Pré-requisitos

* Ter o **Python** instalado (versão 3 ou superior)

### 🚀 Passo a passo

1. Clone este repositório:

```
git clone https://github.com/seuusuario/sistema-gestao-pecas.git
```

2. Acesse a pasta do projeto:

```
cd sistema-gestao-pecas
```

3. Execute o programa:

```
python main.py
```

---

## 💻 Exemplo de Uso

### Entrada:

```
ID: 001
Peso: 100
Cor: azul
Comprimento: 15
```

### Saída:

```
Peça cadastrada com sucesso!
Status: Aprovada
```

---

## 🧠 Lógica Utilizada

O sistema foi desenvolvido utilizando:

* Estruturas condicionais (`if/else`) para validação
* Estruturas de repetição (`while`) para o menu interativo
* Funções para modularização do código
* Listas para armazenamento de dados

---

## 🚧 Desafios Encontrados

* Garantir a validação correta dos dados
* Controlar o limite de peças por caixa
* Organizar os dados de forma clara para o relatório

---

## 🚀 Possíveis Melhorias Futuras

* Integração com banco de dados (SQLite)
* Interface gráfica (GUI)
* Integração com sensores industriais
* Uso de Inteligência Artificial para análise de qualidade

---

## 👨‍💻 Autor

Desenvolvido por **[Seu Nome Aqui]**

---

## 📎 Licença

Este projeto é acadêmico e não possui fins comerciais.
