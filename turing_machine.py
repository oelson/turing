def turing_generator(input_str, initial_state, transitions):
    tape = DictTape(input_str)
    head = 0
    state = initial_state
    yield str(tape), head, state
    while True:  # repetition
        char_r = tape[head]  # perception
        behavior = transitions[(state, char_r)]  # branching
        if behavior is None:
            return None  # termination
        else:
            next_state, char_w, step = behavior
        tape[head] = char_w  # write
        head += step  # move
        state = next_state  # reconfiguration
        yield str(tape), head, state


def turing_partial_function(initial_state, transitions):
    def turing_execution(input_str, limit=None):
        generator = turing_generator(input_str, initial_state, transitions)
        n = 1
        tape = None
        for tape, _, _ in generator:
            if n == limit:
                break
            n += 1
        return tape

    return turing_execution


class DictTape:
    def __init__(self, input_str=''):
        self.dict = dict(enumerate(input_str))

    def __getitem__(self, index):
        return self.dict[index] if index in self.dict else None

    def __setitem__(self, index, char):
        self.dict[index] = char

    def __str__(self):
        indexes = list(self.dict.keys())
        indexes.sort()
        ordered_chars = (self.dict[index] if self.dict[index] is not None else ' ' for index in indexes)
        return ''.join(ordered_chars)

    def __len__(self):
        return len(self.dict)
