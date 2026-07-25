# Sistema de Gerenciamento de Treinos

Um sistema desenvolvido em **Python** utilizando **Programação Orientada a Objetos (POO)** para gerenciar treinos de academia. O projeto permite cadastrar alunos, controlar planos semanais de treinamento, validar níveis de experiência e calcular o gasto calórico de diferentes modalidades de exercícios.

---

## Índice

* [Sobre o Projeto](#sobre-o-projeto)
* [Funcionalidades](#funcionalidades)
* [Conceitos de POO Aplicados](#conceitos-de-poo-aplicados)
* [Regras de Negócio](#regras-de-negócio)
* [Cálculo das Calorias](#calculo-das-calorias)
* [Como Executar](#como-executar)
* [Exemplo de Saída](#exemplo-de-saída)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Autores](#autores)
* [Instrutor](#instrutor)

---

# Sobre o Projeto

Este projeto simula um sistema de gerenciamento de treinos para a PowerFit Academia, aplicando os principais conceitos da Programação Orientada a Objetos.

Onde cada aluno vai possuir um plano semanal composto por diferentes tipos de treino, respeitando todas as regras de experiência e limites de treinos por semana.

O projeto foi desenvolvido com foco educacional para consolidar conhecimentos de POO em Python.

---

# Funcionalidades

* Cadastro de alunos
* Criação de treinos de diferentes modalidades
* Controle de níveis de dificuldade
* Restrição de treinos conforme o tempo de matrícula
* Limite máximo de treinos semanais
* Cálculo automático de calorias
* Cálculo de ganho de mobilidade para treinos de flexibilidade
* Exibição completa do plano semanal

---

# Conceitos de POO Aplicados

O projeto utiliza diversos conceitos fundamentais da Programação Orientada a Objetos.

### Abstração

A classe abstrata `Treino` define a estrutura comum para todos os tipos de treino e obriga suas subclasses a implementarem o método:

```python
calcular_calorias()
```

---

### Herança

As classes abaixo herdam da classe `Treino`:

* `TreinoForca`
* `TreinoCardio`
* `TreinoFlexibilidade`

Assim, todas compartilham atributos comuns, como o nível do treino.

---

### Polimorfismo

Cada tipo de treino implementa o método `calcular_calorias()` de forma específica.

| Tipo          | Fórmula                 |
| ------------- | ----------------------- |
| Força         | Peso × Séries × 0.15    |
| Cardio        | Tempo × Intensidade × 8 |
| Flexibilidade | Tempo × 2               |

---

### Encapsulamento

Cada classe é responsável por armazenar e manipular seus próprios dados, mantendo a organização e a segurança das informações.

---


# Regras de Negócio

## Níveis disponíveis

* Iniciante
* Intermediário
* Avançado

Caso seja informado um nível inválido, o sistema lança uma exceção (`ValueError`).

---

## Restrições por experiência

| Tempo de matrícula | Treinos permitidos        |
| ------------------ | ------------------------- |
| Menos de 1 mês     | Apenas Iniciante          |
| Entre 1 e 3 meses  | Iniciante e Intermediário |
| 3 meses ou mais    | Todos os níveis           |

---

## Limite semanal

O Limite Semanal como próprio nome diz, é quantidade de treinos que cada aluno pode realizar, sendo no máximo **5 treinos** por semana.

Ao tentar cadastrar um sexto treino, o sistema impede a operação e informa que o limite foi atingido.

---

# Cálculo das Calorias

### Treino de Força

```text
Calorias = Peso × Séries × 0.15
```

### Treino Cardio

```text
Calorias = Tempo × Intensidade × 8
```

### Treino de Flexibilidade

```text
Calorias = Tempo × 2
```

Além disso, os treinos de flexibilidade calculam:

```text
Mobilidade = Tempo × 1.5
```

---

# Como Executar

## Pré-requisitos

* Python 3.10 ou superior

### Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### Acesse a pasta

```bash
cd seu-repositorio
```

### Execute o programa

```bash
python sistema_treinos.py
```

---

# Exemplo de Saída

```text
Treino iniciante adicionado para Diego.
Treino iniciante adicionado para Diego.
Diego não pode realizar treinos intermediários ou avançados.
Diego ainda não pode realizar treinos avançados.
Treino iniciante adicionado para Diego.

==============================
Plano semanal de Diego
==============================

Treino 1: TreinoForca
Nível: iniciante
Calorias: 22.50

Treino 2: TreinoCardio
Nível: iniciante
Calorias: 1200.00

Treino 3: TreinoFlexibilidade
Nível: iniciante
Calorias: 80.00
Ganho de mobilidade: 60.00

------------------------------
Total semanal de calorias: 1302.50
------------------------------
```

---

# Tecnologias Utilizadas

* Python 3
* Programação Orientada a Objetos (POO)
* Módulo `abc` (Abstract Base Classes)

---

# Autores

* João Vitor Gomes | Nº 8
* João Pedro Rangel | Nº 7
* Guilherme Silva Dranka | Nº 5
* Diego Luiz Bernal | Nº 6

---

# Instrutor

* Henrique Daniel da Rocha
