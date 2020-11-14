# University of Science, VNU
# Author: Nhut-Nam Le
# Vietnamese Word Tokenize
# -*- coding: utf-8 -*-
with open('./src/data/VDic_uni.txt', 'r', encoding='utf-8') as reader:
    lines = [line.rstrip() for line in reader]

lines.remove(lines[0])

with open('./src/data/process_vdic.txt', 'w', encoding='utf-8') as writer:
    for line in lines:
        data = line.split('\t\t')
        writer.write(data[0] + '\n')
