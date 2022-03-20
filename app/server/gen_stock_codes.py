
import string
import random


class gen_stock_codes:
    
    def __init__(self):
        pass

    def generate_stock_code(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10))
