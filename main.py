from choice_funcs import ChoiceFuncs
from dao.impl.card_dao_impl import CardDaoImpl
from service.impl.card_service_impl import CardServiceImpl
from service.util.impl.card_util_impl import CardUtilImpl

import argparse

parser = argparse.ArgumentParser("Choose type of the interface")
parser.add_argument("-r", "--refill", nargs=3, action="store", help='To refill money in card')
parser.add_argument("-c", "--check_amount_of_cash", nargs=2, action="store")
parser.add_argument("-a", "--add", nargs=3, action="store")
parser.add_argument("-t", "--transfer", nargs=4, action="store")
parser.add_argument("-w", "--withdraw", nargs=3, action="store")
parser.add_argument("-e", "--exit", action="store_true")
args = parser.parse_args()

if __name__ == '__main__':
    is_not_exit = True

    while is_not_exit:

        cardDao = CardDaoImpl()
        cardUtil = CardUtilImpl(cardDao)

        card_service = CardServiceImpl(cardUtil, cardDao)

        #python 3.8 doesnt provide matcher-case
        if args.add:
            card_service.add(ChoiceFuncs.first_choice(args.add[0], args.add[1], args.add[2]))
            is_not_exit = False
        elif args.refill:
            card_service.refill(ChoiceFuncs.second_choice(args.refill[0], args.refill[1], args.refill[2]))
            is_not_exit = False
        elif args.check_amount_of_cash:
            print(card_service.check_amount_of_cash(ChoiceFuncs.third_choice(args.check_amount_of_cash[0], args.check_amount_of_cash[1])))
            is_not_exit = False
        elif args.transfer:
            print(card_service.transfer(ChoiceFuncs.fourth_choice(args.transfer[0], args.transfer[1], args.transfer[2], args.transfer[3])))
            is_not_exit = False
        elif args.withdraw:
            print(card_service.withdraw(ChoiceFuncs.fifth_choice(args.withdrow[0], args.withdrow[1], args.withdrow[2])))
            is_not_exit = False
        elif args.exit:
            is_not_exit = False
