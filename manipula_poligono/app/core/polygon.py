from __future__ import annotations

from math import cos, pi, sin, tau

from app.core.state import MIN_VERTEX_COUNT


def generate_regular_vertices(
    center: tuple[float, float], radius: float, sides: int
) -> list[tuple[float, float]]:
    if sides < MIN_VERTEX_COUNT:
        raise ValueError(f"Polygon must have at least {MIN_VERTEX_COUNT} vertices.")
    if radius <= 0.0:
        raise ValueError("Polygon radius must be positive.")

    cx, cy = center
    # O primeiro vertice fica no topo e os demais avancam com o mesmo passo angular.
    start_angle = pi / 2.0
    step = tau / sides

    # Cada par (cos, sin) projeta um vertice do poligono regular ao redor do centro.
    return [
        (
            cx + radius * cos(start_angle + index * step),
            cy + radius * sin(start_angle + index * step),
        )
        for index in range(sides)
    ]
