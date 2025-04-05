# [ZDI-CAN-25373: Windows Shortcut Exploit Abused as Zero-Day in Widespread APT Campaigns](https://www.trendmicro.com/en_us/research/25/c/windows-shortcut-zero-day-exploit.html)

Trend Zero Day Initiative™ (ZDI) uncovered both state-sponsored and cybercriminal groups extensively exploiting ZDI-CAN-25373 (aka ZDI-25-148), a Windows .lnk file vulnerability that enables hidden command execution.

## PoC
Run `poc.py` to hide the target of `legit.lnk` and write it to disk as `hidden.lnk`


legit.lnk

![image](https://github.com/user-attachments/assets/b03d83d5-a465-4daa-9d0f-5cb001a711fc)


hidden.lnk

![image](https://github.com/user-attachments/assets/03b7518e-2353-40b9-8ca3-51285ad2faac)
