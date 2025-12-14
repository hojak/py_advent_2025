from day11.network import Network


def test_init_network():
    network = Network("you: out")
    assert network.size() == 1


def test_find_the_only_path():
    network = Network("you: aaa\naaa: ccc\nbbb: aaa out\nccc: out")
    assert network.find_all_paths_from_to("you", "out") \
        == [["you", "aaa", "ccc", "out"]]


def test_find_number_of_possible_paths():
    network = Network('''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out''')
    
    assert network.find_number_of_possible_paths("you", "out") == 5
