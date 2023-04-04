import json
import random
import time
from generator import *
from formats import *
from sol import *

def make_sol(domain, i, n):
    return SOL(domain=domain, start = i, stop = n )

def bf(domains, n, k, p, sol, e, h):
    if not p:
        return evaluate(sol, n, e ,h)

    ans = 0
    for domain in domains:
        for i in range(0, n-k+1):
            tmp_sol = make_sol(domain, i, i+k)
            concat_sol:list = SOL.concat_sol(sol, tmp_sol)

            # Logs
            # printb(tmp_sol)

            ans = max(ans, bf(domains, n, k, p-1, concat_sol, e, h))
            
            # Remover el ultimo elemento de una lista
            concat_sol.pop()

    return ans
            

def solve(elena: list, hansel:list, k:int, p:int, n:int):
    result = []

    domains = ["elena", "hansel"]
    
    
    ans = bf(domains, n, k, p, result, elena, hansel)
    return ans

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