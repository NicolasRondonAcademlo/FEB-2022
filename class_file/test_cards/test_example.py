
def test_ok():
    assert (1,2,3) == (1,2,3)

def test_fail():
    # True or Fasle -> True pasa -- False falla

    assert (1,2,3) == (3,2,1)