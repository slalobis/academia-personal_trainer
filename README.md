# Sistema de Gerenciamento de Treinos de Academia

Projeto desenvolvido em **Python** utilizando os princípios da **Programação Orientada a Objetos (POO)** para simular o gerenciamento de treinos em uma academia.

O sistema permite cadastrar alunos, criar diferentes modalidades de treino, organizar planos semanais e validar regras de negócio relacionadas ao nível de experiência do aluno.

---

# Objetivos do Projeto

* Aplicar os principais conceitos de Programação Orientada a Objetos;
* Desenvolver um sistema organizado utilizando múltiplas classes;
* Implementar regras de negócio reais para controle de treinos;
* Utilizar abstração, herança, encapsulamento, polimorfismo e interfaces.

---

# Funcionalidades

* Cadastro de alunos;
* Cadastro de instrutores;
* Criação de treinos de força, cardio e flexibilidade;
* Organização dos treinos em uma ficha de treino;
* Controle do plano semanal do aluno;
* Validação do nível de dificuldade dos treinos;
* Restrição de treinos conforme o tempo de matrícula;
* Limite máximo de cinco treinos por semana;
* Cálculo automático de calorias queimadas;
* Cálculo do ganho de mobilidade em treinos de flexibilidade;
* Exibição completa das informações cadastradas.

---

# Conceitos de POO Aplicados

## Abstração

A classe abstrata `Treino` define a estrutura comum para todos os tipos de treino, obrigando suas subclasses a implementarem o método:

* `calcular_calorias()`

---

## Herança

As classes abaixo herdam da classe `Treino`:

* `TreinoForca`
* `TreinoCardio`
* `TreinoFlexibilidade`

Todas compartilham atributos e comportamentos em comum.

---

## Polimorfismo

Cada tipo de treino implementa o método `calcular_calorias()` de maneira diferente, respeitando suas próprias características.

---

## Encapsulamento

Os atributos das classes são privados e acessados através de propriedades (`@property`), garantindo maior segurança e organização dos dados.

---

## Interface

A interface `Avaliavel` define métodos que podem ser implementados pelas classes responsáveis por realizar avaliações relacionadas aos treinos.

---

# Regras de Negócio

## Níveis permitidos

* Iniciante
* Intermediário
* Avançado

Caso seja informado um nível inválido, o sistema lança uma exceção (`ValueError`).

---

## Tempo de matrícula

O aluno somente pode realizar treinos compatíveis com sua experiência:

| Tempo de matrícula | Treinos permitidos        |
| ------------------ | ------------------------- |
| Menos de 1 mês     | Iniciante                 |
| Entre 1 e 3 meses  | Iniciante e Intermediário |
| Acima de 3 meses   | Todos os níveis           |

---

## Limite semanal

Cada aluno pode possuir no máximo **cinco treinos** cadastrados em seu plano semanal.

Caso esse limite seja excedido, o sistema impede o cadastro do novo treino.

---

# Cálculo das Calorias

Cada modalidade possui sua própria forma de cálculo.

### Treino de Força

```text
Calorias = Peso × Séries × Repetições
```

### Treino Cardio

```text
Calorias = Tempo × Intensidade × 8
```

### Treino de Flexibilidade

```text
Calorias = Tempo × 2
```

Além disso:

```text
Mobilidade = Tempo × 1,5
```

---

# Como Executar

## Pré-requisitos

* Python 3.10 ou superior

## Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

## Acesse a pasta

```bash
cd SEU-REPOSITORIO
```

## Execute o projeto

```bash
python main.py
```

---

# Exemplo de Funcionamento

```text
Aluno cadastrado com sucesso.

Treino de Força adicionado ao plano semanal.

Treino Cardio adicionado ao plano semanal.

Plano semanal gerado com sucesso.

Total de calorias calculadas.

Treino de Flexibilidade:
Mobilidade estimada: 45.0
```

---

# Tecnologias Utilizadas

* Python 3
* Programação Orientada a Objetos (POO)

---

# Autores

Projeto desenvolvido como atividade acadêmica para aplicação dos conceitos de Programação Orientada a Objetos em Python.

---

# Licença

Este projeto possui finalidade exclusivamente educacional.
