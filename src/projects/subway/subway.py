#!/usr/bin/env python3
# encoding: UTF-8
"""Torn to pieces"""

from pythonds3.graphs import Graph
from typing import Tuple


def read_file(filename: str) -> Tuple[Graph, str, str]:
    """
    Read graph from file

    Return the graph object and two vertices: start and destination
    """
    raise NotImplementedError


def find_routes(g: Graph, src: str, dst: str) -> str:
    """Find the path between two stations"""
    raise NotImplementedError


def main():
    """This is the main function"""
    pass


if __name__ == "__main__":
    main()
