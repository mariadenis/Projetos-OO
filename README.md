# Criador de figuras geométricas 

Este é um programa interativo para criação e manipulação de figuras geométricas em Python. Ele suporta figuras unidimensionais (pontos e retas) e bidimensionais (retângulos, círculos e triângulos), oferecendo funcionalidades como cálculo de perímetros, áreas e distâncias até a origem.

---

## Estrutura do Projeto

O programa está organizado em um pacote chamado `package.maths`, contendo as seguintes classes:

- `Point`: Representa um ponto no plano cartesiano.
- `Circle`: Representa um círculo.
- `Reta`: Representa uma reta definida por dois pontos.
- `Retangulo`: Representa um retângulo.
- `Triangulo`: Representa um triângulo.

## Funcionalidades

- **Pontos:**
  - Criação de pontos com coordenadas \(x, y\).
  - Cálculo da distância até a origem.

- **Retas:**
  - Criação de retas com base em dois pontos.
  - Cálculo do comprimento da reta.
  - Cálculo da distância entre a reta e a origem.

- **Retângulos:**
  - Criação de retângulos com ponto central, base e altura.
  - Cálculo do perímetro.
  - Cálculo da área.
  - Cálculo da distância do ponto central até a origem.

- **Círculos:**
  - Criação de círculos com ponto central e raio.
  - Cálculo do perímetro.
  - Cálculo da área.
  - Cálculo da distância do centro até a origem.

- **Triângulos:**
  - Criação de triângulos com ponto central, base, altura e comprimentos dos lados.
  - Verificação de existência do triângulo com base nos lados.
  - Classificação do triângulo (Equilátero, Isósceles, Escaleno).
  - Cálculo do perímetro.
  - Cálculo da área.
  - Cálculo da distância do ponto central até a origem.

---

## Requisitos

- **Python 3.8+**
- Não são necessárias dependências externas.
