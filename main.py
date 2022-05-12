from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod, abstractproperty


class Connector(ABC):
    @abstractmethod
    def connect(self):
        pass


class SQLConnector(Connector):
    
    def connecting(self):
        pass

sqlc = SQLConnector()
