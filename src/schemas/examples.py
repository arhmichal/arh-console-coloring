import re
import schemas.definitions.console_colors as cc

r_name = r"[\w.+-]+"
r_path_can_be_empty = "/{0,2}("+r_name+"/{1,2})*"
r_path = "/{0,2}("+r_name+"/{1,2})+"

compiler_flags = [
    { "pattern": re.compile(f"-(W)({r_name})"), 
      "replace": cc.format(r"-\1", cc.Color.White) + cc.format(r"\2", cc.Color.Red)},
    { "pattern": re.compile(f"-(f)({r_name})"), 
      "replace": cc.format(r"-\1", cc.Color.White) + cc.format(r"\2", cc.Color.Blue, cc.Format.Light)},
    { "pattern": re.compile(f"-(l)({r_name})(?=\\s|$)"),
      "replace": cc.format(r"-\1", cc.Color.White) + cc.format(r"\2", cc.Color.Cyan, cc.Format.Light)},
    { "pattern": re.compile(f"-(D)_({r_name})(?=\\s)"), 
      "replace": cc.format(r"-\1_", cc.Color.White) + cc.format(r"\2", cc.Color.Cyan)},
    { "pattern": re.compile(f"-(D)_({r_name})=({r_name})"), 
      "replace": cc.format(r"-\1_", cc.Color.White) + cc.format(r"\2", cc.Color.Cyan) + "=" + cc.format(r"\3", cc.Color.Cyan, cc.Format.Light)},
    { "pattern": re.compile(f"-()(std)=({r_name})"), 
      "replace": cc.format(r"-\1", cc.Color.White) + cc.format(r"\2", cc.Color.Cyan) + "=" + cc.format(r"\3", cc.Color.Cyan, cc.Format.Light)},
    
    { "pattern": re.compile(r"-(I)("+r_path+r_name+")"),
      "replace": cc.format(r"-\1", cc.Color.White) + cc.format(r"\2", cc.Format.Dark, cc.Color.Grey)},
    { "pattern": re.compile(r"-(L)("+r_path+r_name+")"), 
      "replace": cc.format(r"-\1", cc.Color.White) + cc.format(r"\2", cc.Format.Dark, cc.Color.Grey)},
]

files_patterns = [
    { "pattern": re.compile(r"(\b"+r_path_can_be_empty+r_name+r"\.(o|d|so)\b)"),
      "replace": cc.format(r"\1", cc.Format.Dark, cc.Color.Grey)},
    { "pattern": re.compile(r"(\b"+r_path_can_be_empty+r_name+r"\.(cpp|cc|c|hpp|hh|h)\b)"),
      "replace": cc.format(r"\1", cc.Color.Green)},
]

binaries_patterns = [
    { "pattern": re.compile(r"(^/[\w/\.]*/((protoc|cpp|gcc)\b|g\+\+))"),
      "replace": cc.format(r"\1", cc.Format.Light, cc.Color.Green)},
    { "pattern": re.compile(r"\b(make|mkdir|cp|mv|rm|chmod|sed|grep|cat|cd)\b"),
      "replace": cc.format(r"\1", cc.Format.Light, cc.Color.Yellow)},
]

scheme = []
scheme.extend(compiler_flags)
scheme.extend(files_patterns)
scheme.extend(binaries_patterns)
