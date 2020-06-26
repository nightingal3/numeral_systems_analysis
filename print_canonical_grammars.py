from num2words import num2words

#a = 11, b = 12...etc
additional_digits = {num: letter for num, letter in zip([i for i in range(11, 21)], [chr(i) for i in range(97, 107)])}

def decompose(num, base):
    coefficients = list(str(num))
    vals = []
    for i, coefficient in enumerate(coefficients[::-1]):
        val = int(coefficient) * (base ** i)
        vals.insert(0, val)
    
def print_base_n_rep(num, n):
    return int(num, n)

if __name__ == "__main__":
    decompose(135, 10)