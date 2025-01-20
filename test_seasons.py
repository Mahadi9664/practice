from seasons import check_birthday

def main():
    ...

def test_check_birthday():
    assert check_birthday('2001-12-17') == ("2001","12","17")
    assert check_birthday('2001-1-1') == "Invalid date"
    assert check_birthday('july 21, 2001') == "Invalid date"



if __name__ == "__main__":
    main()
