# Rubik's Cube Solver

[Português](README.md) | [English](README.en.md)

A personal project to study and build a 3×3 Rubik's Cube solver in Python, step by step. The goal is to understand the mathematics and implement the main parts without relying on a ready-made solving library.

## Idea

- Represent the cube as 54 stickers.
- Build moves using coordinates in R³ and rotation matrices.
- Convert rotations into permutations that can be applied to the 54-position vector.
- Validate the moves, then use search and heuristics to find solutions.

## Current status

The project is at an early stage. `rubikscube.ipynb` contains the initial cube representation and a first implementation of the U move. Geometric move generation and the solver are still to be developed.

## Getting started

Install the dependencies listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

In Jupyter or Google Colab, you can also run this in a notebook cell:

```python
%pip install -r requirements.txt
```

Then open `rubikscube.ipynb`. The notebook uses NumPy for coordinates and Matplotlib for the 3D visualization.

## Study plan

1. Define coordinates and orientations for all six faces.
2. Generate moves geometrically and compare their permutations.
3. Add checks for move properties.
4. Develop a solver using search and heuristics.
5. Explore computer vision as a future step.

This project is also a study of linear algebra, geometry, group theory, and search. The plan may change as the project develops.
