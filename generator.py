"""Módulo de generación sintética de puntos en dominios cuadrados 2^j.

Provee utilidades reproducibles para generar distribuciones uniformes dentro
de límites espaciales [0, 2^j] x [0, 2^j], orientadas a poblar estructuras
de partición espacial como Quadtrees y validar contra fuerza bruta.
"""

from _future_ import annotations

import argparse
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np


def generate_uniform_points(
    j: int,
    n_points: int,
    seed: int | None = None,
) -> Tuple[np.ndarray, float]:
    """Genera n puntos uniformemente distribuidos en el dominio [0, 2^j] x [0, 2^j].

    Args:
        j: Exponente que determina el lado del dominio cuadrado (U = 2^j).
        n_points: Número total de puntos a generar.
        seed: Semilla para el generador pseudoaleatorio de NumPy (reproducibilidad).

    Returns:
        Una tupla con:
            - np.ndarray de forma (n_points, 2), donde cada fila es [x, y].
            - float representando la longitud del lado del dominio U.

    Raises:
        ValueError: Si j < 0 o n_points <= 0.
    """
    if j < 0:
        raise ValueError(f"El exponente j debe ser >= 0, recibido: {j}")
    if n_points <= 0:
        raise ValueError(f"El número de puntos debe ser > 0, recibido: {n_points}")

    # Calcular dimensión del dominio espacial U = 2^j
    u_side = float(2**j)

    # Inicializar el generador de números aleatorios con la semilla dada
    rng = np.random.default_rng(seed)

    # Generación vectorizada en el intervalo semicerrado [0, u_side)
    points = rng.uniform(low=0.0, high=u_side, size=(n_points, 2))

    return points, u_side


def plot_point_distribution(
    points: np.ndarray,
    u_side: float,
    j: int,
    max_display_points: int = 5000,
) -> None:
    """Renderiza visualmente el conjunto de puntos confinados en el dominio U.

    Args:
        points: Arreglo bidimensional (N, 2) con las coordenadas de los puntos.
        u_side: Longitud del lado del dominio cuadrado (2^j).
        j: Exponente usado en la configuración para la leyenda gráfica.
        max_display_points: Límite de puntos a dibujar para evitar saturar el render.
    """
    total_points = points.shape[0]
    
    # Submuestreo visual si N es masivo para agilizar renderizado
    if total_points > max_display_points:
        indices = np.random.choice(total_points, size=max_display_points, replace=False)
        display_pts = points[indices]
        title_suffix = f" (Muestra visual de {max_display_points} de {total_points:,} pts)"
    else:
        display_pts = points
        title_suffix = f" (N = {total_points:,} pts)"

    fig, ax = plt.subplots(figsize=(7, 7))

    # Graficar puntos generados
    ax.scatter(
        display_pts[:, 0],
        display_pts[:, 1],
        s=8,
        color="#1f77b4",
        alpha=0.6,
        edgecolors="none",
        label="Puntos sintéticos",
    )

    # Dibujar límites del dominio U = 2^j
    ax.set_xlim(-0.05 * u_side, 1.05 * u_side)
    ax.set_ylim(-0.05 * u_side, 1.05 * u_side)

    # Bounding box del dominio formal
    domain_box = plt.Rectangle(
        (0.0, 0.0),
        u_side,
        u_side,
        fill=False,
        edgecolor="#d62728",
        linewidth=2.0,
        linestyle="--",
        label=f"Dominio U = 2^{j} ({u_side:.0f}x{u_side:.0f})",
    )
    ax.add_patch(domain_box)

    # Ajustes de cuadrícula y etiquetas
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.set_xlabel("Coordenada X")
    ax.set_ylabel("Coordenada Y")
    ax.set_title(f"Distribución de Puntos en Dominio Cuadrado{title_suffix}")
    ax.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


def main() -> None:
    """Punto de entrada de línea de comandos para validación rápida."""
    parser = argparse.ArgumentParser(
        description="Generador de puntos sintéticos para pruebas de Quadtree."
    )
    parser.add_argument(
        "-j",
        type=int,
        default=6,
        help="Exponente para el dominio U = 2^j (default: 6 -> 64x64)",
    )
    parser.add_argument(
        "-n",
        "--points",
        type=int,
        default=1000,
        help="Número total de puntos a generar (default: 1000)",
    )
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        default=42,
        help="Semilla aleatoria para reproducibilidad (default: 42)",
    )
    parser.add_argument(
        "--no-plot",
        action="store_true",
        help="Omite el renderizado de la gráfica en pantalla",
    )

    args = parser.parse_args()

    # Generar puntos
    pts, side = generate_uniform_points(j=args.j, n_points=args.points, seed=args.seed)

    print(f"[OK] Generados {pts.shape[0]} puntos.")
    print(f"[OK] Dominio espacial: [0, {side}] x [0, {side}] (j={args.j}).")
    print(f"[OK] Rango X observado: [{pts[:, 0].min():.4f}, {pts[:, 0].max():.4f}]")
    print(f"[OK] Rango Y observado: [{pts[:, 1].min():.4f}, {pts[:, 1].max():.4f}]")

    if not args.no_plot:
        plot_point_distribution(points=pts, u_side=side, j=args.j)


if _name_ == "_main_":
    main()

"""
Instrucciones de Uso Rápido en la Terminal
 * Crear y activar el entorno virtual:
   python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

 * Instalar dependencias:
   pip install -r requirements.txt

 * Ejecutar el generador con parámetros personalizados:
   # Ejemplo: Dominio 2^8 (256x256), 5,000 puntos y semilla 123
python generator.py -j 8 -n 5000 -s 123
"""
