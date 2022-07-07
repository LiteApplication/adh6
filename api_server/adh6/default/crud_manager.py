from typing import Optional, Tuple
from adh6.constants import DEFAULT_LIMIT, DEFAULT_OFFSET
from adh6.exceptions import IntMustBePositive
from adh6.default.decorator.log_call import log_call
from adh6.default.decorator.auto_raise import auto_raise
from adh6.authentication.security import uses_security
from adh6.default.crud_repository import CRUDRepository


class CRUDManager:

    def __init__(self, repository: CRUDRepository, abstract_entity, not_found_exception):
        self.repository = repository
        self.abstract_entity = abstract_entity
        self.not_found_exception = not_found_exception

    @log_call
    @auto_raise
    @uses_security("read", is_collection=True)
    def search(self, ctx, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, terms=None, **kwargs) -> Tuple[list, int]:
        if limit < 0:
            raise IntMustBePositive('limit')

        if offset < 0:
            raise IntMustBePositive('offset')

        return self._search(ctx, limit=limit,
                            offset=offset,
                            terms=terms,
                            **kwargs)

    def _search(self, ctx, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, terms=None, **kwargs) -> Tuple[list, int]:
        return self.repository.search_by(ctx, limit=limit,
                                         offset=offset,
                                         terms=terms,
                                         **kwargs)

    @log_call
    @auto_raise
    def get_by_id(self, ctx, id: int):
        result = self.repository.get_by_id(ctx, id)
        @uses_security("read", is_collection=False)
        def _get_by_id(cls, ctx, filter_=None):
            return filter_
        return _get_by_id(self, ctx, filter_=result)

    @log_call
    @auto_raise
    def update_or_create(self, ctx, obj, id: Optional[int] = None):
        current_object = None
        if id is not None:
            current_object = self.repository.get_by_id(ctx, id)

        if current_object is None:
            @uses_security("create", is_collection=True)
            def _create(cls, ctx, filter_=None):
                new_object = self.repository.create(ctx, filter_)
                return new_object, True
            return _create(self, ctx, filter_=obj)
        else:
            obj.id = current_object.id

            @uses_security("update", is_collection=False)
            def _update(cls, ctx, filter_=None):
                return self.repository.update(ctx, filter_, override=True), False
            return _update(self, ctx, filter_=obj)

    @log_call
    @auto_raise
    def partially_update(self, ctx, obj, id: int, override=False):
        current_object = self.repository.get_by_id(ctx, id)
        print(current_object)
        obj.id = id
        @uses_security("update", is_collection=False)
        def _partially_update(cls, ctx, filter_=None):
            return self.repository.update(ctx, obj, override=override), False

        return _partially_update(self, ctx, filter_=current_object)

    @log_call
    @auto_raise
    def delete(self, ctx, id: int):
        current_object = self.repository.get_by_id(ctx, id)
        print(current_object)
        @uses_security("delete", is_collection=False)
        def _delete(cls, ctx, filter_=None):
            self.repository.delete(ctx, id)
        return _delete(self, ctx, filter_=current_object)
