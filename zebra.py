from turing_machine import turing_partial_function, DictTape


def python_zebra(input_str, limit=None):
    tape = DictTape(input_str)
    head = 0
    state = 'write_0'
    n = 1
    while n != limit:
        char_r = tape[head]
        if state == 'write_0' and char_r is None:
            tape[head] = '0'
            state = 'blank_after_0'
            head += 1
        elif state == 'blank_after_0' and char_r is None:
            tape[head] = None
            state = 'write_1'
            head += 1
        elif state == 'write_1' and char_r is None:
            tape[head] = '1'
            state = 'blank_after_1'
            head += 1
        elif state == 'blank_after_1' and char_r is None:
            tape[head] = None
            state = 'write_0'
            head += 1
        n += 1
    return str(tape)


turing_zebra = turing_partial_function('write_0', {
    ('write_0', None): ('blank_after_0', '0', +1),
    ('blank_after_0', None): ('write_1', None, +1),
    ('write_1', None): ('blank_after_1', '1', +1),
    ('blank_after_1', None): ('write_0', None, +1),
})

print(python_zebra('', 32))
print(turing_zebra('', 32))
