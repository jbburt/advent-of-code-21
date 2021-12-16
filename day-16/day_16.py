"""
https://adventofcode.com/2021/day/16
"""

from math import prod
from operator import gt, lt, eq

with open('day-16/input.txt', 'r') as fp:
    data = list(fp.read())

mapping = {x: y for x, y in zip('ABCDEF', range(10, 16))}
mapping |= {str(i): i for i in range(10)}

_ops = [sum, prod, min, max, None, gt, lt, eq]


def int2bin(x):
    return "{:04b}".format(x)


def bin2int(b):
    return int(b, 2)


intmap = {k: int2bin(v) for k, v in mapping.items()}

string = "".join(intmap[char] for char in data)


def process_literal(i):
    binrep = ''
    end = False
    while not end:
        if string[i] == '0':
            end = True
        binrep += string[i + 1:i + 5]
        i = i + 5
    literal = bin2int(binrep)
    return i, literal


def get_packet_length(i):
    length = bin2int(string[i:i + 15])
    return i + 15, length


def process_packet(i, nsubpackets=None, j=None):

    global versions
    global _ops

    packet_start = i

    # parse version and packet type id
    version = bin2int(string[i:i + 3])
    versions += version
    packet_type = bin2int(string[i + 3:i + 6])

    i = i + 6
    nsub = 0
    num = fn = None
    subpackets = list()

    if packet_type == 4:
        i, num = process_literal(i)
    else:
        fn = _ops[packet_type]
        length_type = string[i]
        i = i + 1
        if length_type == '0':
            # next 15 bits are a number that represents total length in bits
            i, length = get_packet_length(i)
            packet_end = i + length
            while True and i < len(string):
                if j is not None and i >= j:
                    break
                if nsubpackets is not None and nsub == nsubpackets:
                    break
                if i >= packet_end:
                    break
                i, s = process_packet(i, j=packet_end)
                subpackets.append(s)
                nsub = nsub + 1
        else:
            # next 11 bits are number that represents the number of sub packets
            npackets = bin2int(string[i:i + 11])
            i = i + 11
            for _ in range(npackets):
                i, m = process_packet(i)
                subpackets.append(m)

    if num is None:
        if packet_type > 4:
            num = fn(*subpackets)
        else:
            num = fn(subpackets)

    # pad with zeros if packet not a multiple of 4 bits long
    size = i - packet_start
    if not (size % 4):
        npad = (4 - (size % 4)) % 4
    else:
        npad = 0
    i = i + npad

    return i, num


versions = 0

i, n = process_packet(0)
print(f'p1: {versions}')
print(f'p2: {n}')
