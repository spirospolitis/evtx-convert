import json

import Evtx.Evtx as evtx

from .. import logging
from . import AbstractConverter

"""
    File: ToJSON.py
    Date: 09/2019
    Author: Spiros Politis
    Python: 3.6
"""

"""
    Implements a .evtx to JSON converter.
"""


class ToJSON(AbstractConverter.AbstractConverter):
    """
        Constructor
    """
    def __init__(self):
        AbstractConverter.AbstractConverter.__init__(self)

        self.__evtx = None


    """
        Converts a .evtx fole to JSON.
        
        :param evtx: .evtx file
    """
    def convert(self, evtx: object):
        import json

        self._event_counter = 0

        # Total event counter.
        json_events_count = sum(1 for _ in super()._iter_evtx_to_xml(evtx))

        # Iterate through evnt log records.
        for xml in super()._iter_evtx_to_xml(evtx):
            self._event_counter += 1

            # Convert each log record to JSON.
            try:
                # If first JSON element, prepend a "{".
                if self._event_counter == 1:
                    json_event = ""
                    json_event += "{"
                    json_event += "\n"
                    json_event += "\"" + str(self._event_counter) + "\"" + ":" + json.dumps(super()._xml_to_json(xml), indent=4)

                # If last event element, append a "}".
                if self._event_counter == json_events_count:
                    json_event = ""
                    json_event += "\"" + str(self._event_counter) + "\"" + ":" + json.dumps(super()._xml_to_json(xml), indent=4)
                    json_event += "\n"
                    json_event += "}"

                if self._event_counter > 1 and self._event_counter < json_events_count:
                    json_event = ""
                    json_event += "\"" + str(self._event_counter) + "\"" + ":" + json.dumps(super()._xml_to_json(xml), indent=4)

                # Up until the last element, append a ",".
                if self._event_counter < json_events_count:
                    json_event += ","

                yield json_event
            except Exception as exception:
                self._error_counter += 1
                
                logging.log.error("ToJSON:convert():exception:{}".format(exception))
            else:
                self._success_counter += 1

        super()._verbose(evtx)


    """
        Properties
    """
    @property
    def evtx(self):
        return self.__evtx
