from day7.manifold import Manifold


def test_simple_beam():
    manifold = Manifold(".S.")
    manifold.fire_beam()

    assert manifold.get_beam_layout() == ".S."
    assert manifold.get_number_of_splitted_beams() == 0


def test_beam_expands_straight_forward_from_start():
    manifold = Manifold(".S.\n...")
    manifold.fire_beam()

    assert manifold.get_beam_layout() == ".S.\n.|."
    assert manifold.get_number_of_splitted_beams() == 0


def test_beam_expands_straight_forward():
    manifold = Manifold(".S.\n...\n...\n...")
    manifold.fire_beam()

    assert manifold.get_beam_layout() == ".S.\n.|.\n.|.\n.|."
    assert manifold.get_number_of_splitted_beams() == 0


def test_beam_is_splitted():
    manifold = Manifold(".S.\n...\n.^.\n...")
    manifold.fire_beam()

    assert manifold.get_beam_layout() == ".S.\n.|.\n|v|\n|.|"
    assert manifold.get_number_of_splitted_beams() == 1


def test_replace_char_at():
    assert Manifold.replace_char_at("abcde", 2, "X") == "abXde"
    assert Manifold.replace_char_at("abcde", 0, "X") == "Xbcde"
    assert Manifold.replace_char_at("abcde", 4, "X") == "abcdX"


def test_number_of_timelines_for_a_single_beam():
    manifold = Manifold(".S.\n...")
    manifold.fire_beam()

    assert manifold.get_number_of_timelines() == 1


def test_number_of_timelines_for_a_splitted_beam():
    manifold = Manifold(".S.\n...\n.^.\n...")
    manifold.fire_beam()

    assert manifold.get_number_of_timelines() == 2


def test_timeslines_for_joining_beam_paths():
    manifold = Manifold("..S..\n.....\n..^..\n.....\n.^.^.\n.....")
    manifold.fire_beam()

    print(manifold.timelines_per_row)

    assert manifold.get_beam_layout() == "..S..\n..|..\n.|v|.\n.|.|.\n|v|v|\n|.|.|"
    assert manifold.get_number_of_timelines() == 4

    assert len(manifold.timelines_per_row) == len(manifold.beam_layout)
