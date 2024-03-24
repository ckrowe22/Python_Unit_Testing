import pytest
from Assignment6 import Creditcard
from unittest.mock import Mock


@pytest.mark.parametrize("card_num,expected_luhn", [
    ('4532015112830366', 'Valid Credit Card'),
    ('5000123456789012', 'The credit card number you entered is invalid.'),
    ('3111111111111111', 'The credit card number you entered is invalid.')])
def test_luhn_check(card_num, expected_luhn):
    card = Creditcard(card_num)
    assert card.luhn_check() == expected_luhn


@pytest.mark.parametrize("card_num,expected_bank", [
    ('4532015112830366', 'Visa'),
    ('5000123456789012', 'Mastercard'),
    ('3111111111111111', 'American Express')])
def test_bank_check(card_num, expected_bank):
    card = Creditcard(card_num)
    assert card.bank_check() == expected_bank


@pytest.mark.parametrize("card_num,expected_bank_id", [
    ('4532015112830366', '53201'),
    ('5000123456789012', '00012'),
    ('3111111111111111', '11111')])
def test_bank_id(card_num, expected_bank_id):
    card = Creditcard(card_num)
    assert card.bank_id() == expected_bank_id


@pytest.mark.parametrize("card_num,expected_acct_num", [
    ('4532015112830366', '112830366'),
    ('5000123456789012', '456789012'),
    ('3111111111111111', '111111111')])
def test_acct_num(card_num, expected_acct_num):
    card = Creditcard(card_num)
    assert card.acct_num() == expected_acct_num


@pytest.mark.parametrize("bank_id,expected_bank_info", [
    ('53201', 'Bank Info 1'),
    ('00012', 'Bank Info 2'),
    ('11111', 'Bank Info 3')])
def test_get_bank_info(bank_id, expected_bank_info):
    # mocking because there is no database to pull info from
    mock_database = Mock()
    mock_database.info.return_value = expected_bank_info
    card = Creditcard(bank_id)
    assert card.get_bank_info(mock_database) == expected_bank_info
