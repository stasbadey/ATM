from decimal import Decimal
from typing import List, Union

from dateutil import parser

from model.entity.card import Card


class ChoiceFuncs:
    def __init__(self):
        pass

    @staticmethod
    def first_choice(card_number, expiration_date, pin) -> Card:

        return Card(card_number, pin, expiration_date)

    @staticmethod
    def second_choice(card_number, pin, amount) -> List[Union[str, Decimal]]:

        return [card_number, pin, amount]

    @staticmethod
    def third_choice(card_number, pin) -> List[str]:

        return [card_number, pin]

    @staticmethod
    def fourth_choice(card_number, pin, amount_of_cash_to_transfer, participant_card_number) -> List[Union[str, Decimal]]:

        return [card_number, pin, amount_of_cash_to_transfer, participant_card_number]

    @staticmethod
    def fifth_choice(card_number, pin, amount_of_cash_to_withdraw) -> List[Union[str, Decimal]]:

        return [card_number, pin, amount_of_cash_to_withdraw]
