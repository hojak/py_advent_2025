from day11.network import Network


def test_init_network():
    network = Network("you: out")
    assert network.size() == 1
