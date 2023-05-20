<h1 align="center">pathfinding</h1>
<p align="center"><img src="https://github.com/t5avish/pathfinding/assets/96640086/f16e2df2-3382-4e5f-95cb-e033230592de" /></p>

a simple pathfinding simulation written with Python and Pygame.
the application implements the BFS algorithm to find the shortest path between two points: a character and a treasure chest.

## Requirements
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
* ![player](https://github.com/t5avish/pathfinding/assets/96640086/04de91da-3f1f-4eef-a855-2d4153107097) : to place the character (origin point)

* ![chest](https://github.com/t5avish/pathfinding/assets/96640086/20dcbb01-10dd-4f18-9b3c-2bd9445fedfe) : to place the treasure chest (destination point)

* ![obstacle](https://github.com/t5avish/pathfinding/assets/96640086/28017897-a1fa-48d5-b607-3f6d72c80609) : to place an obstacle (the character cant go throw)

* ![eraser](https://github.com/t5avish/pathfinding/assets/96640086/8252120f-edfd-4824-a376-c6460831c145) : to delete an object from the board

* ![start](https://github.com/t5avish/pathfinding/assets/96640086/39da304e-7b4d-46c3-8a41-7a96e8ff02c2) : to start the simulation

* ![reset](https://github.com/t5avish/pathfinding/assets/96640086/8f689c84-5546-45cc-b6a4-9b3b97c18224) : to reset the board (clears all)

## The Algorithm

* **Breadth First Search (BFS)**: A traversal-based algorithm that explores all neighbors of a node before moving on to the next level. Guaranteed to find the shortest path in unweighted graphs.

## Attribution
* graphics : [Ninja Adventure Pack](https://pixel-boy.itch.io/ninja-adventure-asset-pack)
