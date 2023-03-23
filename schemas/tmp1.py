import re
import schemas.definitions.console_colors as colors

scheme = [
    { "pattern": re.compile(r"\n\b\ta([sS])da\d"), "replace": r"qwe \1 asd", "final": True },
    { "pattern": re.compile(r"(\s)|(-)"), "replace": r", ", "final": False },
]
