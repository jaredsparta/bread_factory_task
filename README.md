# Task

![](images/t1.png)

![](images/t2.png)

![](images/t3.png)

**User stories**
```
#1
As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

#2
As a user, I can use the bake dough with dough to get naan.

#3
As a user, I can user the run factory with water and flour and get naan.
```

**My interpretation**
- From my understanding, I will create a Naan Factory class
- This will have the option of manually doing the two methods:
    1. Making dough
    2. Baking dough
- But the factory should also have the option to simply run by itself with a method. All one would need to do is simply input water, flour and set the baking time.
- This is what I implemented

**Explanation**
- We must apply TDD in this task
- Firstly, we must create a test class

- Run the test using ```pytest```
```

================================================================================================= short test summary info ================================================================================================== 
ERROR test_factory.py - NameError: name 'NaanFactory' is not defined
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
===================================================================================================== 1 error in 0.46s =====================================================================================================
```

- There are failures and we must then program to fix these errors
- Create a ```factory.py``` file
- Create a ```NaanFactory``` class inside it:
```python
    Class NaanFactory:
    pass
```
- Running ```pytest``` again yields:
```
================================================================================================= short test summary info ==================================================================================================
FAILED test_factory.py::Test::test_bake_dough - AttributeError: 'NaanFactory' object has no attribute 'bake_dough'
FAILED test_factory.py::Test::test_make_dough - AttributeError: 'NaanFactory' object has no attribute 'make_dough'
FAILED test_factory.py::Test::test_run_factory - AttributeError: 'NaanFactory' object has no attribute 'run_factory'
```

- We must now add the required methods inside the class:
```python
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
        self.bake_dough(bake_what, time)
```

- We can now run the test again. We use ```pytest -v``` to get more information:
```
PS C:\Users\Jared\Documents\GitHub\active\bread_factory_task> pytest -v
=================================================================================================== test session starts ==================================================================================================== 
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- c:\users\jared\appdata\local\programs\python\python39\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Jared\Documents\GitHub\active\bread_factory_task
collected 3 items                                                                                                                                                                                                            

test_factory.py::Test::test_bake_dough PASSED                                                                                                                                                                         [ 33%] 
test_factory.py::Test::test_make_dough PASSED                                                                                                                                                                         [ 66%] 
test_factory.py::Test::test_run_factory PASSED                                                                                                                                                                        [100%] 

==================================================================================================== 3 passed in 0.30s ===================================================================================================== 
```