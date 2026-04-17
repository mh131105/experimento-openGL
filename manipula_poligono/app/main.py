from __future__ import annotations

import sys

from OpenGL.GLUT import (
    GLUT_DOUBLE,
    GLUT_RGB,
    glutCreateWindow,
    glutDisplayFunc,
    glutInit,
    glutInitDisplayMode,
    glutInitWindowPosition,
    glutInitWindowSize,
    glutKeyboardFunc,
    glutMainLoop,
    glutPostRedisplay,
    glutReshapeFunc,
    glutSpecialFunc,
    glutSwapBuffers,
)

from app.core.state import PolygonState
from app.input.keyboard import handle_ascii_key, handle_special_key
from app.render.renderer import PolygonRenderer

WINDOW_TITLE = "OpenGL 2D Polygon"
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720

state = PolygonState.initial()
renderer = PolygonRenderer()


def display_callback() -> None:
    # Cada redisplay usa o estado atual como fonte unica do desenho.
    renderer.render(state)
    glutSwapBuffers()


def reshape_callback(width: int, height: int) -> None:
    renderer.reshape(width, height)


def keyboard_callback(key: bytes, _: int, __: int) -> None:
    global state

    state, changed = handle_ascii_key(state, key)
    if changed:
        # A janela e redesenhada assim que algum atributo muda.
        glutPostRedisplay()


def special_callback(key: int, _: int, __: int) -> None:
    global state

    state, changed = handle_special_key(state, key)
    if changed:
        # As teclas de movimento tambem atualizam a tela imediatamente.
        glutPostRedisplay()


def main() -> None:
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(80, 80)
    glutCreateWindow(WINDOW_TITLE.encode("utf-8"))

    renderer.setup()
    renderer.reshape(WINDOW_WIDTH, WINDOW_HEIGHT)

    # Os callbacks conectam desenho, teclado e redimensionamento ao loop da GLUT.
    glutDisplayFunc(display_callback)
    glutReshapeFunc(reshape_callback)
    glutKeyboardFunc(keyboard_callback)
    glutSpecialFunc(special_callback)
    glutPostRedisplay()
    glutMainLoop()


if __name__ == "__main__":
    main()
