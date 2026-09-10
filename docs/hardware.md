# Hardware

Stelulu Technologies **Stinky Gaming Footboard**, models seen as SGFB-101201 / SBFB-101201 (2013–2014).

## Physical

- Four Cherry MX Blue switches: toe, heel, left, right
- Rocking plate; usable 1-foot or 2-foot, landscape or portrait
- Swappable torsion springs (TBOX): blue soft / green medium / red hard
- Mini-USB on the underside, detachable cable, strain-relief channel
- Red status LED when enumerated
- Steel inner frame, T6 aluminum top plate
- No special kernel driver: standard USB HID

## USB

| Field | Value |
|---|---|
| VID | `27e0` |
| PID | `0101` |
| Vendor string | Stelulu |
| Product string | Stinky Board |
| Class | HID |

Firmware 1.2 contains a composite HID device:

1. Interface 0 — keyboard-style HID (the programmed keystrokes live here)
2. Interface 1 — second HID interface, almost certainly the configuration / vendor channel

Onboard memory stores the active mapping. The Windows app also kept named profiles on disk and, if left running, auto-switched profiles by watching process names (max 9 programs). That auto-switch is host software, not firmware.

## Button actions (official software)

| Mode | Behavior |
|---|---|
| Normal | Keyboard-like press/hold/release |
| Key Down | Single down+release even if held |
| Pulse | Repeat 1–30 clicks per second while held |
| Unbound | No output |

Modifiers: Shift, Ctrl, Alt, Windows; left/right distinguished. Simultaneous keys / diagonals supported.

## Firmware

`firmware/Stinky_Firm_1.2.hex` is Intel HEX for an AVR-class USB MCU (vector table + USB descriptors in-image). Used span is about 8.4 KiB. VID/PID and the "Stelulu" / "Stinky Board" UTF-16 strings are in the image.

Flashing was done through the Windows configurator Settings tab. Do not brick a unique board by guessing a programmer until the update protocol is captured.

## Linux today

Generic `usbhid` already binds `03:00:00`. If a profile was previously saved on the board, keystrokes should appear as a normal keyboard on Linux with no extra software.

If the board was never programmed, or you need to change binds, you need either:

- the Windows configurator (VM), or
- this project's tools once the vendor reports are decoded, or
- a userspace `uinput` mapper reading raw HID reports
