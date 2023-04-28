# CS50 Course - Joshua Knauber

This repository contains my solutions to some of the exercises in the CS50 course. It also contains some additional projects around similar topics.

## Setup

To run the files first create a virtual environment and install the requirements:

```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Classification

### Shopping

From CS50, based on the given csv with shopping data train a KNeighboursClassifier to predict whether a customer will buy a product or not.

The functions to implement were load_data, train_model and evaluate.

## Genetic

### Function

A project to predict a given function using a genetic algorithm.

### Knapsack

A project to solve the knapsack problem using a genetic algorithm.

## Knowledge

### Minesweeper

From CS50, run runner.py to play. The functions add_knowledge, make_safe_move and make_random_move were left to implement.

## Neural Nets

### MNIST

A project to predict numbers from the mnist dataset using a tensorflow. Experiment notes are in the notebook.

### Traffic Signs

From CS50, project to predict categories of traffic signs from the GTSRB dataset. More notes in the README in the folder.

## Optimization

### Crossword

From CS50, project to generate a crossword puzzle with backtracking. The functions to implement were enforce_node_consistency, revise, ac3, assignment_complete, consistent, order_domain_values, select_unassigned_variable and backtrack.

### Sudoku

A project to solve Sudoku with backtracking, implementation under search/sudoku.

## Reinforcement Learning

### Nim

From CS50, project to play Nim against an AI. The functions to implement were get_q_value, update_q_value, best_future_reward and choose_action.

## Search

### Maze

A project to implement different search algorithms from scratch. There are different frontier classes that can be exchanged to use them.

### Sudoku

An attempt to use search algorithms to solve Sudoku. The backtracking implementation is also here.

## Tic Tac Toe

A project to play tic tac toe with minimax players. There is one implementation with and without alpha beta pruning.
