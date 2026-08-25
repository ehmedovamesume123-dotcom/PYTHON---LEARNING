metn = " Mexanika mühəndisliyi "

print(metn.upper())                      # Bütün hərfləri böyük edir
print(metn.lower())                      # Bütün hərfləri kiçik edir
print(metn.strip())                      # Kənardakı boşluqları silir
print(metn.replace("Mexanika", "Sənaye"))  # Sözü əvəz edir
print(metn.strip().split(" "))           # Mətni siyahıya bölür
print(len(metn))                         # Mətnin uzunluğu
print(metn.strip().startswith("Mexanika")) # "Mexanika" ilə başlayırmı?
print(metn.strip().endswith("mühəndisliyi")) # "mühəndisliyi" ilə bitirmi?
