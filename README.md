# stinkyboard-linux

Open-source Linux support and reverse-engineering for the abandoned **Stelulu Stinky Gaming Footboard** (USB `27e0:0101`).

Stelulu shut down. The official Windows configurator is an Inno Setup `.exe` from 2013–2014. This repo preserves the firmware, documents the hardware, and is the starting point for a Linux tool that can talk to the board.

## Current status

| Piece | State |
|---|---|
| USB identity | Known (`27e0:0101`, HID, "Stelulu" / "Stinky Board") |
| Official firmware 1.2 | Preserved in `firmware/` |
| Kernel driver | Not needed — generic `usbhid` already binds |
| udev rule | `udev/99-stinkyboard.rules` |
| Config protocol | Not decoded yet — needs a live capture |
| Linux configurator | Scaffold only (`tools/stinkyctl.py`) |

If a profile is already stored on the board, Linux may already emit those keystrokes with no extra software. The missing piece is *reprogramming* the board without Windows.

## Two tracks

1. **Programmer** — decode HID feature reports the Windows app wrote, then `stinkyctl` writes the same map.
2. **Userspace mapper** — read raw button reports and inject keys via `uinput`. Usable even if onboard programming stays opaque.

## Quick start (Linux)

```bash
sudo cp udev/99-stinkyboard.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
# unplug / replug the board

python3 tools/stinkyctl.py list
```

Then run the commands in `docs/capture-notes.md` and send the output. That single dump decides whether we implement a programmer, a mapper, or both.

## Repo layout

```
docs/           hardware, protocol, sources, capture checklist
firmware/       official Stinky_Firm_1.2.hex
udev/           99-stinkyboard.rules
tools/          stinkyctl.py (enumerate / dump HID)
```

Vendor binaries (the 10 MB configurator installers) are **not** committed. Checksums and Archive.org URLs are in `docs/sources.md`.

## Legal

New code and docs: MIT (`LICENSE`).

`firmware/Stinky_Firm_1.2.hex` and any original Stelulu material are preserved for interoperability with abandoned hardware. Stelulu / Stinkyboard names are used only to identify the device.

## Hardware in one line

Four Cherry MX Blue foot switches on a rocking plate. Mappings saved to onboard memory. Pulse / Key Down / Normal / Unbound. Modifiers up to 16 binds. Auto-profile switching lived in the Windows process, not the firmware.
