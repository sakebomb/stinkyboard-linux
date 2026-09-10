# Sources

Official Stelulu site (stinkyboard.com) is dead. These are the preservation copies used by this project.

## Internet Archive

| Item | URL |
|---|---|
| Software, firmware, manual | https://archive.org/details/Stinkyboard |
| Config 1.2 / 1.4 / 1.5 beta + firmware | https://archive.org/details/Stinky-Gaming-Footboard-Drivers |

Direct files from `Stinkyboard`:

| File | SHA-256 | Notes |
|---|---|
| `Stinky_Firm_1.2.hex` | `c589734b7a312301321a6782506c6cf8d93eb9ea95d90d071c9491e96fe1cb26` | AVR Intel HEX, copied into `firmware/` |
| `Stinky_Config_1.2.exe` | `13a6587e2e44822cbbd264f20418ef4f192f36af8ed179a299ab5fd722925b10` | Inno Setup installer, ~9.8 MiB. Not committed. |
| `Stinky_Manual_1.0.pdf` | (download from IA) | User manual |
| `Stinky_Config_1.4.exe` | (see Drivers item) | Later configurator |
| `Stinky_Config_1.5_Beta.exe` | (see Drivers item) | Beta configurator |

Download firmware:

```bash
curl -L -o firmware/Stinky_Firm_1.2.hex \
  https://archive.org/download/Stinkyboard/Stinky_Firm_1.2.hex
```

## USB identity

- Vendor ID: `0x27e0` (Stelulu)
- Product ID: `0x0101` (Stinky Board)
- Class: HID `03:00:00`
- Linux hardware probe: https://linux-hardware.ru/?id=usb:27e0-0101

## Period reviews (2013–2014)

Useful for behavior that is not in the firmware image: Pulse rate, auto-profile (host-side), spring kits, TBOX adjustment.
