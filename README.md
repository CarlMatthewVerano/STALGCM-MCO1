# STALGCM-MCO1
HOW TO USE APPLICATION

Input Format:
The input to the deterministic one-counter automaton consists of the following components:
- Number of states
- List of states
- Number of input symbols
- Alphabet
- Number of transitions
- Transitions(current_state key input next_state transition_action)
  *Note: key means if the counter is zero or nonzero
  *Note: transition_action means if whether the counter will decrement, do nothing, or increment {-1, 0, 1}
- Start_state
- Number of accept states
- List of accept states

Output Format:
The deterministic one-counter automaton processes the input string provided to it using the defined transitions and rules. After processing the input, it produces a binary output indicating whether the input string is accepted or not. In other words, the output is a boolean value: ‘True’ if the input is accepted, and ‘False’ if the input is rejected.

Operation of the machine
The machine starts processing the input string from its start state. For each character in the input string, it checks the transition table to determine the next state and the action to be performed on the counter. The transition table contains entries in the form of ‘(input_symbol, is_zero)’, where ‘input_symbol’ represents the character being read from the input, and ‘is-zero’ is a binary value indicating the counter is zero or non-zero.

Based on the current state, the input symbol, and the value of the counter, the machine looks up the transition table to find the appropriate transition to the next state and the counter action to be performed. The counter can be incremented, decremented, or remain unchanged. If the counter goes negative during the processing of the input, the automaton rejects the input string.

After processing the entire input string, the machine checks whether it has reached an accept state and if the counter is zero. If both conditions are met, the input string is accepted; otherwise, it is rejected.

Testing the automaton:
Firstly, the user has to input test strings to the textbox in the GUI. Then they proceed to choosing a file using the ‘read_one_counter_file’ function; wherein the text chosen should contain the components of the deterministic one-counter automata. For each test string, it calls the ‘input_process’ method of the machine and prints the step-by-step procedure of each transition from the input then shows whether the input string is accepted or not accepted.


As a sample, take for example diagram_sample.txt
To run a sample simulation, the user first has to input the test strings, which are: {00, 11, 12, 012, 00112, 22, 120}. To input it in the input box, follow this format: "00, 11, 12, 012, 00112, 22, 120" (disregard the quotation marks).After inputting these test strings to the input box in the GUI, the user has to choose a file by clicking the button above said input box. After which the application will automatically run once a file has been chosen and will do simulations on the test strings.