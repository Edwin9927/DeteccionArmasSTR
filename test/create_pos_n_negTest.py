import pytest
from src import load_images_neg as load
@pytest.mark.parametrize(
    "dire",
    [
        (""),
        ("/mnt/d/Development")
    ]
)
def test_create_pos_n_neg(dir):
    #self.assertEqual(True, False)  # add assertion here
    path = dir
    assert load.create_pos_n_neg(path) == None


