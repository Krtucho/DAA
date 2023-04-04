class SOL:
    def __init__(self, domain, start, stop) -> None:
        self.domain = domain
        self.ranges:range = range(start, stop)

    # Redefinir el print de la clase SOL
    def __str__(self) -> str:
        return f"Domain: {self.domain} Range: start: {self.ranges.start+1} end: {self.ranges.stop}"
    
    def __repr__(self) -> str:
        return f"Domain: {self.domain} Range: start: {self.ranges.start+1} end: {self.ranges.stop}"

    @staticmethod
    def concat_sol(left_sol: list, right_sol):
        tmp_left_sol = left_sol.copy()
        tmp_left_sol.append(right_sol)
        return tmp_left_sol

class MatchedSOL(SOL):
    def __init__(self, domain, start, stop, matched_mask: list=[], matched_number: int=0) -> None:
        super().__init__(domain, start, stop)
        self.matched_mask = matched_mask
        self.matched_number = matched_number # Matched number is the number of indices in mask that are true

    def __str__(self) -> str:
        return f"Domain: {self.domain} Range: start: {self.ranges.start+1} end: {self.ranges.stop} matched: {self.matched_number}"

    def __repr__(self) -> str:
        return f"Domain: {self.domain} Range: start: {self.ranges.start+1} end: {self.ranges.stop} matched: {self.matched_number}"
    
def evaluate(sols, n, e, h):
    answers = [False]*n
    count = 0

    # Logs
    # printb("Actual Sol")

    for sol in sols:
        for ans in sol.ranges:
            if (sol.domain == "elena" and ans+1 in e and not answers[ans])  or (sol.domain == "hansel" and ans+1 in h and not answers[ans]):
                answers[ans] = True
                count += 1
        # Logs
        # print(sol)
    # Logs
    # printb("End of Actual Sol")
        
    output = ""
    red = []
    green = []
    for index, token in enumerate(answers):
        if token:
            green.append(index)
        else:
            red.append(index)
        output += str(index+1)

    # Logs
    # print("Answers: ")
    # printgr(output, red, green)
    # print(answers)
    return count