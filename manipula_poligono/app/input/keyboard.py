from __future__ import annotations

from collections.abc import Callable

from OpenGL.GLUT import GLUT_KEY_DOWN, GLUT_KEY_LEFT, GLUT_KEY_RIGHT, GLUT_KEY_UP

from app.core.actions import (
    cycle_border_color,
    cycle_fill_color,
    cycle_line_width,
    decrement_vertex_count,
    increment_vertex_count,
    move_down,
    move_left,
    move_right,
    move_up,
    toggle_display_mode,
)
from app.core.state import PolygonState

StateAction = Callable[[PolygonState], PolygonState]

# Mapeia as teclas normais para alteracoes diretas dos atributos do poligono.
ASCII_KEYMAP: dict[str, StateAction] = {
    "n": increment_vertex_count,
    "m": decrement_vertex_count,
    "c": cycle_fill_color,
    "v": cycle_border_color,
    "b": cycle_line_width,
    "p": toggle_display_mode,
}

# As teclas especiais controlam o deslocamento do centro no plano.
SPECIAL_KEYMAP: dict[int, StateAction] = {
    GLUT_KEY_LEFT: move_left,
    GLUT_KEY_RIGHT: move_right,
    GLUT_KEY_UP: move_up,
    GLUT_KEY_DOWN: move_down,
}


def _normalize_ascii_key(key: bytes | str) -> str:
    if isinstance(key, bytes):
        return key.decode("utf-8", errors="ignore").lower()
    return str(key).lower()


def handle_ascii_key(
    state: PolygonState, key: bytes | str
) -> tuple[PolygonState, bool]:
    normalized_key = _normalize_ascii_key(key)
    action = ASCII_KEYMAP.get(normalized_key)

    if action is None:
        return state, False

    next_state = action(state)
    return next_state, next_state != state


def handle_special_key(state: PolygonState, key: int) -> tuple[PolygonState, bool]:
    action = SPECIAL_KEYMAP.get(key)

    if action is None:
        return state, False

    next_state = action(state)
    return next_state, next_state != state
