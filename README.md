# evtx-convert

A package for converting Windows Event Log .evtx files to different formats.

## Installation

```bash
    pip install -r requirements.txt
```

## Architecture

The package utilizes the following concepts for implementing an easily extensible architecture for processing Windows Event Log events:

- Source: a source of event log data. The source can be file or stream-based and it is up to the developer to implement an appropriate handler class. Included in the package is a FileSource class for reading .evtx files from a directory or on a single file basis. Developers should extent the *AbstractSource* class and override the *ingest(self, args: object)* method.
- Converter: a mechanism for converting log data to different formats. Included in the package is a JSON converter class (ToJSON). Developers should extent the *AbstractConverter* class and override the *convert(self, evtx: object)* method.
- Sink: the endpoint to which converted log data should be sinked. Included in the package is a FileSink class for saving entries to the file system. Developers should extent the *AbstractSink* class and override the *dump(self, args: object, event: object)* method.

## Usage example

Included withe the package is a *main.py* file which implements the *FileSource*, *ToJSON*, and *FileSink* interfaces for converting .evtx files to .json.

Processing a single .evtx file:

```bash
    python main.py --source FileSource --sink FileSink --converter ToJSON --loglevel 0 process_files --file <your_evtx_file>
```

Processing a directory of .evtx files:

```bash
    python main.py --source FileSource --sink FileSink --converter ToJSON --loglevel 0 process_directory --directory <your_evtx_files_directory>
```