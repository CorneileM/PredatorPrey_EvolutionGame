# An evolution-based strategy game

## Status
In progress (very early stages)

## Goal
To build a simple, but challenging game where players guide the evolution of predators hunting prey.

## Brief (preliminary) description of game
At the start, players select predator traits based on the game environment (habitat types) and limited information on prey traits.
The game commences and simulates predator and prey behavior. Predators and prey initially wander through the environment, but predators can lock onto prey trails (if they are fresh enough) and potentially catch them.
Predators have limited energy, and die if they do not catch prey in time, while prey can't leave their prefered habitat for too long.
<br>
<br>
If a player's predators survive a simulation cycle, their surviving predators will generate new predators (offspring) that have a mix of their traits. The surviving prey will also pass on their traits to the next generation.
At the start of each new cycle, the player can also add one extra predator with player-determined traits that they think will be succesful in the next cycle.
<br>
<br>
Each game will be truly unique (unique prey, predator, and habitat traits), with unique emergent properties. The player's goal is to survive for as many cycles as possible by figuring out a stable evolutionary strategy for each cycle.

## Tools used
I'm aiming to build this in Python using simple arrays and a combination of random & directional walker behavior.

## Why?
It's a fun challenge, hopefully with a fun output in the end.
