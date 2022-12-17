import random
import subprocess

def generate_random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(["%02x" % x for x in mac])

INTERFACE = "enp2s0"  # Değiştirilecek ağ arayüzünün adı

mac = generate_random_mac()
subprocess.run(["ip", "link", "set", "dev", INTERFACE, "address", mac])
