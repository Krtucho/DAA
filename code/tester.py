import bf
import max_flow
# import bf_opt
# import greedy
# import div_n_con

from generator import *
from formats import *
import time
from sol import AlgSol


def test_sol(n_u, n_v, edges, sol, method="bf", test_alg_time=""):
    ans = 0

    ts = time.time()
    
    if method == "bf":
        ans = bf.solve(n_u, n_v, edges)
    elif method == "max_flow":
        ans = max_flow.solve(n_u, n_v, edges)

    te = time.time()
    time_str = f"Time: {round(te-ts, 5)}"

    if AlgSol.compare_sol(ans, sol):
        printg(f"maximum: {sol} {test_alg_time} expected: {method}_solution: {ans} SUCCESS! {time_str}")
    else:
        printr(f"maximum: {sol} expected: {ans} !FAILED {time_str}")
        return False

    return True
    
def test_ramdom_sol():
    n_u, n_v, edges = load_params("test_solutions/1683515630.0276542_params.json")#problem_generator()#load_params("test_solutions/1683514321.0528038_params.json")#problem_generator()#load_params("test_solutions/1680473961.5395467_params.json")#problem_generator()#load_params("test_solutions/1680471934.3560534_params.json")#load_params("test_solutions/1680471130.264099_params.json")#load_params("test_solutions/1680470753.1520169_params.json")#load_params("test_solutions/1680465226.0782478_params.json")#problem_generator()#load_params("1680185784.9080827_params.json")
    
    ts = time.time()

    # ans = bf.solve(n_u, n_v, edges)
    ans = max_flow.solve(n_u, n_v, edges)

    te = time.time()
    time_str = f"Time: {round(te-ts, 5)}"

    if not test_sol(n_u, n_v, edges, ans, "bf", time_str):
        print("SOLUTION FAILED, ALGORITHM HAS BUGS")
        # Save log in a file
        file = open("log.txt", "a")
        file.write(f"Error with params:\nn_u: {n_u} n_v: {n_v} edges: {edges} ans: {ans}\n with algorithm: bf")
        file.close()

while True:
    test_ramdom_sol()
    time.sleep(2)
    # input("Press enter for another solution")