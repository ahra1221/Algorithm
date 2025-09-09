class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for o in operations:
            l = len(record)
            if o == "+":
                s = record[l-1] + record[l-2]
                record.append(s)
            elif o == "D":
                record.append(record[l-1] * 2)
            elif o == "C":
                record.pop()
            else:
                record.append(int(o))
        return sum(record) if record else 0