#!/usr/bin/python3
"""
This module contains a script that reads from stdin and computes metrics
"""
import re
import sys
from typing import Optional, Tuple, Dict


PATTERN: str = (r"^(\d{0,3}\.){3}\d{0,3} "
                r"- \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "
                r"\"GET /projects/260 HTTP/1\.1\" "
                r"(\d{3}) (\d+)$")


def extract_status_and_size(line: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extracts the status code and size from a log line

    Args:
        line (str): The log line to parse

    Returns:
        Tuple[Optional[str], Optional[str]]: A tuple of the status code & size
    """
    match = re.search(PATTERN, line)

    if match:
        return (match.group(2), match.group(3))
    else:
        return None, None


def printMetrics(total_size: int, status_codes: Dict[str, int]) -> None:
    """
    Prints the metrics for the log lines read so far

    Args:
        total_size (int): The total size of all the log lines read so far
        status_codes (Dict[str, int]): A dict of status codes & their counts

    Returns:
        None
    """
    print("File size: {}".format(str(total_size)))
    for status_code in status_codes.keys():
        if status_codes[status_code] != 0:
            print("{}: {}".format(status_code, str(status_codes[status_code])))


status_codes: Dict[str, int] = {
                                "200": 0, "301": 0,
                                "400": 0, "401": 0,
                                "403": 0, "404": 0,
                                "405": 0, "500": 0}
total_size: int = 0
lines: int = 0

try:
    for line in sys.stdin:
        lines += 1

        status_code: Optional[str]
        size: Optional[str]
        status_code, size = extract_status_and_size(line.strip())
        if status_code and size:
            total_size += int(size)
            if status_code in status_codes:
                status_codes[status_code] += 1

        if lines >= 10:
            printMetrics(total_size, status_codes)
            lines = total_size = 0
            for code in status_codes.keys():
                status_codes[code] = 0
except KeyboardInterrupt:
    printMetrics(total_size, status_codes)
