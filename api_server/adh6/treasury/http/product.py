# coding=utf-8
import typing as t

from adh6.constants import DEFAULT_LIMIT, DEFAULT_OFFSET
from adh6.decorator import log_call, with_context
from adh6.treasury.product_manager import ProductManager


class ProductHandler:
    def __init__(self, product_manager: ProductManager):
        self.product_manager = product_manager

    @with_context
    @log_call
    def search(self, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, terms=None):
        result, total_count = self.product_manager.search(limit=limit, offset=offset, terms=terms)
        headers = {
            "X-Total-Count": str(total_count),
            'access-control-expose-headers': 'X-Total-Count'
        }
        result = list(map(lambda x: x.to_dict(), result))
        return result, 200, headers

    @with_context
    @log_call
    def get(self, id_: int):
        return self.product_manager.get_by_id(id=id_).to_dict(), 200

    @with_context
    @log_call
    def buy_post(self, member_id: int, payment_method: int, products: t.List[int]):
        self.product_manager.buy(member_id, payment_method, products)
        return None, 204
