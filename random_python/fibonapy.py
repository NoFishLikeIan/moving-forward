def fibonacci(pos, ret_seq = True):
    a, b = 0, 1
    sequence = [a,b]
    for i in range(pos):
        old_b = b
        b += a
        a = old_b
        sequence.append(b)

    sequence = sequence if ret_seq else sequence[-1]
    return sequence