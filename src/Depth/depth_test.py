import pytest
from .depth import Graph


@pytest.fixture
def simple_connected_graph():
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (2, 3), (3, 4)]
    return Graph(vertices, edges)


@pytest.fixture
def empty_graph():
    return Graph([], [])


@pytest.fixture
def single_node_graph():
    return Graph([1], [])


@pytest.fixture
def disconnected_graph():
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (3, 4)]
    return Graph(vertices, edges)


def test_dfs_traversal_simple_graph(simple_connected_graph):
    assert simple_connected_graph.dfs() == [1, 2, 3, 4]


def test_dfs_gen_yields_correct_order(simple_connected_graph):
    assert list(simple_connected_graph.dfs_gen()) == [1, 2, 3, 4]


def test_graph_is_iterable(simple_connected_graph):
    assert list(simple_connected_graph) == simple_connected_graph.dfs()


def test_iterator_matches_dfs_output(simple_connected_graph):
    it_result = list(simple_connected_graph)
    dfs_result = simple_connected_graph.dfs()
    assert it_result == dfs_result


def test_dfs_on_empty_graph(empty_graph):
    assert empty_graph.dfs() == []
    assert list(empty_graph) == []


def test_dfs_on_single_node(single_node_graph):
    assert single_node_graph.dfs() == [1]
    assert list(single_node_graph) == [1]


def test_dfs_on_disconnected_graph(disconnected_graph):
    result = disconnected_graph.dfs()
    assert result == [1, 2, 3, 4]


@pytest.mark.parametrize(
    "vertices, edges, expected_length",
    [
        ([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4)], 4),
        ([1], [], 1),
        ([], [], 0),
        ([1, 2, 3, 4], [(1, 2), (3, 4)], 4),
    ],
)
def test_dfs_output_length_parametrized(vertices, edges, expected_length):
    g = Graph(vertices, edges)
    assert len(g.dfs()) == expected_length
