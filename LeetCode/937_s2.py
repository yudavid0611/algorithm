class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digits = []
        letters = []

        for log in logs:
            space_idx = log.find(' ')
            if log[space_idx + 1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        f = lambda x: (x.split()[1:], x.split()[0])
        letters = sorted(letters, key=f)
        
        return letters + digits