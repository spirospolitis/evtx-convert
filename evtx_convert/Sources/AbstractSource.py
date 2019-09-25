from abc import ABC, abstractmethod

"""
    File: AbstractSource.py
    Date: 09/2019
    Author: Spiros Politis
    Python: 3.6
"""

"""
    Abstract base class for ingesting .evtx files.
"""

class AbstractSource(ABC):
    """
        Constructor
    """
    def __init__(self):
        super().__init__()

    """
        Defines the data ingestion interface.
    """
    @abstractmethod
    def ingest(self, args: object):
        pass