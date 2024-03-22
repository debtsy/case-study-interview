from flask import jsonify
from models import CardHolder, CreditCard
from base_controller import BaseController, db


class CardHolderController(BaseController):
    model = CardHolder

    def get_card_holders(self, search_params):
        return self.get_all(**search_params)

    def get_card_holders_by_name(self, name):
        card_holders = CardHolder.query.filter(CardHolder.name.ilike(f'%{name}%')).all()
        return jsonify([card_holder.to_dict() for card_holder in card_holders])

    def get_card_holders_by_card_issuance_date(self, issuance_date):
        card_holders = CardHolder.query.join(CreditCard).filter(CreditCard.issuance_date == issuance_date).all()
        return jsonify([card_holder.to_dict() for card_holder in card_holders])

    def get_card_holder_details(self, card_holder_id):
        card_holder = CardHolder.query.get(card_holder_id)
        if card_holder:
            return jsonify(card_holder.to_dict())
        else:
            return jsonify({"error": "Card holder not found"}), 404


card_holder_controller = CardHolderController()
