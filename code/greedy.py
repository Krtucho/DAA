from sol import *
import copy

def update_mask(marked:MatchedSOL, target:MatchedSOL, k):
    for index in marked.ranges:
        val = marked.matched_mask[index]
        if val and target.matched_mask[index]:
            target.matched_mask[index] = False
            target.matched_number -= 1


def update_matched_number(matched_sol: MatchedSOL, k: int, n: int, elena_dict, hansel_dict):
    # Update matched_mask for overlapping indices in ranges of elena_dict.values and hansel_dict.values()
    clone = MatchedSOL(matched_sol.domain, matched_sol.ranges.start, matched_sol.ranges.stop, matched_sol.matched_mask.copy(), matched_sol.matched_number)
    # Create a clone of matched_sol
    for i in range(max(0, clone.ranges.start-k), min(clone.ranges.start+k, n-k+1)):
        update_mask(clone, elena_dict[i], k)
        update_mask(clone, hansel_dict[i], k)
    
    # Update elements with the same range or overlapping range with the matched element. Update matched_mask and matched_number. matched_mask is a boolean list with indices meaning that the index is matched or not. matched_number is the number of indices in mask that are true


def greedy(n, k, p, elena, hansel):
    # Get all combinations with k for elena and hansel
    elena_dict = {}
    hansel_dict = {}

    for i in range(0, n-k+1): # Cost n*k - (n-k+1)*k = n*k - n*k + k*k = k*k
        elena_dict[i] = MatchedSOL(domain="elena", start=i, stop=i+k)
        hansel_dict[i] = MatchedSOL(domain="hansel", start=i, stop=i+k)

    # Set the matched mask and matched number for elena and hansel
    for elena_sol in elena_dict.values():
        matched_mask = [False]*n
        matched_number = 0
        for ans in elena_sol.ranges:
            if ans+1 in elena:
                matched_mask[ans] = True
                matched_number += 1
        elena_sol.matched_mask = matched_mask
        elena_sol.matched_number = matched_number
    
    for hansel_sol in hansel_dict.values():
        matched_mask = [False]*n
        matched_number = 0
        for ans in hansel_sol.ranges:
            if ans+1 in hansel:
                matched_mask[ans] = True
                matched_number += 1
        hansel_sol.matched_mask = matched_mask
        hansel_sol.matched_number = matched_number
    
    ans = 0

    while p:
        # Get the maximum element by matcher_number
        max_elena: MatchedSOL = max(elena_dict.values(), key=lambda x: x.matched_number)
        max_hansel: MatchedSOL = max(hansel_dict.values(), key=lambda x: x.matched_number)

        matched_sol: MatchedSOL = max_elena

        # if are the same matched_number, look if they overlap and chose one
        if max_elena.matched_number == max_hansel.matched_number:
            # If ranges overlap, choose the one with the smallest start index
            if abs(max_elena.ranges.start - max_hansel.ranges.start) < k:
                # Looking for the best choice
              
                # Make a copy of elena_dict and hansel_dict to not modify the original one and update the matched_number
                elena_dict_copy = copy.deepcopy(elena_dict)#.copy()
                hansel_dict_copy = copy.deepcopy(hansel_dict)#.copy()

                # Update the matched_number for the elena_dict_copy and hansel_dict_copy
                update_matched_number(max_elena, k, n, elena_dict_copy, hansel_dict_copy)
                max_elena_copy = max(max(elena_dict_copy.values(), key=lambda x: x.matched_number).matched_number, max(hansel_dict_copy.values(), key=lambda x: x.matched_number).matched_number)

                # Make a copy of elena_dict and hansel_dict to not modify the original one and update the matched_number
                elena_dict_copy = copy.deepcopy(elena_dict)#.copy()
                hansel_dict_copy = copy.deepcopy(hansel_dict)#.copy()

                # Update the matched_number for the elena_dict_copy and hansel_dict_copy
                update_matched_number(max_hansel, k, n, elena_dict_copy, hansel_dict_copy)

                max_hansel_copy = max(max(elena_dict_copy.values(), key=lambda x: x.matched_number).matched_number, max(hansel_dict_copy.values(), key=lambda x: x.matched_number).matched_number)

                if max_elena_copy > max_hansel_copy:
                    matched_sol = max_elena
                else:
                    matched_sol = max_hansel
        # else, choose the biggest
        else:
            matched_sol = max_elena if max_elena.matched_number > max_hansel.matched_number else max_hansel

        ans += matched_sol.matched_number # Update the answer


        # Logs
        # print(max_elena)
        # print(max_hansel)

        # Update elements with the same range or overlapping range with the matched element
        update_matched_number(matched_sol, k, n, elena_dict, hansel_dict)
        # Add the element back to the result

        p -= 1

    return ans


def solve(elena: list, hansel:list, k:int, p:int, n:int):
    result = []
    domains = ["elena", "hansel"]
    
    
    ans = greedy(n, k, p, elena, hansel)
    return ans

