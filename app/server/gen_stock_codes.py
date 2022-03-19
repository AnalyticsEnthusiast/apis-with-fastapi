
import string
import random

def generate_stock_code():
    return ''.join(random.choices(string.ascii_lowercase, k=10))
