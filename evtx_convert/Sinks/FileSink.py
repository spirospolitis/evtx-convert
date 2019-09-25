from .. import logging
from . import AbstractSink

"""
    File: FileSink.py
    Date: 09/2019
    Author: Spiros Politis
    Python: 3.6
"""

"""
     Context manager class for dumping to file.
"""


class FileSink(AbstractSink.AbstractSink):
    """
        Constructor
    """
    def __init__(self, file_name: str, file_format: str):
        AbstractSink.AbstractSink.__init__(self)

        self.__file_name = file_name
        self.__file_format = file_format
        self.__file = None


    """

    """
    def __enter__(self):
        logging.log.debug("FileSink:__enter__()")

        self.__file = open(self.__file_name.replace(".evtx", "." + self.__file_format), "w", encoding="utf-8")

        return self


    """

    """
    def __exit__(self, *args: object):
        logging.log.debug("FileSink:__exit__()")

        self.__file.close()


    def prepend(self, data: object):
        pass

    def append(self, data: object):
        pass

    """

    """
    def dump(self, data: object):
        logging.log.debug("FileSink:dump():data:{}".format(data))

        try:
            self.__file.write(data)
        except Exception as exception:
            logging.log.error("FileSink:dump():exception:{}".format(exception))


    """
        Properties
    """
    @property
    def file_name(self):
        return self.__file_name

    @property
    def file_format(self):
        return self.__file_format
    
    @property
    def file(self):
        return self.__file