def make_i(value):
    value = str(value)
    try:
        real = float(value)
        imaginary = 0.

    except ValueError:
        try:
            imaginary = float(value.replace('i', ''))
            real = 0.
        except ValueError:
            pos_split = value.split('+')
            if len(pos_split) == 2:
                real = float(pos_split[0])
                imaginary = float(pos_split[1].replace('i', ''))
            else:
                neg_split = value.split('-')
                if len(neg_split) == 2:
                    real = float(neg_split[0])
                    imaginary = float(neg_split[1].replace('i', ''))
                else:
                    real = None 
                    imaginary = None
    d = {'real': real, 'i': imaginary} 
    return d

class complex_op():

    def __init__(self, x):
        self.x_real = make_i(x)['real']
        self.x_i = make_i(x)['i'] 


    def __add__(self, other):
        y_i = make_i(other)['i']
        y_real = make_i(other)['real']

        self.x_real += y_real
        self.x_i += y_i

        return self.x_real, self.x_i
    
    def __radd__(self, other):
        y_i = make_i(other)['i']
        y_real = make_i(other)['real']

        self.x_real += y_real
        self.x_i += y_i

        return self.x_real, self.x_i

d = [complex_op(f'{i}+ 12.2i') for i in range(10)]
sum_d = sum(d)
print('Done debugging')
