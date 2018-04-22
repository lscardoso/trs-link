# trs-link

Python script to transfer files to and from the TRS-80 Model 100 vintage computer

This script handles RS232 transnsfers to/from a TRS-80 Model 100 computer and a modern computer. It works in text and basic modes, handling character translations such as "line feed" to "new line" and EOF.

## Dependencies

* Python 3
* pyserial

## Usage

```
python3 trs-link --help 
```

for a list of options

On your TRS-80 M100, do all transfers with TELCOM, without any width (just type Enter when asked for a width)

Beware that:

* the device defaults to a MAC OS usr-to-serial interface à la: /dev/cu.usbserial. Change this to reflect your serial port
* default baudrate is set to 1200. At the TRS-80 side this corresponds to the configuration string "58N1D". There might be some issues transfering large files with this configuration as the TRS-80 is kinda slow. Think about reducing the speed at both sides before transmissiomn

## Next features

* fix the command line interface to something more friendly
* translate from the TRS-80 ascii character set to modern encondings
* write a TRS-80 side code to further automate the transmission of files by sending file names and other info

