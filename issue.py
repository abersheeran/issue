import os
import logging
import fnmatch


class IssueFilter(logging.Filter):
    """
    Filter logs by name. Allow Unix shell style wildcards.

    +----------+----------------------------------+
    | Pattern  |              Meaning             |
    +----------+----------------------------------+
    | *        | matches everything               |
    | ?        | matches any single character     |
    | [seq]    | matches any character in seq     |
    | [!seq]   | matches any character not in seq |
    +----------+----------------------------------+
    """

    def __init__(self) -> None:
        super().__init__("")

    def filter(self, record: logging.LogRecord):
        return fnmatch.fnmatchcase(record.name, os.environ.get("ISSUE", "*"))


if __name__ == "__main__":
    handler = logging.StreamHandler()
    handler.addFilter(IssueFilter())
    logging.basicConfig(level=logging.DEBUG, handlers=[handler])

    logging.getLogger("test1").debug("Debug1")
    logging.getLogger("test2").debug("Debug2")
