# OpenGL Polygon App

Aplicação OpenGL 2D em Python para criação e manipulação de um único polígono regular, com execução principal via Docker + noVNC.

## Requisitos

- Docker
- Docker Compose
- Navegador web

## Controles

| Tecla | Ação |
| --- | --- |
| `N` | Aumenta o número de vértices |
| `M` | Diminui o número de vértices |
| `↑` `↓` `←` `→` | Move o polígono |
| `C` | Muda a cor de preenchimento |
| `V` | Muda a cor da borda |
| `B` | Aumenta a espessura da borda |
| `P` | Alterna entre preenchido e contorno |

## Executar com Docker

Suba o ambiente:

```bash
docker compose up --build
```

Abra a interface gráfica no navegador:

```text
http://localhost:6080
```

O desktop virtual exibirá a janela OpenGL em execução.

## Regras implementadas

- polígono regular com `3..12` vértices;
- posição inicial `(0.0, 0.0)`;
- raio inicial `0.30`;
- preenchimento inicial azul;
- borda inicial preta;
- espessura inicial `2.0`;
- modo inicial `FILLED`;
- movimento com passo `0.05`;
- paleta circular fixa com 8 cores;
- espessura cíclica de `1.0` até `10.0`.

## Artefatos de entrega

- código-fonte comentado;
- relatório em docs/relatorio_atv1cg.pdf;
