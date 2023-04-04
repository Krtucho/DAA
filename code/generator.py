# Create a generator of problem instances
import json
import random
import time


def problem_generator():
    n = random.randint(1, 20)
    k = random.randint(1, n)
    p = random.randint(1, n)
    elena = []
    hansel = []

    for i in range(0, n):
        elena.append(random.randint(1, n))
        hansel.append(random.randint(1, n))

    elena.sort()
    hansel.sort()
    # Remove duplicates from the lists
    elena = list(dict.fromkeys(elena))
    hansel = list(dict.fromkeys(hansel))
    
    filename = save_params(elena, hansel, k, p, n)
    print(f"Problem saved in {filename}")

    return elena, hansel, k, p, n


# Create a function to save the params elena, hansel, k, p and n in a json file
def save_params(elena, hansel, k, p, n):
    # elena, hansel, k, p, n = problem_generator()
    params = {
        # "id": 1,
        "elena": elena,
        "hansel": hansel,
        "k": k,
        "p": p,
        "n": n
    }

    filename = f"test_solutions/{str(time.time())}_params.json" 
    with open(filename, "w") as f:
        json.dump(params, f)

    return filename

# Load params from json file
def load_params(file_name):
    with open(file_name, "r") as f:
        params = json.load(f)

    return params["elena"], params["hansel"], params["k"], params["p"], params["n"]

def show_generated_sols_file_names():
    import os
    for file in os.listdir("test_solutions"):
        if file.endswith("_params.json"):
            print(file)
            print("elena, hansel, k, p, n")
            print(load_params(file), "\n")