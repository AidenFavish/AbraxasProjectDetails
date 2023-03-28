# Abraxas Aquaphonics Project
We are designing a system running off a raspberry pi that would notify Mr. Lutticken when a leak is detected.
## Members:
- **Lead:** Aiden Favish
- **Programers:** Joseph Ensberg and Nick DeWall
- **Electric Engineer:** Will Guo
- **Designer:** Zander Brooks

# How it works:
The aquaphonics notification system works by sensing a change in voltage through its external voltmeter. 
A constantly running program will keep checking voltage and if it drastically changes it will execute the notification script. 
The notification script will send an email (or text) to the recipients located in the `hidden.py` file under directory `/Desktop/AbraxasProject/AbraxasNotificationSystem/hidden.py`. If you want to add recipients add their address to the array in `hidden.py` under the variable `reciever2`.
The program runs through an SMTP server called SendInBlue if the key expires it can be updated in the `hidden.py` file. 
