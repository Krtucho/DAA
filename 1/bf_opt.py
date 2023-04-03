import json
import random
import time
from generator import *
from formats import *
from sol import *

# elena = []
# hansel = []

# p = 2


def contains_sol(sols_dict, domain, start_range, stop_range):
    try:
        return sols_dict[f"{domain}_{start_range}_{stop_range}"]
    except:
        return False

def make_sol(domain, i, n):
    return SOL(domain=domain, start = i, stop = n )

def bf_opt(domains, n, k, p, sol, e, h, sols_dict):
    ans = 0
    if k == n or n <= k*p: # Si la cantidad de intentos que puedo usar me basta para encontrar las 9 preguntas entre ambas pruebas
        if not sol:
            pass
        else:
            ans = evaluate(sol, n, e, h)
    if not p:
        return evaluate(sol, n, e ,h)

    # ans = 0
    for domain in domains:
        for i in range(0, n-k+1): # for i in range(0, n-k+1): 
            if contains_sol(sols_dict, domain, i, i+k): # If has choosen the sol, just continue
                continue
            tmp_sol = make_sol(domain, i, i+k)
            concat_sol:list = SOL.concat_sol(sol, tmp_sol)

            # Logs
            # printb(tmp_sol)
            sols_dict[f"{domain}_{i}_{i+k}"] = True

            ans = max(ans, bf_opt(domains, n, k, p-1, concat_sol, e, h, sols_dict))

            sols_dict[f"{domain}_{i}_{i+k}"] = False

            # Remover el ultimo elemento de una lista
            concat_sol.pop()

    return ans
            

def solve(elena: list, hansel:list, k:int, p:int, n:int):
    result = []
    # k = 1
    # n = 8

    domains = ["elena", "hansel"]
    
    
    ans = bf_opt(domains, n, k, p, result, elena, hansel, {})
    return ans
# a = range(1,2)
# print(a)
# print(a.index(1))
# print("start" ,a.start)
# print(a.step)
# print(a.stop) random.randint(1, n)

def random_solver():
    # load a random problem from generator.py
    # solve it
    # save the solution in a json file
    helena, hansel, k, p, n = problem_generator()
    solve(helena, hansel, k, p, n)

def load_solutions(file_name):
    with open(file_name, "r") as f:
        solutions = json.load(f)

    return solutions["solutions"]

def solve_file(file_name):
    elena, hansel, k, p, n = load_params(file_name)
    return solve(elena, hansel, k, p, n)

# show_generated_sols_file_names()
# # random_solver()
# ans = solve_file("1680185784.9080827_params.json")

# printg(f"maximum: {ans} SUCCESS")