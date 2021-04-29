"""
Create graphs for use in test cases here.
"""
import networkx as nx
import pytest


@pytest.fixture
def tree1() -> nx.Graph:
    """
    :return: A line graph on 5 vertices with varying weights.
    """
    tree = nx.Graph()
    tree.add_nodes_from([
        (0, {"weight": 2}),
        (1, {"weight": 3}),
        (2, {"weight": 5}),
        (3, {"weight": 2}),
        (4, {"weight": 3})
    ])
    tree.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4)])
    return tree


@pytest.fixture
def tree2() -> nx.Graph:
    """
    :return: A complete binary tree of depth 4 with uniform weights of 1.
    """
    tree = nx.Graph()
    tree.add_nodes_from([(i, {"weight": 1}) for i in range(15)])
    tree.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6),
                         (3, 7), (3, 8), (4, 9), (4, 10),
                         (5, 11), (5, 12), (6, 13), (6, 14)])
    return tree


@pytest.fixture
def tree3() -> nx.Graph:
    """
    :return: A complete binary tree on 7 vertices with the ith vertex having
    weight i. This test uses a non-default keyword for the weight attribute
    and uses the float type for weights in order to test graph parsing.
    """
    tree = nx.Graph()
    tree.add_nodes_from([(str(i), {"mass": float(i)}) for i in range(7)])
    tree.add_edges_from([("0", "1"), ("0", "2"),
                          ("1", "3"), ("1", "4"),
                          ("2", "5"), ("2", "6")])
    return tree
