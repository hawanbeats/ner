# Named Entity Recognition (NER) with Stanza
Bu repository, Stanza kütüphanesini kullanarak metinlerdeki özel adları (isimler, yerler, organizasyonlar vb.) tespit etmek için bir Python örneğidir. Verilen cümlelerdeki adları ve diğer varlıkları tanımlar ve bunları ekrana yazdırır.

## Proje Özeti
Bu Python kodu, **Stanza** kütüphanesinin Türkçe dil modeliyle metinleri işler ve metinde yer alan **named entity** (özel ad) türlerini tespit eder. Kullanıcıdan alınan metin üzerinde kişi isimleri, yer isimleri, organizasyonlar gibi varlıklar tanımlanır.

## Çalıştırma Adımları
1. Python ve Gerekli Kütüphaneleri Yükleme
- Python'un yüklü olduğundan emin olun. Python 3.x sürümü önerilir.
- Stanza kütüphanesini yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:
``
pip install stanza
``
2. Stanza Türkçe Dil Modeli İndirme
- İlk defa kullanıyorsanız, Türkçe dil modeli verisini indirmeniz gerekebilir. Aşağıdaki komutla Türkçe dil modeli indirilebilir:
```python
import stanza
stanza.download('tr')
```
3. Kodun Çalıştırılması
- Kullanıcıdan alınan cümlelerdeki varlıklar tanımlanır ve her bir varlık ile türü ekrana yazdırılır.
- ``user_input`` değişkenine girilen cümledeki özel adlar tespit edilir.

## Kod Açıklaması
```python
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
```
- ``stanza.Pipeline('tr')``: Türkçe dil modelini başlatır ve metni analiz eder.
- ``sentence.ents``: Cümledeki tespit edilen varlıkları listeler. Varlıklar, kişi ismi, yer ismi, organizasyonlar gibi türlere ayrılabilir.
- ``ent.text`` ve ``ent.type``: Her bir tespit edilen varlığın metni ve türü ekrana yazdırılır.

## Örnek Çıktı
- Girdi:
```
Bir cümle gir (Çıkış için 'q' yazın): İstanbul, Türkiye'nin en büyük şehridir.
```
- Çıktı:
```
Tespit Edilen Varlıklar:
Metin: İstanbul | Tür: GPE
Metin: Türkiye | Tür: GPE
----------------------------------------
```
- Girdi:
```
Bir cümle gir (Çıkış için 'q' yazın): Ahmet Bey, Boğaziçi Üniversitesi'nde çalışıyor.
```
- Çıktı:
```
Tespit Edilen Varlıklar:
Metin: Ahmet Bey | Tür: PER
Metin: Boğaziçi Üniversitesi | Tür: ORG
----------------------------------------
```
## Katkıda Bulunma
Katkıda bulunmak isterseniz, önerilerinizi veya hataları GitHub issues bölümünde paylaşabilir veya pull request gönderebilirsiniz.
