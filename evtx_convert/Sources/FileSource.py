import importlib
import os
import glob
import json

from .. import logging
from . import AbstractSource

"""
    File: FileSource.py
    Date: 09/2019
    Author: Spiros Politis
    Python: 3.6
"""

"""
    Implements a directory / file source.
"""


class FileSource(AbstractSource.AbstractSource):
    """
        Constructor
    """
    def __init__(self):
        AbstractSource.AbstractSource.__init__(self)

        self.__directory = None
        self.__files = []


    """
        Each evtx file is first converted to XML using python-evtx module.
        Next, the XML output is converted to JSON using xmljson (badgerfish).
    """
    def __process_files(self, evtx_files: []):
        self.__files = evtx_files

        logging.log.debug("FileSource:__process_files:files:{}".format(self.__files))

        for evtx_file in evtx_files:
            if evtx_file.endswith(".evtx"):
                logging.log.debug("FileSource:__process_files:file:{}".format(evtx_file))

                yield evtx_file


    """

    """
    def __process_directory(self, directory: str):
        self.__directory = directory
        
        logging.log.debug("FileSource:__process_directory:directory:{}".format(self.__directory))

        return self.__process_files(glob.glob(os.path.join(self.__directory, "*.evtx")))


    """

    """
    def ingest(self, args: object):
        if args.__contains__("directory"):
            yield self.__process_directory(args.directory)

        if args.__contains__("files"):
            yield self.__process_files(args.files)


    """
        Properties
    """
    @property
    def directory(self):
        return self.__directory

    @property
    def files(self):
        return self.__files