import pytest 
from bank_app import deposit,withdraw,transfer,calculate_interest,check_loan_eligibility

@pytest.mark.parametrize("a,b,total",[
    (100,10,110)
])

def test_valid_d(a,b,total):
    assert deposit(a,b) == total

@pytest.mark.parametrize("a,b",[
    (100,-10)
])
def test_invalid_d(a,b):
    with pytest.raises(ValueError):
        deposit(a,b)


def test_valid_w():
    assert withdraw(100,50) == 50
def test_invalid_w():
    with pytest.raises(ValueError):
        withdraw(100,0)

def test_valid_t():
    result = transfer(1000,500,300) 
    assert result == (700,800)
def test_invalid_t():
    with pytest.raises(ValueError):
        transfer(1000,500,0)

def test_valid_c():
    assert calculate_interest(1,100,1) == 2
def test_invalid_c():
    with pytest.raises(ValueError):
        calculate_interest(-1,100,1)

@pytest.mark.parametrize("a,b,total",[
    (6000,750,True),
    (4000,750,False),
])
def test_val(a,b,total):
    assert check_loan_eligibility(a,b) == total