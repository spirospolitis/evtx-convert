import logging

log = logging.getLogger('evtx_convert')
log.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.level = logging.DEBUG
formatter = logging.Formatter(fmt='%(asctime)s [%(name)10s] %(levelname)s %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
stream_handler.formatter = formatter

log.addHandler(stream_handler)
