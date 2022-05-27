import decimal
import unittest
from decimal import Decimal

from dao.impl.card_dao_impl import CardDaoImpl
from model.entity.card import Card
from service.impl.card_service_impl import CardServiceImpl
from service.util.impl.card_util_impl import CardUtilImpl


class CardServiceTest(unittest.TestCase):
    def test_add_must_pass(self):
        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)
        card_service = CardServiceImpl(card_util, card_dao)

        card: Card = Card('9846574834204427', '7228', '04-22')

        raised: bool = False

        try:
            card_service.add(card)
        except:
            raised: bool = True

        self.assertFalse(raised)

    def test_add_must_raise_exception(self):
        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)
        card_service = CardServiceImpl(card_util, card_dao)

        card: Card = Card('0921092109210921', '0921', '04-22')

        raised: bool = False

        try:
            card_service.add(card)
        except:
            raised: bool = True

        self.assertTrue(raised)

    def test_refill_must_pass(self):
        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)
        card_service = CardServiceImpl(card_util, card_dao)

        card_number: str = '0921092109210921'
        pin: str = '0921'
        amount: Decimal = Decimal(30)

        raised: bool = False

        try:
            card_service.refill([card_number, pin, amount])
        except:
            raised: bool = True

        self.assertFalse(raised)

    def test_check_amount_of_cash_must_pass(self):
        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)
        card_service = CardServiceImpl(card_util, card_dao)

        card_number: str = '0921092109210921'
        pin: str = '0921'
        amount: Decimal = Decimal(30)

        expected_amount: Decimal = Decimal('30')

        self.assertEqual(expected_amount, card_service.check_amount_of_cash([card_number, pin, amount]))

    def test_transfer_must_pass(self):
        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)
        card_service = CardServiceImpl(card_util, card_dao)

        card_number: str = '0921092109210921'
        pin: str = '0921'
        amount: Decimal = Decimal(1)
        participant_card_number: str = '0987098709870987'

        return self.assertIsNotNone(card_service.transfer([card_number, pin, amount, participant_card_number]))

    def test_withdraw_must_pass(self):
        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)
        card_service = CardServiceImpl(card_util, card_dao)

        card_number: str = '0921092109210921'
        pin: str = '0921'
        amount: Decimal = Decimal(1)

        self.assertIsNotNone(card_service.withdraw([card_number, pin, amount]))
