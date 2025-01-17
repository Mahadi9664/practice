from working import convert

def main():
    test_format()
    test_value()

def test_format():
    try:
        convert("cat")
        assert False
    except ValueError:
        pass  
    
    try:
        convert("13 am to 5 pm")
        assert False
    except ValueError:
        pass  

    assert convert("5 am to 3 pm") == "05:00 to 15:00"


def test_value():
    assert convert("1:30 am to 2:30 pm") == "01:30 to 14:30"
    assert convert("6 am to 3 pm") == "06:00 to 15:00"



if __name__ == "__main__":
    main()