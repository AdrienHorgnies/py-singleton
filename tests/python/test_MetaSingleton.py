import alone.MetaSingleton


def test_init():
    class Sad(metaclass=alone.MetaSingleton):
        pass

    class Happy(metaclass=alone.MetaSingleton):
        pass

    assert Sad() is Sad()
    assert Happy() is not Sad()
    assert Happy() is Happy()
