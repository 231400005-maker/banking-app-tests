import pytest 
from bank_app import transfer,calculate_interest

def test_valid_t():
    result = transfer(1000,500,300) 
    assert result == (700,800)
def test_invalid_t():
    with pytest.raises(ValueError):
        transfer(1000,500,0)
def test_combine():
    balance = 1000
    balance_from,balance_to = transfer(balance,500,300) 
    assert round(calculate_interest(balance_from,100,1),2) == 1400.00