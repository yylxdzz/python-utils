# python-utils

A small collection of practical Python utility functions.

## Features

- `file_utils` — safe file read/write, atomic writes, directory helpers
- `string_utils` — slugify, truncate, camel/snake case conversion
- `time_utils` — date range helpers, ISO formatting, humanized durations

## Install

```bash
pip install -e .
```

## Usage

```python
from python_utils.file_utils import atomic_write
from python_utils.string_utils import slugify

atomic_write("/tmp/out.txt", "hello")
print(slugify("Hello World!"))  # hello-world
```

## Test

```bash
python -m pytest
```

## License

MIT
