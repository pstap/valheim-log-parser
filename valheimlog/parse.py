import re

from collections import namedtuple
from datetime import datetime
from typing import Optional, Tuple

char_pat = re.compile(r"^(.+): Got character ZDOID from (.+) : (\d+):(\d)$")


LogEntry = namedtuple("LogEntry", ["time", "char_name", "char_id", "is_alive"])

def parse(line: str) -> Optional[LogEntry]:
    match = char_pat.match(line.strip())
    if not match:
        return None

    # extract groups
    try:
        time = match.group(1)
        character_name = match.group(2)
        character_id_str = match.group(3)
        alive = match.group(4)
    except IndexError:
        return None

    # parse
    log_time: datetime = datetime.strptime(time, "%m/%d/%Y %H:%M:%S")
    character_id = int(character_id_str)
    is_alive: bool = alive != "0"

    return LogEntry(log_time, character_name, character_id, is_alive)
