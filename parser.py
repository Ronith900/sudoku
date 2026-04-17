from dataclasses import dataclass
from typing import Optional
import re


@dataclass
class ParsedCommand:
    action: str
    cell: Optional[str] = None
    value: Optional[str] = None
    raw: str = ""



def parse_command(user_input: str) -> ParsedCommand:
    clean_input = " ".join(user_input.strip().upper().split())

    if clean_input == "HINT":
        return ParsedCommand(action="hint", raw=clean_input)

    if clean_input == "CHECK":
        return ParsedCommand(action="check", raw=clean_input)

    if clean_input == "QUIT":
        return ParsedCommand(action="quit", raw=clean_input)
    
    if re.match(r"^[A-I][1-9]\sCLEAR$", clean_input):
        cell, value = clean_input.split(" ")
        return ParsedCommand(action="clear", cell=cell, value=value, raw=clean_input)

    if re.match(r"^[A-I][1-9]\s[1-9]$", clean_input):
        cell, value = clean_input.split(" ")
        return ParsedCommand(action="move", cell=cell, value=value, raw=clean_input)

    return ParsedCommand(action="invalid", raw=clean_input)