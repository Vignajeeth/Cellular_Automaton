# Cellular Automaton

A cellular automaton is a discrete model of computation studied in automata theory. Cellular automata have found application in various areas, including physics, theoretical biology and microstructure modeling.


## What exactly is Cellular Automaton?

A cellular automaton consists of a regular grid of cells, each in one of a finite number of states, such as on and off. The grid can be in any finite number of dimensions. For each cell, a set of cells called its neighborhood is defined relative to the specified cell. An initial state (time t = 0) is selected by assigning a state for each cell. A new generation is created (advancing t by 1), according to some fixed rule (generally, a mathematical function) that determines the new state of each cell in terms of the current state of the cell and the states of the cells in its neighborhood. Typically, the rule for updating the state of cells is the same for each cell and does not change over time, and is applied to the whole grid simultaneously. This repository has most of the famous rules built in it and custom rules can also be fed by making the appropriate changes.


## Usage

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [pygame](https://www.pygame.org/wiki/GettingStarted) and [scipy](https://www.scipy.org/install.html). Clone this repository and run:

```bash
python3 main.py
```

>Click to Toggle Cells. <br>
>Press Spacebar to start/stop. <br>
>Press q to exit the program.

## Visuals

<img src="https://github.com/Vignajeeth/Cellular_Automaton/blob/master/img/gosper_glider_gun_final.gif" width="500" height="500" />


This construct is called the Gosper Glider Gun. It is the first known finite pattern with unbounded growth, found by Bill Gosper in November 1970. Ideally, it would grow infinitely producing gliders at regular intervals but the wrapping of the edges ensures that the gliders would eventually hit the glider gun destroying it.
