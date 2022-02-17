# issue

Filter logs by name. Allow Unix shell style wildcards.

Inspired by https://github.com/debug-js/debug

## Install

```sh
pip install issue
```

## Usage

```python
from issue import IssueFilter

handler = logging.StreamHandler()
handler.addFilter(IssueFilter())  # Add IssueFilter to the handler
logging.basicConfig(level=logging.DEBUG, handlers=[handler])

logging.getLogger("test1").debug("Debug1")
logging.getLogger("test2").debug("Debug2")
```

Then, you can change environment value `ISSUE` to filter the logs by name. Like: `ISSUE=test1 python yourfile.py`
