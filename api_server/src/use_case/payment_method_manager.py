# coding=utf-8
from src.entity.abstract_payment_method import AbstractPaymentMethod
from src.exceptions import PaymentMethodNotFoundError
from src.use_case.crud_manager import CRUDManager
from src.use_case.interface.payment_method_repository import PaymentMethodRepository


class PaymentMethodManager(CRUDManager):
    def __init__(self, payment_method_repository: PaymentMethodRepository):
        super().__init__('payment_method', payment_method_repository, AbstractPaymentMethod, PaymentMethodNotFoundError)
        self.payment_method_repository = payment_method_repository

    def search_access_control_function(self, ctx, roles, f, args, kwargs):
        return args, kwargs, True
