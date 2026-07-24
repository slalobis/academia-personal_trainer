# 🏋️ Sistema de Gerenciamento de Treinos em Python

## 📖 Sobre o projeto

Este projeto consiste em um sistema orientado a objetos para gerenciamento de treinos de academia, desenvolvido em **Python**. O sistema permite cadastrar alunos, controlar planos semanais de treino e calcular o gasto calórico de diferentes modalidades de exercícios.

O objetivo do projeto é demonstrar a aplicação dos principais conceitos de **Programação Orientada a Objetos (POO)**, como abstração, herança, polimorfismo, encapsulamento e composição.

---

## 🚀 Funcionalidades

* Cadastro de alunos.
* Cadastro de três tipos de treino:

  * Treino de Força;
  * Treino Cardio;
  * Treino de Flexibilidade.
* Classificação dos treinos por nível:

  * Iniciante;
  * Intermediário;
  * Avançado.
* Controle de acesso aos treinos conforme o tempo de matrícula do aluno.
* Limite máximo de **5 treinos por semana**.
* Cálculo das calorias gastas por treino.
* Cálculo do total semanal de calorias.
* Cálculo do ganho de mobilidade para treinos de flexibilidade.
* Exibição do plano semanal do aluno.

---

## 📂 Estrutura do projeto

```
Treino (Classe Abstrata)
│
├── TreinoForca
├── TreinoCardio
└── TreinoFlexibilidade

PlanoSemanal

Aluno
```

---

## 🧠 Conceitos de Programação Orientada a Objetos utilizados

### Classe Abstrata

A classe `Treino` funciona como uma base para todos os tipos de treino, impedindo sua instanciação direta e obrigando as subclasses a implementarem o método:

```python
calcular_calorias()
```

---

### Herança

As classes:

* `TreinoForca`
* `TreinoCardio`
* `TreinoFlexibilidade`

herdam os atributos e comportamentos da classe `Treino`.

---

### Polimorfismo

Cada tipo de treino implementa o método `calcular_calorias()` de maneira diferente.

Exemplo:

* Força → depende do peso levantado e do número de séries.
* Cardio → depende do tempo e da intensidade.
* Flexibilidade → depende apenas do tempo.

---

### Encapsulamento

Cada classe é responsável por armazenar e manipular seus próprios dados, mantendo a organização do sistema.

---

### Composição

A classe `Aluno` possui um objeto `PlanoSemanal`, que é responsável por armazenar todos os treinos do aluno.

---

## 📋 Regras do sistema

### Níveis permitidos

* Iniciante
* Intermediário
* Avançado

Caso um nível inválido seja informado, o sistema gera uma exceção (`ValueError`).

---

### Restrições por tempo de matrícula

| Tempo matriculado | Treinos permitidos        |
| ----------------- | ------------------------- |
| Menos de 1 mês    | Apenas Iniciante          |
| Entre 1 e 3 meses | Iniciante e Intermediário |
| 3 meses ou mais   | Todos os níveis           |

---

### Limite semanal

Cada aluno pode cadastrar no máximo **5 treinos** por semana.

Caso tente adicionar um sexto treino, o sistema exibe uma mensagem informando que o limite foi atingido.

---

## 🔥 Cálculo de calorias

### Treino de Força

```
Calorias = Peso × Séries × 0.15
```

---

### Treino Cardio

```
Calorias = Tempo × Intensidade × 8
```

---

### Treino de Flexibilidade

```
Calorias = Tempo × 2
```

Além disso:

```
Mobilidade = Tempo × 1.5
```

---

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do projeto.

3. Execute o arquivo Python:

```bash
python nome_do_arquivo.py
```

---

## 💻 Exemplo de execução

Durante a execução, o programa:

* cria dois alunos (`Carlos` e `Ana`);
* cria treinos de diferentes modalidades e níveis;
* valida se o aluno pode realizar determinado treino;
* impede a inclusão de treinos acima do nível permitido;
* limita o plano semanal a cinco treinos;
* exibe o plano semanal com as calorias gastas e o total da semana.

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Programação Orientada a Objetos (POO)

---

## 📌 Objetivo acadêmico

Este projeto foi desenvolvido com fins de estudo para praticar conceitos fundamentais de Programação Orientada a Objetos em Python, incluindo:

* Classes e Objetos;
* Classes Abstratas (`ABC`);
* Métodos Abstratos;
* Herança;
* Polimorfismo;
* Encapsulamento;
* Composição;
* Validação de regras de negócio.

---

## 👨‍💻 Autores

João Pedro Rangel
João Vitor Gomes
Guilherme Silva Dranka
Diego Luiz Bernal
