import re
import schemas.definitions.console_colors as cc

scheme = [
    { "pattern": re.compile(r"\n\b\ta([sS])da\d"), "replace": r"qwe \1 asd", "final": True },
    { "pattern": re.compile(r"(\s)|(-)"), "replace": r", "},
    { "pattern": re.compile(r"(Ema|Max)"), "replace": cc.format(r"\1", cc.Color.Red)},
    { "pattern": re.compile(r"(Max)"), "replace": cc.format(r"\1", cc.Color.Blue), "final": True},
]
