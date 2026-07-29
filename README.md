# Sistema de Gerenciamento de Treinos

Sistema desenvolvido em **Python** utilizando **Programação Orientada a Objetos (POO)** para gerenciar treinos de academia.

O projeto simula um sistema utilizado por uma academia para organizar treinos personalizados, validar regras de negócio e calcular o gasto calórico de diferentes modalidades de exercícios.

---

## Sobre o Projeto

A academia **PowerFit** deseja substituir o controle manual dos treinos por um sistema capaz de organizar os treinos dos alunos e automatizar o cálculo de calorias.

Cada tipo de treino possui sua própria forma de cálculo, permitindo que o sistema seja facilmente expandido com novos tipos de exercícios.

O projeto foi desenvolvido aplicando conceitos fundamentais de Programação Orientada a Objetos.

---

## Funcionalidades

- Cadastro de alunos.
- Cadastro de treinos.
- Treinos de Força.
- Treinos Cardio.
- Treinos de Flexibilidade.
- Cálculo automático das calorias.
- Cálculo do nível de dificuldade.
- Plano semanal contendo vários treinos.
- Soma das calorias gastas durante a semana.
- Registro de histórico dos treinos cardio.
- Validação de regras de negócio.

---

## Regras de Negócio

O sistema segue as seguintes regras:

- O cálculo de calorias depende do tipo de treino.
- Treinos de força utilizam peso levantado e número de séries.
- Treinos cardio utilizam duração e intensidade.
- Treinos de flexibilidade possuem baixo gasto calórico e cálculo de ganho de mobilidade.
- Um aluno com menos de **1 mês de matrícula** não pode realizar treinos classificados como **Avançado**.
- Um plano semanal pode conter diversos treinos.
- O sistema calcula automaticamente o total de calorias da semana.

---

# Conceitos de POO Aplicados

### Classe Abstrata

A classe `Treino` define a estrutura básica de todos os treinos.

Ela possui dois métodos abstratos:

- `calcular_calorias()`
- `nivel_dificuldade()`

---

### Herança

As classes

- `TreinoForca`
- `TreinoCardio`
- `TreinoFlexibilidade`

herdam da classe `Treino`.

---

### Herança Múltipla

A classe `TreinoCardio` herda de:

- `Treino`
- `Monitoramento`

permitindo registrar o histórico das execuções dos treinos.

---

### Polimorfismo

Cada tipo de treino implementa seu próprio cálculo de calorias e nível de dificuldade.

Exemplo:

```python
for treino in plano.treinos:
    print(treino.calcular_calorias())
```

O mesmo método produz resultados diferentes dependendo do tipo de treino.

---

### Encapsulamento

Todos os atributos foram implementados como privados utilizando:

- `__atributo`

e acessados através de:

- `@property`
- `@setter`

---

### Collections

Foi utilizada uma lista (`list`) para armazenar todos os treinos cadastrados no plano semanal.

---

# Como Executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/academia.git
```

Entre na pasta:

```bash
cd academia
```

Execute:

```bash
python main.py
```

---

# Exemplo de Saída

```text
========================================
=== Aluno ===
Nome: João Pedro
Meses de matrícula: 12
========================================

Verificando treinos...

TreinoForca: Treino permitido.
TreinoCardio: Treino permitido.
TreinoFlexibilidade: Treino permitido.

=== Plano Semanal ===

1. TreinoForca
   Duração: 60 minutos
   Dificuldade: Avançado
   Calorias: 48.00 kcal

2. TreinoCardio
   Duração: 30 minutos
   Dificuldade: Intermediário
   Calorias: 1440.00 kcal

3. TreinoFlexibilidade
   Duração: 45 minutos
   Dificuldade: Avançado
   Calorias: 90.00 kcal

Quantidade de treinos: 3

Total de calorias: 1578.00 kcal
```

---

# Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos (POO)
- Módulos
- Classes Abstratas (`abc`)
- Herança
- Herança Múltipla
- Encapsulamento
- Polimorfismo

---

# Autores

- **João Vitor Gomes Tatsch | Nº8**
- **João Pedro Rangel | Nº7**
- **Guilherme Silva Dranka | Nº5**
- **Diego Luiz Bernal | Nº4**

---

# Instrutor

- **Henrique Daniel da Rocha**
