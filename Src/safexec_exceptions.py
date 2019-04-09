"""
Used to define custom exceptions to be used by Safexecself.

Exceptions include:
FilePathError - Occurs when a file path provided does not lead to an existing
                file.
FileExtensionError - Occurs when a file provided does not contain the .ELF or
                    .ELFS extension.
FileNotSafeError - Occurs when a file provided has been modified and the hash
                    does not match the hash found in the .ELFS file.
UnsignedFileError - Occurs when a .ELFS file provided does not have a hash
                    attached to it.
"""

class Error(Exception):
    """Base class for other exceptions"""

class NotEnoughArgsError(Error):
    """Raise error for passing too few arguments."""
    def __init__(self):
        Error.__init__(self, "Not enough command line arguments given.")

class FilePathError(Error):
    """Raise error for bad file path."""
    def __init__(self):
        Error.__init__(self, "Filepath provided does not exist.")

class FileExtensionError(Error):
    """Raise error for bad file extension."""
    def __init__(self):
        Error.__init__(self, "File provided is not a .ELF or .ELFS file.")

class FileNotSafeError(Error):
    """Raise error for unsafe file detected."""
    def __init__(self):
        Error.__init__(self, "File provided is not safe to run.")

class FileNotSignedError(Error):
    """Raise error for unsigned .ELFS file."""
    def __init__(self):
        Error.__init__(self, ".ELFS file provided does not have a signature.")
