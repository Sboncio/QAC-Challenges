from programs import string_gen

def test_string_type():
    assert type(string_gen()) == str

def test_string_len():
    assert len(string_gen()) == 5

def test_string_case():
    assert string_gen().islower() == True
