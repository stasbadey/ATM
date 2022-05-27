from choice_funcs import ChoiceFuncs
from dao.impl.card_dao_impl import CardDaoImpl
from service.impl.card_service_impl import CardServiceImpl
from service.util.impl.card_util_impl import CardUtilImpl

if __name__ == '__main__':
    is_not_exit = True

    while is_not_exit:
        print("1. Add card "
              "\n2. Refill card "
              "\n3. Check amount of cash of card "
              "\n4. Transfer cash to another card "
              "\n5. Withdraw cash from card"
              "\n0. Exit")

        choice = input()

        cardDao = CardDaoImpl()
        cardUtil = CardUtilImpl(cardDao)

        card_service = CardServiceImpl(cardUtil, cardDao)

        #python 3.8 doesnt provide matcher-case
        if choice == '1':
            card_service.add(ChoiceFuncs.first_choice())
        elif choice == '2':
            card_service.refill(ChoiceFuncs.second_choice())
        elif choice == '3':
            print(card_service.check_amount_of_cash(ChoiceFuncs.third_choice()))
        elif choice == '4':
            print(card_service.transfer(ChoiceFuncs.fourth_choice()))
        elif choice == '5':
            print(card_service.withdraw(ChoiceFuncs.fifth_choice()))
        elif choice == '0':
            is_not_exit = False
