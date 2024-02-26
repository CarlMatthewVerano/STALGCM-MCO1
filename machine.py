# CSALGCM Case Study - One Counter Machine
# Members:
# Gabriel I. Muriel
# Carl Matthew T. Verano


import tkinter as tk
from tkinter import filedialog


class OneCounter:
    def __init__(self, accept_states, alphabet, start_state, states, transitions):
        self.accept_states = accept_states
        self.alphabet = alphabet
        self.start_state = start_state
        self.states = states
        self.transitions = transitions
        self.counter = 0

    def accepted_states(self, state):
        return state in self.accept_states

    def input_process(self, input_string):
        curr_state = self.start_state
        self.counter = 0
        for c in input_string:
            print(c)
            if c not in self.alphabet:
                raise ValueError(f"Invalid character '{c}' in the string")
            if self.counter > 0:
                key = 1
            else:
                key = 0
            transition_key = (curr_state, key, c)
            print(transition_key)
            if transition_key not in self.transitions:
                return False
            curr_state, counter_action = self.transitions[transition_key]
            self.counter += counter_action
            if self.counter < 0:
                return False
        return self.accepted_states(curr_state) and self.counter == 0


def read_one_counter_file(file_path):
    with open(file_path, "r") as file:

        num_states = int(file.readline())
        states = file.readline().split()
        num_inputs = int(file.readline())
        alphabet = file.readline().split()
        num_transitions = int(file.readline())
        transitions = {}

        for _ in range(num_transitions):
            source, is_zero, input_symbol, target, counter_action = file.readline().split()
            source, target = source.strip(), target.strip()
            counter_action, is_zero = int(counter_action), int(is_zero)
            transitions[(source, is_zero, input_symbol)] = (target, counter_action)

        start_state = file.readline().strip()
        num_accept_states = int(file.readline())
        accept_states = file.readline().split()

        return OneCounter(accept_states, alphabet, start_state, states, transitions)


class OneCounterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Deterministic One-Counter Automaton")
        self.geometry("400x500")

        self.label = tk.Label(self, text="Select Input File:")
        self.label.pack(pady=10)

        self.open_button = tk.Button(self, text="Open File", command=self.open_file)
        self.open_button.pack(pady=10)

        self.test_strings_label = tk.Label(self, text="Enter test strings (comma-separated):")
        self.test_strings_label.pack(pady=10)

        self.test_strings_entry = tk.Entry(self)
        self.test_strings_entry.pack(pady=5)

        self.result_text = tk.Text(self, wrap=tk.WORD)
        self.result_text.pack(pady=10, fill=tk.BOTH, expand=True)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            one_counter = read_one_counter_file(file_path)
            test_strings_input = self.test_strings_entry.get()
            test_strings = [s.strip() for s in test_strings_input.split(",")]
            result_str = ""
            for test_string in test_strings:
                result, steps = self.get_steps(one_counter, test_string)
                result_str += f"Input '{test_string}': {'Accepted' if result else 'Not Accepted'}\n"
                result_str += "Steps:\n"
                for step in steps:
                    result_str += f"State: {step[0]}, Character: {step[1]}, Counter Action: {step[2]}, Counter Value: {step[3]}\n"
                result_str += "\n"
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_str)

    def get_steps(self, one_counter, input_string):
        curr_state = one_counter.start_state
        counter = 0
        steps = []

        for c in input_string:
            if c not in one_counter.alphabet:
                raise ValueError(f"Invalid character '{c}' in the string")
            if counter > 0:
                key = 1
            else:
                key = 0
            transition_key = (curr_state, key, c)
            if transition_key not in one_counter.transitions:
                return False, steps
            next_state, counter_action = one_counter.transitions[transition_key]
            steps.append((curr_state, c, counter_action, counter))
            counter += counter_action
            if counter < 0:
                return False, steps
            curr_state = next_state

        if one_counter.accepted_states(curr_state) and counter == 0:
            result = True
        else:
            result = False

        steps.append((curr_state, '', 0, counter))
        return result, steps


if __name__ == "__main__":
    app = OneCounterGUI()
    app.mainloop()
