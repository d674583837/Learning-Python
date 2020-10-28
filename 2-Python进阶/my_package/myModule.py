global_var = 100

class Student(object):
    def __init__(self,name):
        self.name = name
    
    def get_name(self):
        return self.name