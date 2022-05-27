CREATE SEQUENCE IF NOT EXISTS seq_card_id INCREMENT 1 START 1 OWNED BY card.id;

CREATE UNIQUE INDEX IF NOT EXISTS indx_card_number ON card(card_number) INCLUDE (pin);

CREATE TABLE card(
    id              int            DEFAULT nextval('seq_card_id'),
    card_number     varchar(255)                                    NOT NULL UNIQUE,
    pin             varchar(255)                                    NOT NULL UNIQUE,
    amount_of_cash  decimal        DEFAULT 0,
    expiration_date varchar(255)                                    NOT NULL CHECK(expiration_date >= to_char(current_timestamp, 'MM-YY'))
);
