# Ava-Tr Server Dosyaları
Oyuna gelecek olan güncellemeri buradan takip edebilirsiniz.   Oyununuzu güncell tutabilirsiniz.

# Kurulum ve başlatma
Uyarı: Windows üzerinde çalışma garanti edilmez ve onu desteklemeyeceğiz. ANCAK: sunucuyu herhangi bir sorun olmadan Windows'da başlatabilirsiniz ve bunun için kodu düzenlemeniz bile gerekmez.

# Gerekli Olanlar. 
- Ubuntu +18.04 Üstü
- Python3  
- Pip3
- Redis Server

```
Kurulum Talimatları 
- apt-get update
- apt-get upgrade
- apt install python3-pip
- apt-get install redis-server
- systemctl enable redis-server.service
- apt-install git
- git clone https://github.com/zenontrap/ava-tr
- Dosyalar'dan "web.ini" dosyasını kendi serverınıza göre güncelliyorsunuz.
- pip3 install --user -r requirements.txt " oyun gereksimilerini indiriyorsunuz."
- cd [klasör]  dosyaların bulunduğu klasöre girin.
- python3 web.py
- yeni bir terminal acıp dosyaların bulunduğu klasöre tekrardan giderek bu sefer'de
  python3 server.py yazıyoruz.
```
