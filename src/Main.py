from opencv_project.src.Bisection import Bisection
from opencv_project.src.spce import Spliter


class Main:
    def __int__(self):
        bisect = Bisection()
        bisect.PickBisectionMatrix()
        spliter = Spliter()
        spliter.ShowSpliterPicture()


p = Main()
p.__int__()
