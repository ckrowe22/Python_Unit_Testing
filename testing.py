import pytest

def add(x, y=5):
    return x+y

@pytest.mark.parameterize("out, a, b", [(7, 2)])
def test_add(out, a, b):
    assert Calculator.add(a,b) == out

# if __name__ == '__main__':
#     unittest.main()