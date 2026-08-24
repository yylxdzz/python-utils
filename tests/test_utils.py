"""Basic tests for python-utils."""

from python_utils.file_utils import atomic_write, read_text
from python_utils.string_utils import slugify, to_camel_case, to_snake_case, truncate
from python_utils.time_utils import humanize_duration


def test_slugify():
    assert slugify("Hello World!") == "hello-world"


def test_case_conversion():
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_camel_case("hello_world") == "HelloWorld"
    assert to_camel_case("hello_world", upper=False) == "helloWorld"


def test_truncate():
    assert truncate("a" * 100, 10) == "aaaaaaa..."
    assert truncate("short", 10) == "short"


def test_atomic_write(tmp_path):
    f = tmp_path / "out.txt"
    atomic_write(f, "hello")
    assert read_text(f) == "hello"


def test_humanize_duration():
    assert humanize_duration(45) == "45s"
    assert humanize_duration(125) == "2m 5s"
