import bf
import bf_opt
import greedy
import div_n_con

from generator import *
from formats import *
import time


def test_sol(elena, hansel, k, p, n, sol, method="bf", test_alg_time=""):
    ans = 0

    ts = time.time()
    
    if method == "bf":
        ans = bf.solve(elena, hansel, k, p, n)
    elif method == "bf_opt":
        ans = bf_opt.solve(elena, hansel, k, p, n)
    elif method == "div_n_con":
        ans = div_n_con.solve(elena, hansel, k, p, n)
    elif method == "greedy":
        ans = greedy.solve(elena, hansel, k, p, n)

    te = time.time()
    time_str = f"Time: {round(te-ts, 5)}"

    if ans == sol:
        printg(f"maximum: {sol} {test_alg_time} expected: {method}_solution: {ans} SUCCESS! {time_str}")
    else:
        printr(f"maximum: {sol} expected: {ans} !FAILED {time_str}")
        return False

    return True
def test_ramdom_sol():
    elena, hansel, k, p, n = problem_generator()#load_params("test_solutions/1680473961.5395467_params.json")#problem_generator()#load_params("test_solutions/1680471934.3560534_params.json")#load_params("test_solutions/1680471130.264099_params.json")#load_params("test_solutions/1680470753.1520169_params.json")#load_params("test_solutions/1680465226.0782478_params.json")#problem_generator()#load_params("1680185784.9080827_params.json")
    
    # elena, hansel, k, p, n = [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 20], [1, 2, 3, 5, 6, 7, 9, 11, 12, 15, 17, 18, 20], 8, 2, 20 
    ts = time.time()

    # ans = bf_opt.solve(elena, hansel, k, p, n)
    ans = greedy.solve(elena, hansel, k, p, n)
    # ans = dp.solve(elena, hansel, k, p, n)
    # ans = div_n_con.solve(elena, hansel, k, p, n)

    te = time.time()
    time_str = f"Time: {round(te-ts, 5)}"

    if not test_sol(elena, hansel, k, p, n, ans, "div_n_con", time_str):
        print("SOLUTION FAILED, ALGORITHM HAS BUGS")
        # Save log in a file
        file = open("log.txt", "a")
        file.write(f"Error with params:\nelena: {elena} hansel: {hansel} k: {k} p: {p} n: {n} ans: {ans}\n with algorithm: div_n_con")
        file.close()

while True:
    test_ramdom_sol()
    time.sleep(5)
    # input("Press enter for another solution")