<h1 align="center">pathfinding</h1>
<p align="center"><img src="https://github.com/t5avish/pathfinding/assets/96640086/cb13e48e-710f-4f9b-8a2a-1e4c3da93d06" /></p>

a simple pathfinding simulation written with Python and Pygame.
the application implements the BFS algorithm to find the shortest path between two points: a character and a treasure chest.

##Requirements
Requires [python](https://www.python.org/downloads/) and [pygame](https://www.pygame.org/) installed locally.


#### install pygame

```bash
$ pip install pygame
```

## Building

```bash
$ cd "directory of project/code"
$ python main.py
```


## Usage / Controls
* ![player](https://github.com/t5avish/pathfinding/assets/96640086/e8226123-ac9a-4126-aea1-8fcd80954fe3) : to place the character (origin point)

* ![chest](https://github.com/t5avish/pathfinding/assets/96640086/2355678e-4b97-4c2d-a352-137f07b70ed5) : to place the treasure chest (destination point)

* ![obstacle](https://github.com/t5avish/pathfinding/assets/96640086/99d6b32d-37cc-45cf-b80b-282863f4803b) : to place an obstacle (the characher cant go throw)

* ![eraser](https://github.com/t5avish/pathfinding/assets/96640086/1170d1e8-fbaf-4e34-a78e-9bc202bdd8bc) : to delete an object from the board

* ![start](https://github.com/t5avish/pathfinding/assets/96640086/7596a583-ae63-4e6c-a906-21baf1fb8f6f) : to start the simulation

* ![reset](https://github.com/t5avish/pathfinding/assets/96640086/9adac719-5a78-4a17-9af1-018713c09cec) : to reset the board (clears all)

## The Algorithm

* **Breadth First Search (BFS)**: A traversal-based algorithm that explores all neighbors of a node before moving on to the next level. Guaranteed to find the shortest path in unweighted graphs.

## Attribution
* graphics : [Ninja Adventure Pack](https://pixel-boy.itch.io/ninja-adventure-asset-pack)