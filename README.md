# Wi-Fi Network Security Tester (PyWiFi Brute Force)

Ushbu skript `pywifi` kutubxonasidan foydalangan holda, simsiz tarmoqlarning (Wi-Fi) parollar mustahkamligini va lug‘at (dictionary-based) hujumlariga qarshi chidamliligini tekshirish uchun yozilgan o‘quv-tadqiqot vositasidir.

## ⚠️ Muhim ogohlantirish (Disclaimer)

> **DIQQAT:** Ushbu loyiha faqat ta'lim, laboratoriya sinovlari va axborot xavfsizligini o‘rganish maqsadida yaratilgan. Kodni sizga tegishli bo‘lmagan yoki ruxsatingiz yo‘q begona simsiz tarmoqlarda sinab ko‘rish **noqonuniy** hisoblanadi. Foydalanuvchining harakatlari uchun muallif javobgarlikni o‘z zimmasiga olmaydi.

---

## 🚀 Imkoniyatlari

* **Lug‘at asosida tekshirish:** Tayyor `passwords.txt` fayli orqali parollar ro‘yxatini avtomatik sinovdan o‘tkazish.
* **Brute-Force Generator:** Agar parol fayli topilmasa, `itertools` yordamida avtomatik ravishda 8 xonali raqamli kombinatsiyalarni (`00000000` - `99999999`) yaratib tekshirish.
* **Avtomatik profil boshqaruvi:** Tarmoq interfeysini har bir urinishda tozalash va WPA2-PSK xavfsizlik protokoli bo‘yicha ulanishni sinash.

## 🛠️ Talablar va O‘rnatish

Skript ishlashi uchun tizimda Python o‘rnatilgan bo‘lishi va Wi-Fi adapter mavjud bo‘lishi kerak.

Obuna bo'ling sizlarga yanada yaxshi code larni berishda davom etaman 😎
