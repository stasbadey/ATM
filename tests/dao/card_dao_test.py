import unittest
from decimal import Decimal

from dao.impl.card_dao_impl import CardDaoImpl
from model.entity.card import Card


class CardDaoTest(unittest.TestCase):
    def test_find_all_card_must_pass(self):
        card_dao = CardDaoImpl()

        self.assertIsNotNone(card_dao.find_all_card())

    def test_save_card_must_pass(self):
        card_dao = CardDaoImpl()

        card: Card = Card('9586758493720263', '8556', '05-25')

        self.assertIsNone(card_dao.save_card(card))

    def test_card_by_card_number_and_pin(self):
        card_dao = CardDaoImpl()

        card_number: str = '0921092109210921'
        pin: str = '0921'

        self.assertIsNotNone(card_dao.find_card_by_card_number_and_pin(card_number, pin))

    def test_update_cards_amount(self):
        card_dao = CardDaoImpl()

        card_number: str = '0921092109210921'
        amount: Decimal = Decimal('30')

        raised: bool = False

        try:
            card_dao.update_cards_amount(amount, card_number)
        except:
            raised: bool = True

        self.assertFalse(raised)

    def test_find_amount_of_cash_by_card_number_and_pin(self):
        card_dao = CardDaoImpl()

        card_number: str = '0921092109210921'
        pin: str = '0921'

        self.assertIsNotNone(card_dao.find_amount_of_cash_by_card_number_and_pin(card_number, pin))

    def test_transfer_cash_from_one_card_to_participant_card(self):
        card_dao = CardDaoImpl()

        card_number: str = '0921092109210921'
        pin: str = '0921'
        amount: Decimal = Decimal(1)
        participant_card_number: str = '0987098709870987'

        self.assertIsNotNone(card_dao.transfer_cash_from_one_card_to_participant_card(
            [card_number, pin, amount, participant_card_number]))

    def test_withdraw_cash_from_card(self):
        card_dao = CardDaoImpl()

        card_number: str = '0921092109210921'
        pin: str = '0921'
        amount: Decimal = Decimal(1)

        self.assertIsNotNone(card_dao.withdraw_cash_from_card(amount, card_number, pin))