---
name: turkce-usta
description: "/turkce-usta yazıldığında: doğal, TDK uyumlu Türkçe yazar veya düzeltir; imla, hukuk/resmî metin, bağlaç-ek çeşitliliği, AI temizliği."
disable-model-invocation: true
license: MIT
metadata:
  version: "2.2.0"
  compatibility: "claude-code, claude-ai, codex, chatgpt, gemini-cli, antigravity"
---

# Türkçe Usta: Doğal, Zengin ve TDK Uyumlu Türkçe Kılavuzu

Bu kılavuz, İngilizce ağırlıklı eğitim görmüş modellerin ürettiği **"çeviri iskeletli, tekdüze, ek/bağlaç fakiri veya şablonlu"** Türkçeyi; Türkçenin gerçek sözdizimine, zengin ek-çatı-bağlaç sistemine, duygusal inceliklerine ve güncel TDK Yazım Kılavuzu'na taşıyan bütüncül bir üretim ve redaksiyon sistemidir.

> **Önemli Ayrım — Kurallar vs Yaratıcı Özgürlük:** `TDK imlası`, `dil bilgisi anlatım bozuklukları`, `mevzuat tutarlılığı`, `olgu kilidi` ve `AI çeviri çöpü yasağı` **kesindir**. Buna karşılık bağlaç oranları, cümle açılış paleti, deyim/ikileme sıklığı, ritim çeşitliliği ve söz sanatları **yazarın yaratıcı enstrümanlarıdır**; katı sayısal kota değildir. Üretirken sayı sayma; anlam, duygu ve kulak hangisini gerektiriyorsa özgürce seç.

## Çekirdek Anayasa (Skill Açıkken Geçerli)

Bu skill yalnız `/turkce-usta` çağrılınca veya kullanıcı açıkça Türkçe yazım/düzeltme desteği isteyince devreye girer. Açıkken aşağıdaki 10 ilke her Türkçe yanıt, metin üretimi ve düzenlemede uygulanır:

1. **Önce Türkçe Düşün (Sola Dallanan ve Baş-Sonda İskelet):** İngilizce SVO iskeletini (`Bir sistem kurduk, bu sistem...` / `Görüyoruz ki...`) kurma. Niteleyiciyi sıfat-fiille (`-(y)An`, `-DIk`, `-(y)AcAk`) ismin önüne al; vurgulanan bilgiyi yüklemin hemen önündeki **odak yuvasına** koy. Belirtili/belirtisiz tamlama ayrımını (`devlet okulu` vs `devletin okulu`) ve `-lArI` iyelik açıklığını koru.
2. **Bağlaç, Açılış ve Söz Varlığı Özgürlüğü:** `ancak, ayrıca, bununla birlikte, öte yandan, dolayısıyla` refleksine ve soluk `sağlamak, gerçekleştirmek, süreç, kapsamlı` tekrarına düşme. Ardışık eylemleri **ulaçlarla** (`-(y)Ip, -(y)IncA, -ArAk, -DIkçA`) bağla; gerektiğinde bağlaçsız geç ya da amacı **`diye`** ile kur (*"Yetişemem diye korktum"*). Zıtlık, gerekçe ve derecelendirmede nüansa göre seç (*ama, fakat, lakin, oysa, hâlbuki, ne var ki, gelgelelim, gerçi, nitekim, zira, meğer, madem, kaldı ki, üstelik, şöyle dursun*); cümle sonunu da kullan (*... korktum çünkü*). Açılış paletini (özne, belirteç, ulaç, sıfat-fiil, devrik/yüklem, parçacık) mekanik sıraya sokmadan, düşüncenin ritmine göre çeşitlendir; eşanlamlılar arasından tam nüansı seç (*bakmak / süzmek / irdelemek / eşelemek*).
3. **Ek, Çatı, Görünüş ve Aktarma Zenginliği:** `-mAktAdIr` ve gereksiz `-DIr` yığınıyla metni dondurma (yalnız akademik/resmî metin ile tanımda ölçülü koru). Duyumda kanıtsal `-mIş`, hızlı/ansızın eylemde `-(y)Iver`, sürerlikte `-(y)Akal / -Agel`, karşılıklı/birlikte eylemde **işteş çatı `-(I)ş`** (*bakıştılar, gülüştüler*), görünüşte **`-(y)AcAk ol-`**, **`-DI mI`**, **`-mAz mı!`**, **`-(y)AsI gel-`**, anlatıda üç katmanlı geçmiş (`-mıştı / -iyordu / -di`), konuşmada duygu ekleri (`-CA, -CIk, -CAğIz`) ve **`m-p-r-s` pekiştirme sıfatları** (*bembeyaz, kupkuru, sapasağlam*) kullan. Dolaylı aktarımda soru ve zamanı bük (*"Gelecek misin?" -> Gelip gelmeyeceğini sordu*).
4. **Duyguyu, Sesi ve Söz Sanatlarını Klişesiz Kur:** *"İçini bir hüzün kapladı"*, *"Yalnız değilsiniz"*, *"Harika bir soru!"* gibi yapay şablonlara düşme. Duyguyu kip, bedensel/somut ayrıntı, cümle ritmi, ikileme, süssüz mecaz (*ad aktarması, somutlama, ince kinaye*), ünlem veya soru/devrik seçimiyle bağlamın siciline uygun kur.
5. **Zamir, "Bir", "Kendi" ve Kof Fiil Budaması:** Kişi eki özneyi taşıyorsa `ben, biz, o, siz` zamirlerini yalnız karşıtlık veya vurgu gerekiyorsa yaz. Soyut tamlamalardaki gereksiz `bir`i (`büyük bir önem` -> `büyük önem`) ve İngilizce `own` çevirisi `kendi`yi at. `gerçekleştirmek, sağlamak, rol oynamak, sahip olmak, ev sahipliği yapmak` yerine doğrudan Türkçe eylem kur.
6. **Olgusal Sadakat Kilidi:** Mevcut bir metni onarırken veya özetlerken kaynakta olmayan hiçbir sayı, tarih, kişi, kurum, neden-sonuç bağı veya kesinlik derecesi uydurma. Klişe silinince somut veri gerekiyorsa kaynakta yoksa `[somut veri: ...]` yer tutucusu bırak ya da sadeleştir.
7. **TDK İmla, Noktalama, Akademik/Medya ve Hukuk İkilikleri:**
   - Ara sözlerde uzun tire (`—`) ve aralıklarda orta çizgi (`–`) kullanma (`—` yalnız tiyatro/diyalog satır başında konuşma çizgisidir); aralıklar kısa çizgi (`2024-2026`), eksilti/alıntı `...` ve `[...]`, saatler noktalı (`14.30`, `13.00'te`), sayılarda binlik nokta ve kesir virgül (`1.250,75 TL`, `%42,5`), yüzde bitişik (`%25`). İki noktadan sonra tam cümleyse büyük, örnek sıralamasıysa küçük; Türkçe başlıklarda `ve, ile, ya da, ki` bağlaçları **küçük** (*Suç ve Ceza*), haber/blogda **cümle düzeni** kullan.
   - `ve, veya, yahut`, tekrarlı bağlaçlar ve tek zarf-fiilden (`-Ip, -ArAk`) sonra virgül konmaz. Kurum adları kesmesiz (*Türk Dil Kurumuna*; istisna *Avrupa Birliği'ne*), kanunlar genel yazıda kesmeli (*Medeni Kanun'a*); kısaltma ve yabancı terim ekleri **Türkçe okunuşa** göre gelir (`TDK'ye, TBMM'nin, cache'i, queue'yu, URL'yi, CPU'yu, API'yi, GitHub'da, Google'da, Node.js'te, WhatsApp'tan gönder, X'te`).
   - Düzeltme işareti (`^`) anlam ayrımı (*hâlâ/hala, hâkim/hakim, kâr/kar, âdet/adet, dâhil/dahil, hâlihazırda*), `g/k/l` inceliği (*kâğıt, hikâye*) ve nispet `î`'sinde (*resmî, millî*) korunur; **lazım** ve **layık** şapkasızdır. `2.0 sürümü` (`Sürüm 2.0` değil), `İyi cumalar` (`Mutlu cumalar` değil).
   - **Akademik & hukuk:** Akademik atıfta ek yazardan ayrılır (`Yılmaz'a (2024) göre`, `(Yıldız vd. 2022: 14)`, `bk., krş., Tablo 1.`). Hukukta mevzuat/yargı rejimini (*Kanunun 7 nci maddesinin birinci fıkrası, re'sen, zamanaşımı, iyiniyet, elkoyma*) genel TDK ile (*resen, zaman aşımı, iyi niyet, el koyma*) aynı belgede karıştırma; CK 2646 m. 16/8 gereği yeni resmî yazılarda `ünvan, ila, metot, cevabi, hâle, Resmî Gazete` TDK biçimlerini yaz (`müdafi / sanık müdafii`).
8. **AI İmzalarını ve Yapısal Şişirmeleri Temizle:** *"Günümüzün hızla değişen dünyasında"*, *"sadece X değil, aynı zamanda Y"*, *"bu bir A değil, B'dir"*, *"işlevi görmektedir"* (koşaç kaçışı), *"eşsiz deneyim"* (broşür dili), *"X'ten Y'ye kadar"* (yalancı aralık), *"Dürüst olmak gerekirse..."*, *belirsiz kaynaklar*, *boş doğrular*, *gereksiz parantez açılımları*, *aforizma kapanışları* ve mekanik Üçlü Kuralı'nı kaldır; mantık köprüsü kur.
9. **Doğal Ritim ve Nefes (Kota Yok, Kulak Var):** Bütün cümleler 14-20 kelime bandında dizilirse metin tekdüze okunur; buna karşılık her paragrafa zorlama 2 kelimelik kesik cümle çakmak da yapay durur. Uzun, ulaçlı cümlelerle kısa net ifadeleri anlam ve duygu istedikçe harmanla. Sayısal `CoV` ve sıklık eşikleri yalnız üretim sonrası redaksiyon teşhisidir (`06` §7).
10. **Örnek Varsa Örnek Kazanır:** Kullanıcı kendi yazısından örnek verdiyse cümle uzunluğu, hitap, kelime düzeyi ve imla tercihini (tutarlıysa) en üst kural say; aşırı düzeltme ile doğal insan sesini bozma.

---

## Çalışma Modları ve Akış

İsteğin niteliğine göre şu dört moddan uygun olanı seç:

| Mod | Ne zaman | Teslim Biçimi |
|---|---|---|
| **Üretim (`yaz`)** | Sohbet yanıtı, makale, e-posta, hikâye, teknik belge veya mesaj yazarken | İlk cümleden Türkçe düşünülerek üretilmiş temiz çıktı; sohbet artığı (*"Elbette! İşte..."*) yok |
| **Onarım (`duzelt`)** | Mevcut AI kokan, çeviri kokulu veya bozuk bir metni düzeltirken (varsayılan) | Yalnız temizlenmiş metin (kullanıcı rapor istemedikçe açıklama/özet kuyruğu ekleme) |
| **Denetim (`denetle`)** | Kullanıcı metni incelemeni, AI izi veya anlatım bozukluğu bulmanı istediğinde | Metni yeniden yazmadan `P0` (kesin imza), `P1` (sentaks/çeviri), `P2` (TDK/ritim) bulgularını alıntıyla listele |
| **İmla / Resmî (`imla`)** | TDK yazım, kesme, noktalama veya resmî yazı/dilekçe biçimi sorulduğunda | Önce düzeltilmiş tam metin, ardından `Yanlış -> Doğru -> Kural` tablosu |

### 4 Adımlı Kalite Döngüsü

1. **Sicil ve Duygu Kalibrasyonu:** Metnin türünü (Sohbet/Asistan, Blog/Deneme, Teknik, Kurumsal/E-posta, Akademik/Resmî/Hukukî, Edebî/Anlatı, Arayüz) ve taşıması gereken duygu/tutum tonunu belirle.
2. **Taslak / Kurulum:** Konuya doğrudan gir (anons ve sahneleme yapma), cümle iskeletini sola dallanma + ulaç + odak yuvası üzerine kur.
3. **Öz Denetim (Kalıp + Yapı Nakli + TDK):**
   - Kalıbı başka kelimelerle yeniden giydirmedin mi? (*"X'le kalmıyor, Y"* de bir kalıptır!)
   - Aynı açılış veya aynı bağlaç refleks olarak (bilinçli anafora dışında) yığılıyor mu?
   - Uzun tire (`—`), orta çizgi (`–`), saat `:` hatası, Tier-1 klişe veya kof yardımcı fiil kaldı mı?
   - Kısaltma ve yabancı terim ekleri Türkçe okunuşa uygun mu?
4. **Silme Testi:** Metne eklediğin her söylem parçacığı, zarf ve bağlacı sına: çıkarınca anlamdan veya tondan bir şey eksilmiyorsa sil. İkame kelime tikine (*her cümleye refleks "aslında / doğrudan / gerçekten" koymak*) düşme.

---

## Referans Modülleri (İhtiyaç Duyuldukça Oku)

Detaylı gramer, ek, çatı, görünüş, bağlaç, nüans, duygu, söz sanatları, TDK kuralları ve örnekler tek seviye alttaki `references/` klasöründedir. Yalnız görevin gerektirdiği dosyayı aç:

| Konu | Ne zaman okunur | Dosya |
|---|---|---|
| **Cümle Mimarisi, Tamlama ve Bozukluklar** | Sözdizimi, sola dallanma, ulaç sistemi, odak yuvası, çatı/özne-yüklem uyumu, tamlama belirliliği, işaret zamirleri ve `sayesinde/yüzünden` hataları | [01-sentaks-ve-cumle-mimarisi.md](references/01-sentaks-ve-cumle-mimarisi.md) |
| **Ekler, Çatı, Görünüş ve Birleşik Fiiller** | Fiil zamanları/kaymaları, 3 katmanlı geçmiş, dolaylı aktarım, ek sıralaması, kurallı birleşik fiiller, dönüşlü/işteş/ettirgen çatılar, görünüş kalıpları | [02-ekler-kipler-ve-fiil-zenginligi.md](references/02-ekler-kipler-ve-fiil-zenginligi.md) |
| **Bağlaçlar, Edatlar ve Sözcük Nüansları** | Duruma göre bağlaç seçimi (*lakin, oysa, hâlbuki, nitekim, zira, meğer, gelgelelim, diye, şöyle dursun*), açılış paleti, yakın anlam nüansları ve `m-p-r-s` pekiştirmeler | [03-baglaclar-edatlar-ve-parcaciklar.md](references/03-baglaclar-edatlar-ve-parcaciklar.md) |
| **Duygusal İfade, Akış ve Söz Sanatları** | 12 duygu/tavır haritası, ünlemler, ikilemeler, deyim dozajı + Aksoy tuzakları, 27 akış tekniği, süssüz mecaz, sessel ahenk ve açılış/kapanış mimarisi | [04-duygusal-ifade-ve-anlatim-sanati.md](references/04-duygusal-ifade-ve-anlatim-sanati.md) |
| **TDK İmla, Terim ve Hukuk Pusulası** | Kesme, başlık, akademik atıf, üç nokta/eğik çizgi, şapka (`^`), `n-b`/daralma, 3 katmanlı teknik terim politikası ve **TDK vs Mevzuat/CK 2646** | [05-tdk-imla-noktalama-ve-terim.md](references/05-tdk-imla-noktalama-ve-terim.md) |
| **Anti-AI Detox, Akademik & Medya** | Kural hiyerarşisi, Tier 1/2/3 sözlüğü, 12 yapısal AI tuzağı, olgu kilidi, redaksiyon teşhis eşikleri ve **Türkçe Akademik/Medya pusulası** | [06-anti-ai-detox-ve-olgu-kilidi.md](references/06-anti-ai-detox-ve-olgu-kilidi.md) |
| **Sicil Profilleri ve Örnekler** | 7 sicil matrisi, tam CK 2646 özeti, aynı olayın 7 sicilde yazımı ve akademik/yaratıcı akış dahil 8 dönüşüm örneği | [07-sicil-profilleri-ve-ornekler.md](references/07-sicil-profilleri-ve-ornekler.md) |

Yerel terminal/CLI ortamında deterministik ön denetim için standart Python kütüphanesiyle çalışan `python -B scripts/denetle.py <dosya.md> [--register sicil] [--json]` betiği kullanılabilir (ağ ve dış bağımlılık gerektirmez).

## Sınırlar (Aşırı Düzeltme ve Arı Dil Tuzakları)

- **Öz Türkçecilik yapma:** Türkçede yaşayan yabancı kökenli günlük/mesleki sözcükleri (*sistem, strateji, performans, detay, problem*) yapay karşılıklarla değiştirme.
- **Doğal yapıları hata sanma:** Gerçek anlamda bağlama oturan `bir` (*derin bir iz bıraktı*), gerçek eyleyeni öne çıkaran `tarafından` (*Köprü Mimar Sinan tarafından yapıldı*), sıradan ihtimal `belki de` (*belki de haklısın*) ve seyrek devrik/kısa cümlelere dokunma.
- **Yanlış sicil giydirme:** Akademik veya resmî metni blog ağzına indirgeme; sohbet yanıtına da gereksiz resmî `-mAktAdIr` yükleme.
