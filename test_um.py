from um import count
def test_count():
    assert count("hello, um, world") == 1
    assert count("um, yummy, um, um") == 3
    assert count("The quick brown fox.") == 0
