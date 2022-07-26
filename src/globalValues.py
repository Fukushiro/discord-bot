black_list = []
owners = ['fukushiro#0449']
users_to_delete_message = []  # 'Sushikaze#9930'
users_chance_to_delete = []
recover_messages = True


def set_recover_manager(newValue):
    recover_messages = newValue
# Sushikaze#9930


# class SingletonMeta(type):
#     _instances = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(
#                 Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    recover_message = True
