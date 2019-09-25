import argparse
import logging

from evtx_convert.logging import log, stream_handler
from evtx_convert.Sources import *
from evtx_convert.Converters import *
from evtx_convert.Sinks import *


"""
    Creates and parses command line arguments.
"""
def argument_parser():
    # Default argument parser.
    parser = argparse.ArgumentParser(add_help=False, description="Convert Windows .evtx sources to other formats")
    parser.add_argument('--source', '-i', help=".evtx source", type=str, required=True)
    parser.add_argument('--sink', '-o', help=".evtx sink", type=str, required=True)
    parser.add_argument('--converter', '-c', help="Format converter", type=str, required=True)
    parser.add_argument('--help', '-h', help="This help message.", action='help')
    parser.add_argument('--loglevel', '-v', help="Log level", choices=[0, 10, 20, 30, 40, 50], default=20, type=int)
    subparsers = parser.add_subparsers()

    # Argument parser for single .evtx file.
    process_files_parser = subparsers.add_parser('process_files')
    process_files_parser_group = process_files_parser.add_argument_group(title="Process .evtx files")
    process_files_parser_group.add_argument('--files', '-f', help=".evtx file", nargs='+', required=True)
    process_files_parser_group.set_defaults(func=exec_pipeline)

    # Argument parser for folder containing .evtx files.
    process_directory_parser = subparsers.add_parser('process_directory')
    process_directory_parser_group = process_directory_parser.add_argument_group(title="Process directory containing .evtx files")
    process_directory_parser_group.add_argument('--directory', '-d', help="Directory containing .evtx files", required=True)
    process_directory_parser_group.set_defaults(func=exec_pipeline)

    return parser, parser.parse_args()


"""
    Execute a conversion pipeline.

    :param args: program input arguments.
"""
def exec_pipeline(args: object):
    from pydoc import locate

    log.debug("Main:exec_pipeline:args:{}".format(args))

    source_class = locate("evtx_convert.Sources" + "." + args.source + "." + args.source)
    source = source_class()

    converter_class = locate("evtx_convert.Converters" + "." + args.converter + "." + args.converter)
    converter = converter_class()

    sink_class = locate("evtx_convert.Sinks" + "." + args.sink + "." + args.sink)

    # Get Windows Event Log event sources.
    for evtx_file_gen in source.ingest(args):
        # Get Windows Event Log events from each source.
        for evtx_file in evtx_file_gen:
            with sink_class(file_name=evtx_file, file_format="json") as sink:
                # Convert each Windows Event Log event to desired format.
                for converted_event in converter.convert(evtx_file):
                    sink.dump(converted_event)


if __name__ == "__main__":
    parser, args = argument_parser()

    try:
        # Set log level.
        stream_handler.setLevel(logging.getLevelName(args.loglevel))

        args.func(args)
    except Exception as error:
        log.error("Main:error:{}".format(error))

        parser.print_help()

    # import json
    # import pandas as pd

    # with open("..\..\data\samples\small.json") as json_file:
    #     data = json.load(json_file)
    #     print(data)
    #     # df = pd.DataFrame(data)
    #     # print(df.head())
