"""
A DFA is a theoretical model of computation used to represent and control a sequence of transitions
between states in response to external inputs. It is characterized by a finite number of states, 
a set of input symbols, a transition function, a start state, and a set of accepting states. 
The DFA processes input strings and determines whether the string belongs to the language 
it recognizes.

Mathematical Definition:
A DFA is a 5-tuple (Q, Σ, δ, q0, F) where:
- Q is a finite set of states.
- Σ is a finite set of symbols called the alphabet.
- δ: Q × Σ → Q is the transition function.
- q0 ∈ Q is the start state.
- F ⊆ Q is the set of accepting (or final) states.

The DFA starts in the start state q0. For each symbol in the input string, it transitions from 
one state to another according to the transition function δ. If, after consuming the entire input 
string, the DFA is in one of the accepting states, the input string is accepted. Otherwise, 
it is rejected.
"""

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


class DFA:
    """
    A class to represent a deterministic finite automaton (DFA).

    Attributes:
    -----------
    states : set
        A set of states in the DFA.
    alphabet : set
        The alphabet (set of input symbols) the DFA operates on.
    start_state : str
        The start state of the DFA.
    accept_states : set
        The set of accepting states of the DFA.
    transition_function : dict
        A dictionary representing the transition function.
    current_state : str
        The current state of the DFA during processing.
    """

    def __init__(self):
        """
        Initialize the DFA with states, alphabet, start state, accept states, and transition function.
        """
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.transition_function = transition_function
        self.current_state = self.start_state

    def process(self, input_string):
        """
        Process an input string to determine if it is accepted by the DFA.

        Parameters:
        -----------
        input_string : str
            The string to be processed by the DFA.

        Returns:
        --------
        bool
            True if the string is accepted by the DFA, False otherwise.
        """
        for symbol in input_string:
            if symbol not in self.alphabet:
                print(f"The symbol {symbol} doesn't belong to the alphabet [0, 1]")
                return False
            self.current_state = self.transition_function.get((self.current_state, symbol), None)
            if self.current_state is None:
                return False
        return self.current_state in self.accept_states


class Test(DFA):
    """
    A class to test the DFA with a given input string.
    """

    def __init__(self):
        """
        Initialize the Test class by inheriting from the DFA class.
        """
        super().__init__()

    def test(self, input_string):
        """
        Test the DFA with a given input string and print the result.

        Parameters:
        -----------
        input_string : str
            The input string to be tested.
        """
        if self.process(input_string):
            print(f'The string "{input_string}" is accepted by the DFA.')
        else:
            print(f'The string "{input_string}" is rejected by the DFA.')


Test().test(input_string)
