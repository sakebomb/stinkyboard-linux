# Official firmware

`Stinky_Firm_1.2.hex` is not stored as a giant blob in the first commit if you clone before fetching it. Get the verified copy:

```bash
curl -L -o Stinky_Firm_1.2.hex \
  https://archive.org/download/Stinkyboard/Stinky_Firm_1.2.hex
sha256sum Stinky_Firm_1.2.hex
# c589734b7a312301321a6782506c6cf8d93eb9ea95d90d071c9491e96fe1cb26
```

Also mirrored at:
https://archive.org/download/Stinky-Gaming-Footboard-Drivers/Firmware/Stinky_Firm_1.2.hex

AVR Intel HEX. Used span ~0x0000–0x20EF (8432 bytes). Contains USB VID/PID 27e0:0101 and strings "Stelulu" / "Stinky Board".
