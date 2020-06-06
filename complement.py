from turing_machine import turing_partial_function, DictTape


def python_binary_complement(input_str, limit=None):
    tape = DictTape(input_str)
    head = 0
    state = 'complement'
    n = 1
    while n != limit:
        char_r = tape[head]
        if state == 'complement' and char_r == '0':
            tape[head] = '1'
            state = 'complement'
            head += 1
        elif state == 'complement' and char_r == '1':
            tape[head] = '0'
            state = 'complement'
            head += 1
        elif state == 'complement' and char_r is None:
            break
        n += 1
    return str(tape)


turing_binary_complement = turing_partial_function('complement', {
    ('complement', '0'): ('complement', '1', +1),
    ('complement', '1'): ('complement', '0', +1),
    ('complement', None): None,
})

binary_string = '1100011011010010110010100010001011101111'

print(binary_string)
print('-' * len(binary_string))

print(python_binary_complement(binary_string))
print(turing_binary_complement(binary_string))
