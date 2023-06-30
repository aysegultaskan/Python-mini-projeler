import datetime

def yasam_suresi(dogum_tarihi):
    su_an = datetime.datetime.now()
    yasam_suresi = su_an - dogum_tarihi
    yasam_saniye = yasam_suresi.total_seconds()
    return float(yasam_saniye)

# Kullanıcıdan doğum tarihini alınması
dogum_tarihi_str = input("Doğum tarihinizi (GG/AA/YYYY) formatında girin: ")
dogum_tarihi = datetime.datetime.strptime(dogum_tarihi_str, "%d/%m/%Y")

yasam_saniye = yasam_suresi(dogum_tarihi)
print(f"Şu ana kadar {yasam_saniye} saniye yaşadınız.")
