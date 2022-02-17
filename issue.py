import os
import logging
import fnmatch


class IssueFilter(object):
    """
    Filter logs by name. Allow Unix shell style wildcards.

    ```text
    +----------+----------------------------------+
    | Pattern  |              Meaning             |
    +----------+----------------------------------+
    | *        | matches everything               |
    | ?        | matches any single character     |
    | [seq]    | matches any character in seq     |
    | [!seq]   | matches any character not in seq |
    +----------+----------------------------------+
    ```
    """

    def filter(self, record: logging.LogRecord) -> int:
        return fnmatch.fnmatchcase(record.name, os.environ.get("ISSUE", "*"))

    __call__ = filter  # Filter also can be a callable object


if __name__ == "__main__":
    handler = logging.StreamHandler()
    handler.addFilter(IssueFilter())
    logging.basicConfig(level=logging.DEBUG, handlers=[handler])

    logging.getLogger("test1").debug("Debug1")
    logging.getLogger("test2").debug("Debug2")
