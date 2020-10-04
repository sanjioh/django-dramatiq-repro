from uuid import UUID

import dramatiq


class Klass:

    def __init__(self, value):
        self.value = value

    @classmethod
    def fromdict(cls, attrs):
        new_attrs = attrs.copy()
        new_attrs['value'] = UUID(attrs['value'])
        return cls(**new_attrs)


@dramatiq.actor
def a_task(attrs):
    Klass.fromdict(attrs)
