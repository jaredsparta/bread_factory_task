class NaanFactory:
    # Given two inputs, this will either make dough or not dough
    def make_dough(self, input1, input2):
        ingredients = [input1, input2]
        if "water" in ingredients and "flour" in ingredients:
            return "dough"
        else:
            return "not dough"

    # This will bake dough
    def bake_dough(self, input, time):
        if input != "dough":
            return "This oven only bakes dough!"

        if time < 4:
            return "undercooked naan"
        
        if 4 <= time <= 6:
            return "naan"

        if time > 6:
            return "burnt naan"

    # This will concatenate both functions into one
    def run_factory(self, input1, input2, time):
        bake_what = self.make_dough(input1, input2)
        r = self.bake_dough(bake_what, time)
        return r
        
f = NaanFactory()
d = f.make_dough("water", "flour")
print(d)
d_b = f.bake_dough(d, 5)
print(d_b)
print(f.run_factory("flour", "water", 5))