import unittest
from factory import NaanFactory

class Test(unittest.TestCase):
    factory = NaanFactory()
    
    # We want to be able to input water and flour to output dough
    # If this is not the case, then this test will fail
    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough("water", "flour"), "dough")
        self.assertNotEqual(self.factory.make_dough("water", "rice"), "dough")
    
    # We want to be able to bake our dough to create naan
    # The optimal time is 5 minutes, but allow 4 - 6 minutes
    # This function should only return True or False
    # depending on whether or not it was baked to satisfaction
    def test_bake_dough(self):
        self.assertEqual(self.factory.bake_dough("dough", 5), "naan")
        self.assertEqual(self.factory.bake_dough("dough", 7), "burnt naan")
        self.assertEqual(self.factory.bake_dough("dough", 3.9), "undercooked naan")

    # We should just be able to input water and flour as well as set the timing
    # for the baking and output naan
    def test_run_factory(self):
        self.assertEqual(self.factory.run_factory("water", "flour", 5), "naan")    