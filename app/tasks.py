from uuid import UUID

import dramatiq


class Klass:

    def __init__(self, value):
        self.value = value

    @classmethod
    def fromdict(cls, attrs):
        attrs['value'] = UUID(attrs['value'])
        return cls(**attrs)


@dramatiq.actor
def a_task(attrs):
    Klass.fromdict(attrs)
