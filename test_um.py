from um import count

def main():
    test_upper_lower_cases()
    test_word_with_um()
    test_sorrounded_by_space()

def test_upper_lower_cases():
    assert count("hello um UM") == 2

def test_word_with_um():
    assert count("yum") == 0


def test_sorrounded_by_space():
    assert count("hello um world") == 1
    assert count("um?") == 1





if __name__ == "__main__":
    main()