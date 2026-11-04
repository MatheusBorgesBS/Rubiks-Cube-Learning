# Rubik's Cube Solver

[Português](README.md) | [English](README.en.md)

Projeto pessoal para estudar e construir, passo a passo, um solver de cubo mágico 3×3 em Python. O objetivo é entender a matemática e implementar as partes principais, sem depender de uma biblioteca pronta de resolução.

## Ideia

- Representar o cubo como 54 adesivos.
- Construir os movimentos usando coordenadas em R³ e matrizes de rotação.
- Converter as rotações em permutações aplicáveis ao vetor de 54 posições.
- Validar os movimentos e, depois, usar busca e heurísticas para encontrar soluções.

## Estado atual

O projeto está no início. `rubikscube.ipynb` contém a representação inicial do cubo e uma primeira implementação do movimento U. A construção geométrica dos movimentos e o solver ainda estão por fazer.

## Como começar

Instale as dependências listadas em `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

No Jupyter ou Google Colab, você também pode executar em uma célula:

```python
%pip install -r requirements.txt
```

Depois, abra `rubikscube.ipynb`. O notebook usa NumPy.

## Plano de estudo

1. Definir as coordenadas e orientações das seis faces.
2. Gerar movimentos geometricamente e conferir suas permutações.
3. Implementar testes para as propriedades dos movimentos.
4. Desenvolver um solver com busca e heurísticas.
5. Explorar visão computacional como etapa futura.

Este projeto é também um estudo de álgebra linear, geometria, teoria de grupos e busca. As etapas podem mudar conforme o aprendizado.
