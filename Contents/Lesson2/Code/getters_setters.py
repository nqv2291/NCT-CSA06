
class Dog:
    
    def __init__(self, name):
        self.__name = name
        
    @property
    def name(self):
        """ this method is called by dog.name """
        return self.__name
    
    @name.setter
    def name(self, name):
        """ this method is called by dog.name = new_name """
        self.__name = name
    
    @name.deleter
    def name(self):
        """ this method is called by del dog.name """
        self.__name = None

