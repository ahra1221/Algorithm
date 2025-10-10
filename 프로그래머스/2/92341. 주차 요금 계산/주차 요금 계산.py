from collections import defaultdict
import math

def cal_time(intime, outtime):
    inhour, inmin = map(int, intime.split(":"))
    outhour, outmin = map(int, outtime.split(":"))
    return 60 * (outhour - inhour) + (outmin - inmin)

def solution(fees, records):

    answer = []
    cars_record = {}
    accum = defaultdict(int)

    for record in records:
        time, carnum, inout = record.split()
        if inout == "IN":
            cars_record[carnum] = time
        else:
            accum[carnum] += cal_time(cars_record[carnum],time)
            cars_record.pop(carnum)

    if cars_record:
        for n, t in cars_record.items():
            accum[n] += cal_time(t, '23:59')

    for n, t in sorted(accum.items(), key=lambda x:x[0]):
        fee = fees[1]
        if t > fees[0]:
            moretime = t - fees[0]
            fee += math.ceil(moretime / fees[2]) * fees[3]
        answer.append(fee)

    return answer