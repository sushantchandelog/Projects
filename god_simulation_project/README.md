# A Computational Critique of a Karma-Based Hierarchy

This project uses an abstract, agent-based simulation in Python to explore the internal logic, ethical consequences, and philosophical fallacies of a Varna-like system governed by the principles of karma and reincarnation.

Rather than debating the system purely through text, this simulation acts as a "logical laboratory" to test its claims. The core of the project is a series of controlled experiments—a "Just Universe" (Null Hypothesis) and several "Stress Tests"—designed to isolate the mechanics of injustice. The primary finding is that such a system is inherently designed to create and perpetuate inequality, regardless of its starting conditions.

## The Philosophical Premise

The simulation was designed to investigate several core logical problems within the karma/reincarnation framework:

* **The Genesis Paradox:** How can the very first generation of humans be assigned a Varna based on past-life karma if they have no past lives? This points to an arbitrary, non-karmic origin for the entire system.
* **The Paradox of Systemic Injustice:** If a system has even slightly biased rules, can a fair start (e.g., all souls beginning as equals) prevent the eventual rise of a rigid, unjust hierarchy?
* **The Paradox of Soul Conservation:** If souls are eternal and reincarnate in a closed loop, how can a world's population grow? This requires the invention of untestable metaphysical constructs.

## The Simulation Model

The project uses an abstract, non-spatial model. Agents do not exist on a physical grid but as part of a population governed by a set of metaphysical rules.

* **The World:** A class that manages a population of agents and the passage of time. It is initialized with specific rules for karma and reincarnation for each experiment.
* **The Agents (`Human` class):** Each agent has core properties such as `soul_id`, `varna`, `karma_score`, and `age`. Their existence is defined by these abstract states.
* **Core Mechanics:**
    * **Annual Karma Change:** In each year of their life, an agent's karma score is adjusted based on a random number. This rule is intentionally biased, with higher Varnas having a statistically better chance of gaining good karma than lower Varnas.
    * **Reincarnation:** Upon death, an agent's final karma score is checked against a set of thresholds. This score determines the Varna they are reborn into for their next life.

## How to Run the Experiments

The project is structured as an experimental notebook (`hypothesis_testing.ipynb`). Each cell in the notebook represents a different simulation or "universe," allowing for a clear comparison of results.

### Prerequisites

You will need Python 3 and the following libraries. You can install them via pip:
```bash
pip install pandas matplotlib jupyter
