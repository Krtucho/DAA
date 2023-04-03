from sol import *

def dp(domains, n, k, p, elena, hansel):
    matrix = [[0 for x in range(n+1)] for y in range(n+1)]
    
    # Get all combinations with k for elena and hansel
    elena_domain = []
    hansel_domain = []

    elena_dict = {}
    hansel_dict = {}

    # elena_dict_copy = {}
    # hansel_dict_copy = {}

    # for domain in domains:
    for i in range(0, n-k+1): # Cost n*k - (n-k+1)*k = n*k - n*k + k*k = k*k
        elena_dict[i] = MatchedSOL(domain="elena", start=i, stop=i+k)
        hansel_dict[i] = MatchedSOL(domain="hansel", start=i, stop=i+k)
        # elena_dict_copy[i] = MatchedSOL(domain="elena", start=i, stop=i+k)
        # hansel_dict_copy[i] = MatchedSOL(domain="hansel", start=i, stop=i+k)
        # if domain == "elena":
            # elena_domain.append(MatchedSOL(domain=domain, start=i, stop=i+k))
        # else:
            # hansel_domain.append(MatchedSOL(domain=domain, start=i, stop=i+k))
            # result.append(SOL(domain=domain, start=i, stop=i+k))

    # Sort the result by the range
    # result.sort(key=lambda x: x.ranges.start)
    elena_domain.sort(key=lambda x: x.ranges.start)
    hansel_domain.sort(key=lambda x: x.ranges.start)

    # Set the matched mask and matched number for elena and hansel
    for hansel_sol in hansel_dict.values():
        matched_mask = [False]*n
        matched_number = 0
        for ans in hansel_sol.ranges:
            if ans+1 in hansel:
                matched_mask[ans] = True
                matched_number += 1
        hansel_sol.matched_mask = matched_mask
        hansel_sol.matched_number = matched_number

    for elena_sol in elena_dict.values():
        matched_mask = [False]*n
        matched_number = 0
        for ans in elena_sol.ranges:
            if ans+1 in elena:
                matched_mask[ans] = True
                matched_number += 1
        elena_sol.matched_mask = matched_mask
        elena_sol.matched_number = matched_number


    # Search answers for p = 1 and add it to matrix
    # for i in range(1, n-k+1):
    #     for j in range(1, n-k+1):
    #         if elena_dict[j-1].matched_number > hansel_dict[j-1].matched_number:
    #             matrix[i][j] = max(elena_dict[j-1].matched_number, matrix[1][j-1] + )
    #         else:
    #             matrix[i][j] = hansel_dict[j-1].matched_number

    #             0.+99999
    # for i in range(1, n-k+1):
    #     for j in range(1, n-k+1):
    #         if elena_dict[j-1].matched_number > hansel_dict[j-1].matched_number:
    #             matrix[i][j] = max(elena_dict[j-1].matched_number, matrix[1][j-1] + )
    #         else:
    #             matrix[i][j] = hansel_dict[j-1].matched_number
    
    # Print matrix
    for i in range(0, n+1):
        for j in range(0, n+1):
            print(matrix[i][j], end=" ")
     
    # for elena_sol in elena_dict.values():

    # # List for best results with p = 1
    # list_one = [0]*n
    # # Set the results best matched_number for p = 1
    # for i in range(0, n):
    #     if elena_dict[i].matched_number > hansel_dict[i].matched_number:
    #         list_one[i] = elena_dict[i].matched_number
    #     else:
    #         list_one[i] = hansel_dict[i].matched_number

    # list_two = [0]*n
    # # Set the results best matched_number for p = 2
    # for i in range(0, n):
    #     for j in range(i+1, n):
    #         if elena_dict[i].matched_number + hansel_dict[j].matched_number > hansel_dict[i].matched_number + elena_dict[j].matched_number:
    #             list_two[i] = elena_dict[i].matched_number + hansel_dict[j].matched_number
    #         else:
    #             list_two[i] = hansel_dict[i].matched_number + elena_dict[j].matched_number

    # # Set the results best matched_number for p = 3 using list_two and list_one
    # list_three = [0]*n
    # for i in range(0, n):
    #     for j in range(i+1, n):
    #         if list_one[i] + list_two[j] > list_one[j] + list_two[i]:
    #             list_three[i] = list_one[i] + list_two[j]
    #         else:
    #             list_three[i] = list_one[j] + list_two[i]

    # # Set the results best matched_number for p = n, n > 0, using list_one and list_n
    # list_n = [0]*n
    # for i in range(0, n):
    #     for j in range(i+1, n):
    #         if list_one[i] + list_three[j] > list_one[j] + list_three[i]:
    #             list_n[i] = list_one[i] + list_three[j]
    #         else:
    #             list_n[i] = list_one[j] + list_three[i]


def solve(elena: list, hansel:list, k:int, p:int, n:int):
    domains = ["elena", "hansel"]
    
    ans = dp(domains, n, k, p, elena, hansel)
    return ans