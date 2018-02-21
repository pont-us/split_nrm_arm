#!/usr/bin/env python3

# By Pontus Lurcock, 2018.
# This is free and unencumbered software released into the public domain.
# See https://unlicense.org/UNLICENSE for full licensing statement.

from typing import List, Tuple
import argparse


def split(lines: List[str]) -> Tuple[List[str], List[str]]:
    chunks = ([lines[0]], [lines[0]])
    accumulator = chunks[0]
    for line in lines[1:]:
        if "ARM axial" in line:
            accumulator = chunks[1]
        accumulator.append(line)
    return chunks


def main():
    parser = argparse.ArgumentParser("Split a DAT file into NRM and ARM")
    parser.add_argument("INPUT_FILE", type=str)
    parser.add_argument("OUTPUT_FILE_NRM", type=str)
    parser.add_argument("OUTPUT_FILE_ARM", type=str)
    args = parser.parse_args()
    with open(args.INPUT_FILE) as fh:
        lines = fh.readlines()
    chunks = split(lines)
    with open(args.OUTPUT_FILE_NRM, "w") as fh:
        fh.writelines(chunks[0])
    with open(args.OUTPUT_FILE_ARM, "w") as fh:
        fh.writelines(chunks[1])


if __name__ == "__main__":
    main()
