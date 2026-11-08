"""Representação do cubo, movimentos geométricos e visualização."""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import re 
import random


ORDEM_FACES = ("U", "L", "F", "R", "B", "D")
INICIO_FACE = {face: 9 * indice for indice, face in enumerate(ORDEM_FACES)}

coordenadas_U = np.empty((3, 3, 3), dtype=int)
coordenadas_L = np.empty((3, 3, 3), dtype=int)
coordenadas_F = np.empty((3, 3, 3), dtype=int)
coordenadas_R = np.empty((3, 3, 3), dtype=int)
coordenadas_B = np.empty((3, 3, 3), dtype=int)
coordenadas_D = np.empty((3, 3, 3), dtype=int)

for linha in range(3):
    for coluna in range(3):
        coordenadas_U[linha, coluna] = (linha - 1, 1 - coluna, 1)
        coordenadas_L[linha, coluna] = (coluna - 1, 1, 1 - linha)
        coordenadas_F[linha, coluna] = (1, 1 - coluna, 1 - linha)
        coordenadas_R[linha, coluna] = (1 - coluna, -1, 1 - linha)
        coordenadas_B[linha, coluna] = (-1, coluna - 1, 1 - linha)
        coordenadas_D[linha, coluna] = (1 - linha, 1 - coluna, -1)

faces_3d = [
    (0,  coordenadas_U, (1, 0, 0),  (0, -1, 0), (0, 0, 1)),
    (9,  coordenadas_L, (0, 0, -1), (1, 0, 0),  (0, 1, 0)),
    (18, coordenadas_F, (0, 0, -1), (0, -1, 0), (1, 0, 0)),
    (27, coordenadas_R, (0, 0, -1), (-1, 0, 0), (0, -1, 0)),
    (36, coordenadas_B, (0, 0, -1), (0, 1, 0),  (-1, 0, 0)),
    (45, coordenadas_D, (-1, 0, 0), (0, -1, 0), (0, 0, -1)),
]

cores_plot = {
    "W": "white",
    "G": "green",
    "R": "red",
    "B": "blue",
    "O": "orange",
    "Y": "yellow",
}
cores_plot_ids = {
    "0": "white",
    "1": "green",
    "2": "red",
    "3": "blue",
    "4": "orange",
    "5": "yellow",
}
def print_cubo(cubo):
    c = np.array(cubo, dtype=str)

    U = c[0:9].reshape(3, 3)
    L = c[9:18].reshape(3, 3)
    F = c[18:27].reshape(3, 3)
    R = c[27:36].reshape(3, 3)
    B = c[36:45].reshape(3, 3)
    D = c[45:54].reshape(3, 3)

    espaço = "       "

    for i in range(3):
        print(f"{espaço}{U[i,0]} {U[i,1]} {U[i,2]}")

    print()

    for i in range(3):
        linha_L = f"{L[i,0]} {L[i,1]} {L[i,2]}"
        linha_F = f"{F[i,0]} {F[i,1]} {F[i,2]}"
        linha_R = f"{R[i,0]} {R[i,1]} {R[i,2]}"
        linha_B = f"{B[i,0]} {B[i,1]} {B[i,2]}"
        print(f"{linha_L}  {linha_F}  {linha_R}  {linha_B}")

    print()

    for i in range(3):
        print(f"{espaço}{D[i,0]} {D[i,1]} {D[i,2]}")


def plotar_cubo(cubo, elev=25, azim=-55, ax=None, ids=False):

    cubo = np.asarray(cubo)

    if cubo.shape != (54,):
        raise ValueError("O cubo deve ser um vetor de 54 adesivos.")

    # Select the appropriate color dictionary
    cores = cores_plot_ids if ids else cores_plot

    if ax is None:
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111, projection="3d")

    # Camera direction
    a = np.radians(azim)
    e = np.radians(elev)

    camera = np.array([
        np.cos(e) * np.cos(a),
        np.cos(e) * np.sin(a),
        np.sin(e)
    ])

    quadrados = []
    cores = []

    for inicio, grade, direcao_linha, direcao_coluna, normal in faces_3d:

        vl = np.asarray(direcao_linha, dtype=float)
        vc = np.asarray(direcao_coluna, dtype=float)
        n = np.asarray(normal, dtype=float)

        # Hide faces opposite to the camera
        if np.dot(n, camera) <= 0:
            continue

        for linha in range(3):
            for coluna in range(3):

                centro = grade[linha, coluna].astype(float)
                centro = centro + 0.5 * n

                tamanho = 0.46

                cantos = [
                    centro - tamanho*vl - tamanho*vc,
                    centro - tamanho*vl + tamanho*vc,
                    centro + tamanho*vl + tamanho*vc,
                    centro + tamanho*vl - tamanho*vc,
                ]

                quadrados.append(cantos)

                valor = cubo[inicio + 3*linha + coluna]

                if ids:
                    # Sticker ID -> original face ID
                    valor = int(valor) // 9

                cor = (
                    cores_plot_ids[str(valor)]
                    if ids
                    else cores_plot[str(valor)]
                )

                cores.append(cor)

    adesivos = Poly3DCollection(
        quadrados,
        facecolors=cores,
        edgecolors="#111111",
        linewidths=2
    )

    ax.add_collection3d(adesivos)

    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_zlim(-1.6, 1.6)

    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=elev, azim=azim)

    ax.set_axis_off()
    ax.set_proj_type("ortho")

    return ax



def girar_cubo(cubo, mapa_de_permutacao):
    return cubo[mapa_de_permutacao]


def gerar_mapa_movimento(nome_face):
    """
    Gera um mapa para usar como cubo_novo = cubo[mapa].

    nome_face escolhe a camada e define o sentido horário visto de fora.
    """
    nome_face = nome_face.upper()
    inicio_alvo = INICIO_FACE[nome_face]
    face_alvo = next(face for face in faces_3d if face[0] == inicio_alvo)
    _, _, direcao_linha, direcao_coluna, normal_camada = face_alvo

    # Coordenadas locais: linha, coluna, normal. A rotação gira
    # a grade 90 graus no sentido horário quando vista de fora da face.
    base = np.column_stack((direcao_linha, direcao_coluna, normal_camada))
    giro_local = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
    matriz_rotacao = base @ giro_local @ base.T
    n_camada = np.array(normal_camada, dtype=int)
    # Relaciona cada posição e orientação de adesivo ao índice no vetor.
    indice_por_geometria = {}

    for inicio, grade, direcao_linha, direcao_coluna, normal in faces_3d:
        normal_adesivo = tuple(normal)

        for linha in range(3):
            for coluna in range(3):
                indice = inicio + 3 * linha + coluna
                posicao = tuple(int(x) for x in grade[linha, coluna])
                indice_por_geometria[(posicao, normal_adesivo)] = indice

    mapa = np.empty(54, dtype=int)

    for inicio, grade, direcao_linha, direcao_coluna, normal in faces_3d:
        n_adesivo = np.array(normal, dtype=int)

        for linha in range(3):
            for coluna in range(3):
                origem = inicio + 3 * linha + coluna
                posicao = np.array(grade[linha, coluna], dtype=int)

                # O produto escalar igual a 1 seleciona a camada externa.
                if np.dot(posicao, n_camada) == 1:
                    nova_posicao = matriz_rotacao @ posicao
                    nova_normal = matriz_rotacao @ n_adesivo
                else:
                    nova_posicao = posicao
                    nova_normal = n_adesivo

                chave_destino = (
                    tuple(int(x) for x in nova_posicao),
                    tuple(int(x) for x in nova_normal),
                )
                destino = indice_por_geometria[chave_destino]

                # girar_cubo usa cubo[mapa]:
                # em cada destino, guardamos o índice de origem.
                mapa[destino] = origem

    return mapa


faces = ORDEM_FACES
mapas_movimentos = {}

for face in faces:
    mapa = gerar_mapa_movimento(face)
    mapas_movimentos[face] = mapa
    mapas_movimentos[face + "'"] = np.argsort(mapa)
    mapas_movimentos[face + "2"] = mapa[mapa]



def scramble(moves, estado):
    all_moves = re.findall(r"[ULFRBD](?:2|')?", moves)

    for move in all_moves:
        estado = girar_cubo(estado, mapas_movimentos[move])

    return estado



def scramble_aleatorio(estado, n=int):

    movimentos = list(mapas_movimentos.keys())
    ultimo_movimento = None
    sequencia = []

    for _ in range(n):

        opcoes = [move for move in movimentos if move[0] != ultimo_movimento]

        move = random.choice(opcoes)

        sequencia.append(move)

        estado = girar_cubo(estado,mapas_movimentos[move])

        ultimo_movimento = move[0]

    return estado, sequencia
        
