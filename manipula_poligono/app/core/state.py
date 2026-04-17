from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

Color = tuple[float, float, float]

# Paleta fixa usada para alternar as cores por indice circular.
PALETTE: tuple[Color, ...] = (
    (1.0, 0.0, 0.0),  # red
    (0.0, 1.0, 0.0),  # green
    (0.0, 0.0, 1.0),  # blue
    (1.0, 1.0, 0.0),  # yellow
    (1.0, 0.0, 1.0),  # magenta
    (0.0, 1.0, 1.0),  # cyan
    (1.0, 1.0, 1.0),  # white
    (0.0, 0.0, 0.0),  # black
)

# Esses limites controlam as variacoes permitidas para o poligono.
MIN_VERTEX_COUNT = 3
MAX_VERTEX_COUNT = 12
MOVE_STEP = 0.05
MIN_LINE_WIDTH = 1.0
MAX_LINE_WIDTH = 10.0
LINE_WIDTH_STEP = 1.0


class DisplayMode(Enum):
    FILLED = "filled"
    OUTLINE = "outline"


# O estado concentra os atributos geometricos e visuais usados no desenho.
@dataclass(frozen=True, slots=True)
class PolygonState:
    vertex_count: int = 5
    x: float = 0.0
    y: float = 0.0
    radius: float = 0.30
    fill_color_index: int = 2
    border_color_index: int = 7
    line_width: float = 2.0
    display_mode: DisplayMode = DisplayMode.FILLED

    @classmethod
    def initial(cls) -> "PolygonState":
        return cls()

    @property
    def fill_color(self) -> Color:
        # O indice permite percorrer a paleta sem alterar a estrutura do estado.
        return PALETTE[self.fill_color_index % len(PALETTE)]

    @property
    def border_color(self) -> Color:
        # A borda usa a mesma paleta, mas com indice independente do preenchimento.
        return PALETTE[self.border_color_index % len(PALETTE)]
