from __future__ import annotations

from dataclasses import replace

from app.core.state import (
    LINE_WIDTH_STEP,
    MAX_LINE_WIDTH,
    MAX_VERTEX_COUNT,
    MIN_LINE_WIDTH,
    MIN_VERTEX_COUNT,
    MOVE_STEP,
    PALETTE,
    DisplayMode,
    PolygonState,
)


def _round_coordinate(value: float) -> float:
    return round(value, 10)


def increment_vertex_count(state: PolygonState) -> PolygonState:
    # O limite superior evita crescimento indefinido da quantidade de vertices.
    next_count = min(state.vertex_count + 1, MAX_VERTEX_COUNT)
    return replace(state, vertex_count=next_count)


def decrement_vertex_count(state: PolygonState) -> PolygonState:
    # Um poligono so continua valido com pelo menos tres vertices.
    next_count = max(state.vertex_count - 1, MIN_VERTEX_COUNT)
    return replace(state, vertex_count=next_count)


def move_left(state: PolygonState) -> PolygonState:
    # O deslocamento e aplicado no centro do poligono, sem alterar sua forma.
    return replace(state, x=_round_coordinate(state.x - MOVE_STEP))


def move_right(state: PolygonState) -> PolygonState:
    return replace(state, x=_round_coordinate(state.x + MOVE_STEP))


def move_up(state: PolygonState) -> PolygonState:
    return replace(state, y=_round_coordinate(state.y + MOVE_STEP))


def move_down(state: PolygonState) -> PolygonState:
    return replace(state, y=_round_coordinate(state.y - MOVE_STEP))


def cycle_fill_color(state: PolygonState) -> PolygonState:
    # O modulo faz a paleta reiniciar depois da ultima cor.
    next_index = (state.fill_color_index + 1) % len(PALETTE)
    return replace(state, fill_color_index=next_index)


def cycle_border_color(state: PolygonState) -> PolygonState:
    # A borda percorre a mesma paleta, mas em um ciclo separado do preenchimento.
    next_index = (state.border_color_index + 1) % len(PALETTE)
    return replace(state, border_color_index=next_index)


def cycle_line_width(state: PolygonState) -> PolygonState:
    # Depois da espessura maxima, o contorno volta para o valor minimo.
    next_width = state.line_width + LINE_WIDTH_STEP
    if next_width > MAX_LINE_WIDTH:
        next_width = MIN_LINE_WIDTH
    return replace(state, line_width=round(next_width, 2))


def toggle_display_mode(state: PolygonState) -> PolygonState:
    # A exibicao alterna entre area preenchida e contorno simples.
    next_mode = (
        DisplayMode.OUTLINE
        if state.display_mode is DisplayMode.FILLED
        else DisplayMode.FILLED
    )
    return replace(state, display_mode=next_mode)
