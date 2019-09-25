from abc import ABC, abstractmethod

import xml.etree.ElementTree as et
import Evtx.Evtx
import xmljson

from .. import logging

"""
    File: AbstractConverter.py
    Date: 09/2019
    Author: Spiros Politis
    Python: 3.6
"""

"""
    Abstract base class for classes that implement a .evtx converter interface.
"""

class AbstractConverter(ABC):
    """
        Constructor.
    """
    def __init__(self):
        super().__init__()

        # Total event counter
        self._event_counter = 0

        # Successful event counter
        self._success_counter = 0

        # Error event counter
        self._error_counter = 0

    
    """
        Removes namespace from all elements.

        :param xml_tree: XML ElementTree element.

        :returns: XML ElementTree element with namespace removed.
    """
    def __remove_namespace(self, xml_tree: object):
        for element in xml_tree.getiterator():
            try:
                if element.tag.startswith("{"):
                    element.tag = element.tag.split("}")[1]
            except Exception as exception:
                logging.log.error("AbstractConverter:__remove_namespace():exception:{}".format(exception))

        return xml_tree

    
    """
        XML to JSON using Badgerfish.

        :param xml_str: XML string representation.

        :returns: JSON object.
    """
    def _xml_to_json(self, xml_str: str):
        """
            Convert string XML (after striping namespace) output from evtx.Evtx to XML tree object

            :param xml_str: string

            :returns: xml ElementTree Element
        """
        try:
            xml_data = self.__remove_namespace(et.fromstring(str(xml_str)))
            json_data = xmljson.badgerfish.data(xml_data)
        except Exception as exception:
            logging.log.error("AbstractConverter:_xml_to_json:exception:{}".format(exception))
        else:
            return json_data


    """
        Generator function to read events from evtx file and convert to XML.

        :param evtx_file: file path string.

        :returns: generator to XML string representation of evtx event.
    """
    def _iter_evtx_to_xml(self, evtx: object):
        try:
            with Evtx.Evtx.Evtx(evtx) as evtx_entry:
                # Process each log entry and return its XML representation.
                for record in evtx_entry.records():
                    try:
                        yield record.xml()
                    except Exception as exception:
                        logging.log.error("Failed to convert EVTX to XML for {}. Error: {}".format(evtx, exception))
        except Exception as exception:
            logging.log.error("AbstractConverter:_iter_evtx_to_xml:exception:{}".format(exception))

    """ 
        Log stats per .evtx file.

        :param evtx: .evtx file.
    """
    def _verbose(self, evtx: object):
        logging.log.info({
            "file": evtx, 
            "total events": self._event_counter, 
            "succesful events": self._success_counter,
            "failed events": self._error_counter
        })

    """
        Defines the converter interface.

        :param evtx: .evtx file.
    """
    @abstractmethod
    def convert(self, evtx: object):
        pass
