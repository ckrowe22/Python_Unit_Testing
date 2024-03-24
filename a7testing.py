from Assignment7 import Areas


# Using fixture style for test methods

def setUpModule():
    print("In setUpModule()...")
    global area_obj
    area_obj = Areas()


def tearDownModule():
    print("In tearDownModule()...")
    global area_obj
    del area_obj


class TestClass01:

    @classmethod
    def setUpClass(cls):
        print("In setUpClass()...")

    def setUp(self):
        print("\nIn setUp()...")

    def test_case01(self):
        print("In test_case01()...")
        assert area_obj.areaCirc(5) == 79

    def test_case02(self):
        print("In test_case02()...")
        assert area_obj.areaSquare(4) == 16

    def test_case03(self):
        print("In test_case03()...")
        assert area_obj.areaRect(4, 5) == 20

    def test_case04(self):
        print("In test_case04()...")
        assert area_obj.areaTri(10, 4) == 20

    def test_case05(self):
        print("In test_case05()...")
        assert area_obj.areaParall(7, 5) == 35

    def test_case06(self):
        print("In test_case06()...")
        assert area_obj.areaEllipse(7, 6) == 132

    def tearDown(self):
        print("In tearDown()...")

    @classmethod
    def tearDownClass(cls):
        print("\nIn tearDownClass()...")
