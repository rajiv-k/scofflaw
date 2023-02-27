from condition import Wife, Eq, Lt, Gt

class TestCond():
    def teeeest_Wife(self):
        wife = Wife("Beautiful", "foo")
        got = wife()
        assert got is True, "Wife is always right"

    def test_Eq(self):
        eq = Eq(5, 5)
        assert eq() is True, "5 is equal to 5"

    def test_not_Eq(self):
        eq = Eq(4, 5)
        assert eq() is False, "4 is not equal to 5"

    def test_Lt(self):
        lt = Lt(3, 5)
        assert lt() is True, "3 is less than 5"

    def test_not_Lt(self):
        lt = Lt(6, 5)
        assert lt() is False, "6 is not less than 5"

    def test_Gt(self):
        gt = Gt(8, 5)
        assert gt() is True, "8 is greater than 5"

    def test_not_Gt(self):
        gt = Gt(2, 5)
        assert gt() is False, "2 is not greater than than 5"

