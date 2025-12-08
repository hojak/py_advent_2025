from day7.manifold import Manifold


def test_simple_beam():
    manifold = Manifold(".S.")
    manifold.fire_beam()

    assert manifold.get_beam_layout() == ".S."
    assert manifold.get_number_of_splitted_beams() == 0
