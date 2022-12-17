import random
import subprocess

def generate_random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(["%02x" % x for x in mac])


INTERFACE = input("Interface: ") # Değiştirilecek ağ arayüzünün adı

mac = generate_random_mac()
changed = subprocess.run(["ip", "link", "set", "dev", INTERFACE, "address", mac])

if changed:
    print("Worked! new Mac adress: "+mac)
else:
    print("Failed")
