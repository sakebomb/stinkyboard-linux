#!/usr/bin/env python3
"""Enumerate and dump HID reports for the Stelulu Stinky Footboard (27e0:0101).

Requires: python3, plus either hidapi (`pip install hidapi`) or raw /dev/hidraw.

This does not yet write mappings. Dump first; decode later.
"""

from __future__ import annotations

import argparse
import glob
import os
import sys

VID = 0x27E0
PID = 0x0101


def cmd_list(_: argparse.Namespace) -> int:
    print(f"Looking for VID={VID:04x} PID={PID:04x}")
    found = False

    try:
        import hid  # type: ignore

        for d in hid.enumerate(VID, PID):
            found = True
            print("--- hidapi ---")
            for k in (
                "path",
                "vendor_id",
                "product_id",
                "manufacturer_string",
                "product_string",
                "serial_number",
                "interface_number",
                "usage_page",
                "usage",
            ):
                print(f"  {k}: {d.get(k)}")
    except ImportError:
        print("hidapi not installed (pip install hidapi) — falling back to sysfs/hidraw")

    for uevent in glob.glob("/sys/bus/hid/devices/*/uevent"):
        text = open(uevent, encoding="utf-8", errors="replace").read()
        if "27E0:0101" in text.upper() or "27e0:0101" in text:
            found = True
            print(f"--- {uevent} ---")
            print(text.rstrip())

    raws = sorted(glob.glob("/dev/hidraw*"))
    if raws:
        print("hidraw nodes:", " ".join(raws))

    if not found:
        print("Board not found. Check lsusb and udev rules.", file=sys.stderr)
        return 1
    return 0


def cmd_dump(args: argparse.Namespace) -> int:
    path = args.device
    if not path:
        raws = sorted(glob.glob("/dev/hidraw*"))
        if not raws:
            print("No /dev/hidraw* nodes.", file=sys.stderr)
            return 1
        path = raws[0]
        print(f"Using {path} (pass --device to pick another)")

    fd = os.open(path, os.O_RDWR)
    try:
        print(f"Reading interrupt reports from {path}. Press foot switches. Ctrl-C to stop.")
        while True:
            data = os.read(fd, 64)
            print(data.hex(" "))
    except KeyboardInterrupt:
        print()
        return 0
    finally:
        os.close(fd)


def main() -> int:
    p = argparse.ArgumentParser(description="Stinky Footboard HID helper")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="find the board")
    d = sub.add_parser("dump", help="hexdump interrupt reports")
    d.add_argument("--device", help="/dev/hidrawN")
    args = p.parse_args()
    if args.cmd == "list":
        return cmd_list(args)
    if args.cmd == "dump":
        return cmd_dump(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
