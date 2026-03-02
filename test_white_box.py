import pytest 
from bank_app import deposit,withdraw,transfer,calculate_interest,check_loan_eligibility

def test_valid_d():
    assert deposit(100,50) == 150
def test_invalid_d():
    with pytest.raises(ValueError):
        deposit(100,0)
def test_invalid_de():
    with pytest.raises(ValueError):
        deposit(100,-1)

def test_valid_w():
    assert withdraw(100,50) == 50
def test_invalid_w():
    with pytest.raises(ValueError):
        withdraw(100,0)
def test_invalid_we():
    with pytest.raises(ValueError):
        withdraw(100,-1)
def test_invalid_wee():
    with pytest.raises(ValueError):
        withdraw(90,100)

def test_valid_t():
    result = transfer(1000,500,300) 
    assert result == (700,800)
def test_invalid_t():
    with pytest.raises(ValueError):
        transfer(1000,500,0)
def test_invalid_te():
    with pytest.raises(ValueError):
        transfer(1000,500,-1)
def test_invalid_tee():
    with pytest.raises(ValueError):
        transfer(1000,500,2000)

def test_valid_c():
    assert calculate_interest(1,100,1) == 2
def test_invalid_c():
    with pytest.raises(ValueError):
        calculate_interest(-1,100,1)
def test_invalid_ce():
    with pytest.raises(ValueError):
        calculate_interest(1,-100,1)
    
def test_val():
    assert check_loan_eligibility(6000,750) == True
def test_inval1():
    assert check_loan_eligibility(4000,750) == False
def test_inval2():
    assert check_loan_eligibility(6000,50) == False
def test_inval3():
    assert check_loan_eligibility(4000,50) == False