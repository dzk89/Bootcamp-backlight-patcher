# Bootcamp-backlight-patcher
This patch prevents Windows from starting with the keyboard backlight on and then disables it.

__Tested on Bootcamp.exe 6.1.8086.2__

## DISCLAIMER: USE AT YOUR OWN RISK. I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS SOFTWARE.

## How to use
Either use the .py or the .exe to patch the bootcamp.exe

For the __.py__:

0. Backup bootcamp.exe in case it doesn't work, because then you need to replace the modified file with the backed up file using a live system.
1. Start cmd and enter backlight_patcher.py (Python is required)
2. Provide the absolute path to the bootcamp.exe
3. If success message displays everything should work as expected
4. Reboot


For the __.exe__:

0. Backup bootcamp.exe in case it doesn't work, because then you need to replace the modified file with the backed up file using a live system
1. Start backlight_patcher.exe
2. Provide the absolute path to the bootcamp.exe
3. If success message displays, everything should work as expected
4. Reboot
