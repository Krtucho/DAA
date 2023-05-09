import json
import random
import time
from generator import *
from formats import *
from sol import *
from graph import *

def same_degrees(n_u, n_v, edges: list, mask):
    degrees_u = {i:0 for i in range(n_u)}
    degrees_v = {i:0 for i in range(n_v)}

    for index, val in enumerate(mask):
        if val:
            try:
                degrees_u[edges[index][0]] += 1
            except:
                degrees_u[edges[index][0]] = 1
            
            try:
                degrees_v[edges[index][1]] += 1
            except:
                degrees_v[edges[index][1]] = 1

    if len(degrees_u) <= 0:
        return False, 1e9
    
    actual_min_degree = 1e9
    for item in degrees_u.items():
        actual_min_degree = min(actual_min_degree, item[1])

    for item in degrees_v.items():
        actual_min_degree = min(actual_min_degree, item[1])


    if actual_min_degree == 0:
        return False, actual_min_degree
    else:
        return True, actual_min_degree

def update_minimums(mask, minimums:dict, deg, edges):
    if not minimums.__contains__(deg):
        count = 0
        for val in mask:
            if val:
                count += 1

        minimums[deg] = SOL(deg, [val for val in mask], edges, count)
    else:
        count = 0
        for val in mask:
            if val:
                count += 1
        
        if minimums[deg].count > count:
            minimums[deg] = SOL(deg, [val for val in mask], edges, count)
        

def evaluate(n_u, n_v, edges, mask, minimums, minDegree: int):
    same_deg, deg = same_degrees(n_u, n_v, edges, mask)
    if same_deg and deg <= minDegree:
        # print(deg)
        # print(mask)
        update_minimums(mask, minimums, deg, edges)

def bf(n_u: int, n_v: int, edges: list, mask: list, index: int, minimums: dict, min_degree)-> None:
    # If ends
    if index == len(edges):
        evaluate(n_u, n_v, edges, mask, minimums, min_degree)
        return
    # Update minimums

    # LLamar al metodo recursivo sin tener en cuenta esta arista
    bf(n_u, n_v, edges, mask, index+1, minimums, min_degree)

    mask[index] = True
    bf(n_u, n_v, edges, mask, index+1, minimums, min_degree) # Llamar al metodo recursivo teniendo en cuenta esta arista
    mask[index] = False

def get_min_degree(edges):
    degrees_u = dict()
    degrees_v = dict()
    for index, val in enumerate(edges):
        try:
            degrees_u[val[0]] += 1
        except:
            degrees_u[val[0]] = 1
        
        try:
            degrees_v[val[1]] += 1
        except:
            degrees_v[val[1]] = 1

    min_degree = 1e8
    for deg in degrees_u.values():
        min_degree = min(min_degree, deg)
    
    for deg in degrees_v.values():
        min_degree = min(min_degree, deg)
    
    return min_degree

def solve(n_u: int, n_v: int, edges: list):
    """
    edges sera una lista de tuplas, el primer elemento es el nodo de U y el 2do el nodo de V
    """
    # Calc min_degree
    edges = [(u-1,v-1) for (u,v) in edges]
    min_degree = get_min_degree(edges)#0
    mask = [False]*len(edges)
    minimums = dict()

    print(min_degree)
    bf(n_u, n_v, edges, mask, 0, minimums, min_degree)

    ans = {0:0}
    for minimum in minimums.items():
        ans[minimum[0]] = minimum[1].count
        print(f"k: {minimum[0]} count: {minimum[1].count} mask: {minimum[1].mask} edges: {minimum[1].edges}")
    
    return ans

def random_solver():
    # load a random problem from generator.py
    # solve it
    # save the solution in a json file
    n_u, n_v, edges = problem_generator()
    solve(n_u, n_v, edges)

def load_solutions(file_name):
    with open(file_name, "r") as f:
        solutions = json.load(f)

    return solutions["solutions"]

def solve_file(file_name):
    n_u, n_v, edges = load_params(file_name)
    return solve(n_u, n_v, edges)