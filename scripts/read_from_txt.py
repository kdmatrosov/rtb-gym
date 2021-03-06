# -*- coding: utf-8 -*-
import re

f = open('../data.txt', 'r')
data = f.readlines()
f.close()

f = open("../data/set.txt", "w")
data = data[1:]  # убрать первую строку

mapXtoWR = {}  # CTR

for line in data:
    x = re.findall(r'(\S+)', line)
    key = x[4] + "_" + x[5] + "_" + x[6] + "_" + x[2] + "_" + x[3]  # city sex age camp adv
    if key in mapXtoWR:
        mapXtoWR[key][0] += int(x[0])  # clicks
        mapXtoWR[key][1] += int(x[1])  # shows
    else:
        mapXtoWR[key] = [int(x[0]), int(x[1]), 0, x[2], x[3]]

line = "{:>5}\t {:>4}\t {:<4}% {:>4}\t {:>4}\t {:>30}\t" \
    .format("click", "show", "CTR", "campId", "advId", "user")
f.write(line + "\n")

for key in mapXtoWR:
    if mapXtoWR[key][1] > 0:
        mapXtoWR[key][2] = round(10000 * mapXtoWR[key][0] / mapXtoWR[key][1]) / 100
    line = "{:>5}\t {:>4}\t {:<6.2f} {:>4}\t {:>4}\t {:>30}" \
        .format(mapXtoWR[key][0], mapXtoWR[key][1], mapXtoWR[key][2], mapXtoWR[key][3], mapXtoWR[key][4], key)
    f.write(line + "\n")

f.close()