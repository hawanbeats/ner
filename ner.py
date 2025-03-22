import stanza # type: ignore

# Türkçe dil modeli yükleniyor (İlk çalıştırmada indirilecek)
stanza.download('tr')  
nlp = stanza.Pipeline('tr')

while True:
    user_input = input("Bir cümle gir (Çıkış için 'q' yazın): ")

    if user_input.lower() == "q":
        print("Sistem kapatılıyor...")
        break

    # Cümleyi işle
    doc = nlp(user_input)

    print("\nTespit Edilen Varlıklar:")
    for sentence in doc.sentences:
        for ent in sentence.ents:
            print(f"Metin: {ent.text} | Tür: {ent.type}")
    print("-" * 40)
