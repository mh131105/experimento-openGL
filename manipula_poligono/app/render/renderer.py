from __future__ import annotations

from OpenGL.GL import (
    GL_COLOR_BUFFER_BIT,
    GL_LINE_LOOP,
    GL_MODELVIEW,
    GL_POLYGON,
    GL_PROJECTION,
    glBegin,
    glClear,
    glClearColor,
    glColor3f,
    glEnd,
    glLineWidth,
    glLoadIdentity,
    glMatrixMode,
    glOrtho,
    glVertex2f,
    glViewport,
)

from app.core.polygon import generate_regular_vertices
from app.core.state import DisplayMode, PolygonState


class PolygonRenderer:
    def __init__(self) -> None:
        self.background_color = (0.08, 0.08, 0.10, 1.0)

    def setup(self) -> None:
        # A cor de fundo e aplicada uma vez antes do primeiro desenho.
        glClearColor(*self.background_color)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def reshape(self, width: int, height: int) -> None:
        safe_width = max(width, 1)
        safe_height = max(height, 1)

        glViewport(0, 0, safe_width, safe_height)
        # A projecao ortografica fixa mantem o plano 2D no intervalo [-1, 1].
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def render(self, state: PolygonState) -> None:
        # Limpa o frame anterior antes de desenhar o estado atual do poligono.
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        vertices = generate_regular_vertices(
            center=(state.x, state.y),
            radius=state.radius,
            sides=state.vertex_count,
        )

        if state.display_mode is DisplayMode.FILLED:
            # No modo preenchido, os vertices formam a area interna da figura.
            glColor3f(*state.fill_color)
            glBegin(GL_POLYGON)
        else:
            # No modo contorno, a espessura afeta apenas a linha externa.
            glLineWidth(state.line_width)
            glColor3f(*state.border_color)
            glBegin(GL_LINE_LOOP)

        # Cada vertice calculado e enviado ao OpenGL na ordem do poligono.
        for vertex_x, vertex_y in vertices:
            glVertex2f(vertex_x, vertex_y)

        glEnd()
