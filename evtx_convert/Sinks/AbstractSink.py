from abc import ABC, abstractmethod

"""
    File: AbstractSink.py
    Date: 09/2019
    Author: Spiros Politis
    Python: 3.6
"""

"""
    Abstract base class for ingesting .evtx files.

    Implements the context manager interface.
"""

class AbstractSink(ABC):
    """
        Constructor.
    """
    def __init__(self):
        super().__init__()


    """
        Defines the __enter__ method of the context manager interface.

        :returns: Should return self.
    """
    @abstractmethod
    def __enter__(self):
        pass

    
    """
        Defines the __exit__ method of the context manager interface.

        :param args: method arguments.
    """
    @abstractmethod
    def __exit__(self, *args: object):
        pass


    """
        Defines the data dump interface.

        :param args: method arguments.
        :param event: .evtx event record.
    """
    @abstractmethod
    def dump(self, args: object, event: object):
        pass