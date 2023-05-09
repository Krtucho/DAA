# Create a generator of problem instances
import json
import random
import time


def problem_generator():
    n_u = random.randint(1, 3)
    n_v = random.randint(1, 3)
    edges_count = random.randint(max(n_u, n_v), 20)
    edges = []
    for i in range(edges_count):
        edges.append((random.randint(1,n_u), random.randint(1, n_v)))

    filename = save_params(n_u, n_v, edges)
    print(f"Problem saved in {filename}")

    return n_u, n_v, edges

# Create a function to save the params elena, hansel, k, p and n in a json file
def save_params(n_u, n_v, edges):
    # elena, hansel, k, p, n = problem_generator()
    params = {
        # "id": 1,
        "n_u": n_u,
        "n_v": n_v,
        "edges": edges
    }

    filename = f"test_solutions/{str(time.time())}_params.json" 
    with open(filename, "w") as f:
        json.dump(params, f)

    return filename

# Load params from json file
def load_params(file_name):
    with open(file_name, "r") as f:
        params = json.load(f)

    return params["n_u"], params["n_v"], params["edges"]

def show_generated_sols_file_names():
    import os
    for file in os.listdir("test_solutions"):
        if file.endswith("_params.json"):
            print(file)
            print("n_u, n_v, edges")
            print(load_params(file), "\n")