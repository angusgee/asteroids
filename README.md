# Asteroids Game

A classic arcade-style Asteroids game implemented in Python using Pygame.

## Game Description

In this game, you control a spaceship navigating through an asteroid field. Your objective is to survive as long as possible by avoiding collisions with asteroids and shooting them to clear your path.

## Features

- Player-controlled spaceship with rotation and thrust mechanics
- Shooting mechanism to destroy asteroids
- Asteroid splitting system:
  - Large asteroids split into two medium asteroids when shot
  - Medium asteroids split into two small asteroids when shot
  - Small asteroids disappear when shot
- Randomly generated asteroid field with increasing difficulty
- Physics-based movement and collision detection

## Controls

- **A/D**: Rotate the spaceship left and right
- **W/S**: Move forward and back
- **Space Bar**: Fire bullets

## Requirements

- Python 3.x
- Pygame

## Installation

1. Ensure you have Python installed on your system
2. Install Pygame:

```
pip install pygame
```

## How to Run

Navigate to the game directory and run:

```
python main.py
```

## Game Components

- **main.py**: Main game loop and collision detection
- **player.py**: Player spaceship class
- **asteroid.py**: Asteroid class with splitting functionality
- **shot.py**: Bullet class
- **circleshape.py**: Base class for circular objects
- **constants.py**: Game constants and settings
- **asteroidfield.py**: Handles asteroid generation

## Game Mechanics

### Asteroid Splitting

When a bullet hits an asteroid:
1. Large asteroids split into two medium-sized asteroids
2. Medium asteroids split into two small asteroids
3. Small asteroids are destroyed without splitting

The new asteroids move in different directions at increased speeds, making the game progressively more challenging as you destroy larger asteroids.

