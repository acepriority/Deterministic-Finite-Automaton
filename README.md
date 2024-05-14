# Deterministic-Finite-Automaton

This project implements a Deterministic Finite Automaton (DFA) in Python. The DFA processes input strings to determine whether they are accepted by the defined automaton.

## DFA Class

The `DFA` class represents a deterministic finite automaton. It includes methods to initialize the DFA and process input strings.

### Attributes

- `states`: A set of states in the DFA.
- `alphabet`: The alphabet (set of input symbols) the DFA operates on.
- `start_state`: The start state of the DFA.
- `accept_states`: The set of accepting states of the DFA.
- `transition_function`: A dictionary representing the transition function.
- `current_state`: The current state of the DFA during processing.

### Methods

- `__init__()`: Initializes the DFA with states, alphabet, start state, accept states, and transition function.
- `process(input_string)`: Processes an input string to determine if it is accepted by the DFA. Returns `True` if the string is accepted, `False` otherwise.

## Test Class

The `Test` class inherits from the `DFA` class and is used to test the DFA with given input strings.

### Methods

- `__init__()`: Initializes the Test class by inheriting from the DFA class.
- `test(input_string)`: Tests the DFA with a given input string and prints whether the string is accepted or rejected.

## Example Usage

```python
states = {'A', 'B', 'C'}
alphabet = {'0', '1'}
start_state = 'A'
accept_states = {'C'}
transition_function = {
    ('A', '0'): 'B',
    ('A', '1'): 'A',
    ('B', '0'): 'B',
    ('B', '1'): 'C',
    ('C', '0'): 'B',
    ('C', '1'): 'A'
}

input_string = '01001101'

Test().test(input_string)
```

In this example, the DFA is defined with states A, B, and C, an alphabet consisting of 0 and 1, a start state A, accept states {C}, and a transition function that defines state transitions based on input symbols. The input string 01001101 is tested against this DFA to determine if it is accepted.

To run the code, simply execute the Python script. The output will indicate whether the input string is accepted or rejected by the DFA.
