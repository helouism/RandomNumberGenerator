import random
from pyscript import document


def generate_num(event):
    """Generate a random number between 1 and 10"""
    input_start = document.querySelector("#range_start")
    num_start = int(input_start.value)

    input_end = document.querySelector("#range_end")
    num_end = int(input_end.value)

    random_num = random.randint(num_start, num_end)

    output_div = document.querySelector("#output")
    output_div.innerText = random_num
