#Buat biodata dictionary

biodata = {
    "Nama\t"          : "Meiana Sahabuddin",
    "Tanggal Lahir\t": "05-Mei-2005",
    "Alamat\t"        : "Jl.H.A.M Arsyad Soreang",
    "Hobi\t"          : ["Olahraga","Dengar Musik"],
    "Status\t"        : "Pelajar"
}

# Menampilkan biodata
print("Biodata: ")
for key, value in biodata.items():
    print(f"{key}: {value}")