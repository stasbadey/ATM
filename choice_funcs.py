from decimal import Decimal
from typing import List, Union

from dateutil import parser
from model.entity.card import Card


class ChoiceFuncs:
    def __init__(self):
        pass

    @staticmethod
    def first_choice() -> Card:
        print("Pass a card number, expiration date(YY-MM) and pin")
        card_number = input()
        expiration_date = parser.parse(input()).strftime('%m-%y')
        pin = input()

        return Card(card_number, pin, expiration_date)

    @staticmethod
    def second_choice() -> List[Union[str, Decimal]]:
        print("Put the card(type card number and pin)")
        card_number = input()
        pin = input()

        print("Put the cash")
        amount = Decimal(input())

        return [card_number, pin, amount]

    @staticmethod
    def third_choice() -> List[str]:
        print("Put the card(type card number and pin)")
        card_number = input()
        pin = input()

        return [card_number, pin]

    @staticmethod
    def fourth_choice() -> List[Union[str, Decimal]]:
        print("Put the card(type card number and pin)")
        card_number = input()
        pin = input()

        print("Type amount of cash to transfer")
        amount_of_cash_to_transfer = Decimal(input())

        print("Type participant card number")
        participant_card_number = input()

        return [card_number, pin, amount_of_cash_to_transfer, participant_card_number]

    @staticmethod
    def fifth_choice() -> List[Union[str, Decimal]]:
        print("Put the card(type card number and pin)")
        card_number = input()
        pin = input()

        print("Type amount of cash to withdraw")
        amount_of_cash_to_withdraw = Decimal(input())

        return [card_number, pin, amount_of_cash_to_withdraw]
