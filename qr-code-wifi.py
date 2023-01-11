import wifi_qrcode_generator as qr

SSID = str(input("Entrez le nom de votre réseau WI-FI : "))
PASS = str(input("Entrez le mot de passe de votre réseau WI-FI : "))

qrCode = qr.wifi_qrcode(SSID, False, 'WPA', PASS)

qrCode.show()

qrCode.save("qrcode-wifi.png")