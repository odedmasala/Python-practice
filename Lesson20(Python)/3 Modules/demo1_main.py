# Option 1

# import demo1_my_module
# demo1_my_module.do1()

# Option 2
# from demo1_my_module import do2
# do2()

# Option 2.2

print("demo1_main __name__:", __name__)

from demo1_my_module import *
do2()
# do2()