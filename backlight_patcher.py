"""
This patch prevents Windows from starting with
the keyboard backlight on and then disables it

DISCLAIMER: USE AT YOUR OWN RISK, I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS SOFTWARE.
"""

import os.path

offset = 0x7D499
# C6 87 10 02 00 00 01 48 8B
update = b'\xc6\x87\x10\x02\x00\x00\x00\x48\x8b'


def patch(path):
    print("writing bytes")
    print(update)
    with open(os.path.join(path, 'bootcamp.exe'), 'r+b') as f:
        f.seek(offset)
        f.write(update)
    print("patching successful")


if __name__ == '__main__':

    print("************************\n* author: nikiibarbaro *\n************************\n")
    print("e.g.: C:\Program Files\Boot Camp\n")
    path = input("Enter path to bootcamp.exe: ")
    patch(path)
