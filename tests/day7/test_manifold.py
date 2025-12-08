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
