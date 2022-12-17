<h1>If you want to enter the mac address manually:</h1>
For using:<br>
sudo python app.py -i INTERFACE -m NEW_MAC_ADDRESS<br>
Example:<br>
sudo python app.py -i eth0 -m 00:11:22:33:44:55<br>
And your Mac Adress chang. New Mac Adress: "00:11:22:33:44:55"<br>
<h1>If you want the random mac address to be generated and changed:</h1>
For using:<br>
sudo python random_1.py<br>
output: "Write Interface:"<br>
Example:<br>
```shell
marijua@Marijua:~/Masaüstü/important/software/macAdressChanger$ sudo python3 random_1.py 
Interface: enp2s0
Worked! new Mac adress: 00:16:3e:3b:ff:27
marijua@Marijua:~/Masaüstü/important/software/macAdressChanger$ 
```
