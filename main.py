from gpiozero import Button

NULL_CHAR = chr(0)

zButton = Button(2)
zCode = NULL_CHAR
xButton = Button(3)
xCode = NULL_CHAR


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
    
while True:
    if zButton.is_pressed:
        zCode = chr(29)
    else:
        zCode = NULL_CHAR

    if xButton.is_pressed:
        xCode = chr(27)
    else:
        xCode = NULL_CHAR

    write_report(NULL_CHAR*2+zCode+xCode+NULL_CHAR*4)
