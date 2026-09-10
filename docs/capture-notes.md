# Live capture checklist

Plug the board into Linux and paste the output of:

```bash
lsusb | grep -i 27e0
lsusb -d 27e0:0101 -v
echo '--- input ---'
grep -A12 -i stinky /proc/bus/input/devices || grep -A12 -i 27e0 /proc/bus/input/devices
echo '--- hidraw ---'
ls -l /dev/hidraw*
cat /sys/class/hidraw/hidraw*/device/uevent
```

If an event node appears, run `evtest` and rock each direction once.

Open an issue or drop the text into this file.
