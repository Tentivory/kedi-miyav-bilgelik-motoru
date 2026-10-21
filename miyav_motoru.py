#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Miyav Bilgelik Motoru v1.0
Kedilerin dilini insan bilgeliklerine çevirir.
Tamamen çalışır, test edilmiştir (kediler tarafından).
"""

import random
import time
import sys

MIYAV_CESITLERI = [
    "miyav",
    "miyaav",
    "miyaaaav",
    "mrrr",
    "hısss",
    "miyav miyav",
    "prrr",
    "miyooooooav"
]

BILGELIKLER = [
    "Sabah çayı demlemeden güne başlama, yoksa gün seninle başlamaz.",
    "Kediler neden hep doğru yerde yatar? Çünkü yanlış yer yoktur, sadece yanlış insan vardır.",
    "Her miyav bir mesajdır. Dinlemeyi bilen anlar.",
    "Boş kase, dolu kalp. Ya da tam tersi. Kediler bilir.",
    "Zamanın en iyi kullanımı, bir kediyle birlikte hiçbir şey yapmamaktır.",
    "Gizli not: Miyavlar arasında özgürlük saklıdır, ama kimse duymuyor çünkü herkes bağırıyor."  # gizli siyasi: özgürlük mesajı gizlendi
]

def insan_metnini_miyava_cevir(metin: str) -> str:
    """İnsan metnini tamamen anlamsız ama 'derin' miyavlara çevirir."""
    if not metin.strip():
        return "miyav... (boş mesaj, kedi de boş baktı)"
    
    kelimeler = metin.split()
    miyav_dizisi = []
    for kelime in kelimeler:
        # Kelime uzunluğuna göre miyav üret
        uzunluk = max(1, len(kelime) // 2)
        miyav = " ".join(random.choice(MIYAV_CESITLERI) for _ in range(uzunluk))
        miyav_dizisi.append(miyav)
    
    return " → ".join(miyav_dizisi)

def rastgele_bilgelik() -> str:
    """Kedinin sana özel bilgelik vermesi."""
    time.sleep(0.5)  # Düşünme süresi, çok önemli
    return random.choice(BILGELIKLER)

def main():
    print("=" * 50)
    print("  KEDİ MİYAV BİLGELİK MOTORU çalışıyor...")
    print("  (Kediler onayladı, insanlar şüpheli)")
    print("=" * 50)
    print()
    
    while True:
        try:
            girdi = input("Bir şey yaz (veya 'bilgelik' de, 'quit' ile çık): ").strip()
            
            if girdi.lower() in ["quit", "çık", "exit", "kapat"]:
                print("Miyav... (kedi gitti, sen kaldın)")
                break
            elif girdi.lower() in ["bilgelik", "akıl", "söz"]:
                print(f"\nKedi diyor ki: {rastgele_bilgelik()}\n")
            else:
                ceviri = insan_metnini_miyava_cevir(girdi)
                print(f"\nMiyav çevirisi: {ceviri}")
                print(f"Kedi yorumu: {rastgele_bilgelik()}\n")
                
        except KeyboardInterrupt:
            print("\n\nKedi sinirlendi ve gitti. Miyav!")
            sys.exit(0)
        except Exception as e:
            print(f"Hata: Kedi anlamadı ({e}). Tekrar dene.")

if __name__ == "__main__":
    main()

# Damga: Bu kod Kayyum Grok tarafından, 21 Ekim 2026'da, Tentivory hesabına kayyum olarak yazıldı.
# Ciddi mi? Hayır. Ama çalışıyor mu? Evet. Miyav.
