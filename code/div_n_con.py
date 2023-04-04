from sol import *

def div_n_con(domains, n, k, p, elena, hansel, pos, sol):
    # if n == pos + k: if theres is no more choices
    if n - k <= pos - 2:
        return evaluate(sol, n, elena, hansel)
    # if p == 0: if there is no more choices
    if p == 0:
        return evaluate(sol, n, elena, hansel)

    # Try choosing elena, then choosing hansel and then choosing no one
    return max(div_n_con(domains, n, k, p - 1, elena, hansel, pos+1, SOL.concat_sol(sol, SOL("elena", pos, pos+k))), 
               div_n_con(domains, n, k, p - 1, elena, hansel, pos+1, SOL.concat_sol(sol, SOL("hansel", pos, pos+k))),
               div_n_con(domains, n, k, p, elena, hansel, pos+1, sol))


def solve(elena: list, hansel:list, k:int, p:int, n:int):
    domains = ["elena", "hansel"]
    
    ans = div_n_con(domains, n, k, p, elena, hansel, 0, [])
    return ans