# Protocol notes

Status: **unconfirmed**. Needs a live board and/or a USBPcap capture of `Stinky_Config_*.exe`.

## What we know from artifacts

- Device is composite HID, not a vendor-class bulk device.
- "Save Config" writes the active map into onboard memory.
- Firmware updates consume an Intel HEX file selected in the Windows UI.
- Auto-profile switching required the Windows process to stay running.

## Capture plan

On a Windows VM with the board passed through:

1. Install Wireshark + USBPcap.
2. Capture while: enumerating, reading current config, changing one button, Save Config, Pulse vs Normal, firmware browse (do not flash yet).
3. Filter `usb.idVendor == 0x27e0`.
4. Drop the pcap into `captures/` (gitignored if large) and note SET_REPORT / GET_REPORT lengths here.

On Linux, with the board plugged in:

```bash
lsusb -d 27e0:0101 -v
sudo hidrd-convert -o spec /sys/bus/hid/devices/*27E0:0101*/*/report_descriptor
python3 tools/stinkyctl.py list
python3 tools/stinkyctl.py dump
```

Then press toe / heel / left / right and record which interface produces traffic.

## Hypotheses to test

1. Interface 1 feature reports hold the 4-button map (usage, modifiers, mode, pulse rate).
2. Keyboard interface only emits the *programmed* keys; raw switch state may only exist on interface 1.
3. If (2) is true, a uinput mapper can ignore onboard memory entirely.

Update this file as soon as a capture exists. Do not invent report layouts.
