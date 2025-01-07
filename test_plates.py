from plates import is_valid

def main():
    test_max_min()
    test_two_letters()
    test_middle()
    test_first()
    test_punc()

def test_max_min():
    assert is_valid("Bw50000") == False
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEF") == True


def test_two_letters():
    assert is_valid("AB") == True
    assert is_valid("1AB") == False
    assert is_valid("A1") == False
    assert is_valid("123") == False

def test_middle():
    assert is_valid("AA1A") == False
    assert is_valid("AA1A") == False

def test_first():
    assert is_valid("Cs50") == True
    assert is_valid("cs05") == False

def test_punc():
    assert is_valid("P13.12") == False
    assert is_valid("p13!14") == False
    assert is_valid("pp11 3") == False

if __name__ == "__main__":
    main()
    