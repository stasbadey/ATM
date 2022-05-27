import unittest

from dao.impl.card_dao_impl import CardDaoImpl
from model.entity.card import Card
from service.util.impl.card_util_impl import CardUtilImpl


class CardUtilTest(unittest.TestCase):

    def test_is_exist_must_pass(self):
        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)

        card: Card = Card('9846574839201627', '7568', '04-22')

        self.assertFalse(card_util.is_exists(card))

    def test_check_length_must_pass(self):
        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)

        card_number: str = '9846574839201627'
        pin: str = '7563'

        raised: bool = False

        try:
            card_util.check_length(pin, card_number)
        except:
            raised: bool = True

        self.assertFalse(raised)

    def test_check_length_must_raise_exception(self):
        card_dao = CardDaoImpl()
        card_util = CardUtilImpl(card_dao)

        card_number: str = '9846574839201627323'
        pin: str = '7563'

        raised: bool = False

        try:
            card_util.check_length(pin, card_number)
        except:
            raised: bool = True

        self.assertTrue(raised)
