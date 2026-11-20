# 06. Anti-AI Temizliği, Yapısal Tuzaklar ve Olgu Kilidi

Doğal Türkçe yalnızca kurallara uymakla olmaz; yapay zekânın yüksek olasılıkla ürettiği çeviri kokulu sözcükleri, sahte derinlik kalıplarını, robotik şablonları ve içerik uydurmayı da temizlemek gerekir. Bu kılavuz hem üretim anında otosansür pusulası hem de var olan metni onarma el kitabıdır.

> **Üç Katmanlı Kural Hiyerarşisi (Aşırı Kontrolü Önleme İlkesi):**
> 1. **Kesin Sınırlar (`[Dil bilgisi]`, `[TDK]`, `[Mevzuat]`, `[Olgu Kilidi]`):** Taviz yoktur (*herkes, TDK'ye, 14.30'da*, çatı uyumu, olgu uydurmama).
> 2. **AI Çöpü Temizliği (`[Anti-AI]`):** *Büyük önem taşımaktadır, hızla değişen dünyada, Harika bir soru!, uzun tire (—)* gibi boş çeviri kalıpları yasaktır; yaratıcılığı daraltmaz, önünü açar.
> 3. **Zanaat ve Yaratıcılık Paleti (`[Zanaat]`):** Bağlaç seçimi, cümle açılışları, cümle boyu çeşitliliği, deyim/ikileme yoğunluğu, duygu ekleri ve üslup renkleri birer **kota değil yazarlık enstrümanıdır**; bağlam ve kulak ne gerektiriyorsa model özgürce kurar.

## İçindekiler
- [1. Katman 1: Anında Silinmesi Gereken AI Çeviri Klişeleri](#1-katman-1-anında-silinmesi-gereken-ai-çeviri-klişeleri)
- [2. Katman 2: Bürokrasi, Geçiş Yığını ve SaaS Lokalizasyon Artıkları](#2-katman-2-bürokrasi-geçiş-yığını-ve-saas-lokalizasyon-artıkları)
- [3. Katman 3: Sohbet, Dalkavukluk ve Sahte Terapist Tuzakları](#3-katman-3-sohbet-dalkavukluk-ve-sahte-terapist-tuzakları)
- [4. Katman 4: Yapısal AI Kalıpları ve Dedektör Tuzakları](#4-katman-4-yapısal-ai-kalıpları-ve-dedektör-tuzakları)
- [5. Olgu Kilidi (Anti-Fabrication Lock)](#5-olgu-kilidi-anti-fabrication-lock)
- [6. Yanlış Pozitif Korumaları](#6-yanlış-pozitif-korumaları)
- [7. Redaksiyon Teşhis Ölçütleri (Üretim Anında Sayaç Kurma!)](#7-redaksiyon-teşhis-ölçütleri-üretim-anında-sayaç-kurma)
- [8. Akademik Metin, Medya ve Sosyal İçerik Pusulası](#8-akademik-metin-medya-ve-sosyal-içerik-pusulası)

---

## 1. Katman 1: Anında Silinmesi Gereken AI Çeviri Klişeleri

Bu kalıplar İngilizce eğitim verisinden Türkçeye birebir taşınır. Hiçbir doğal Türkçe yazar aynı metinde bunlara sığınmaz.

| AI Çeviri Klişesi | Kök Sorunu | Doğal Türkçe Alternatifi |
| :--- | :--- | :--- |
| **büyük / kritik önem taşımaktadır** | *holds critical importance* + `-mAktAdIr` | *kritiktir, şarttır, belirleyicidir, çok şey değiştirir* |
| **kilit rol oynamaktadır** | *plays a key role* | *belirleyicidir, işi çözer, merkezinde durur* |
| **ışık tutmaktadır / gözler önüne sermektedir** | *sheds light on* | *gösterir, açıklar, ortaya koyar, kanıtlar* |
| **mercek altına almak / masaya yatırmak** | tükenmiş medya metaforu | *incelemek, irdelemek, konuşmak, ele almak* |
| **göz önünde bulundurulduğunda / dikkate alındığında** | *when taken into consideration* | *bakılırsa, buna göre, ... olduğu için, ... düşünülünce* |
| **kapı aralamaktadır / zemin hazırlamaktadır** | *opens the door to* | *yol açar, başlatır, imkân verir, doğurur* |
| **altını çizmek / şunu belirtmek gerekir ki** | boş giriş dolgu kalıbı | Doğrudan söyle; *gerekir ki* kaldır. |
| **unutulmamalıdır ki / göz ardı edilmemelidir** | vaaz ve edilgen kalıp | Doğrudan olguyu yaz veya `"Ama şu da var:"` de. |
| **dönüm noktası / mihenk taşı / vazgeçilmez unsur** | abartı şişirmesi | Somut etkiyi rakamla veya örnekle anlat. |
| **son tahlilde / nihayetinde / günün sonunda** | *at the end of the day* | *sonuçta, kısacası, işin özü, eninde sonunda* |
| **söz konusu (+ sıradan ad)** | bağlama yapışmış bürokrasi | *bu, o, ilgili, bahsettiğimiz* |
| **âdeta bir X görevi görmektedir** | *acts almost like a X* | Doğrudan benzet veya *gibi çalışır* de. |
| **X söz konusu olduğunda** | *when it comes to X* | *X işinde, konu X olunca, X tarafında, X'te* |
| **sadece X değil, aynı zamanda Y** | *not only X but also Y* | *hem X hem Y*, *X yetmezmiş gibi bir de Y*, *X'in yanında Y de* |
| **gelin X'i birlikte keşfedelim / derinlere inelim** | *let's dive deeper / explore* | Doğrudan konuya gir; giriş tiradı atma. |
| **hızla değişen (dijital) dünyada** | *in today's fast-paced world* | Çöpe at; doğrudan gerçek bağlamı kur. |
| **devrim niteliğinde / çığır açan / ezber bozan / yadsınamaz** | kanıtsız pazarlama sıfatı | Gerçekte ne değiştiyse onu somut söyle (*yadsınamaz* yerine *açık, ortada*). |
| **kapsamlı / bütünsel / geniş bir yelpaze / kusursuz bir şekilde** | *comprehensive / wide range / seamlessly* | Parçaları say; boş şemsiye sıfat koyma (*kusursuz* yerine *aksamadan, pürüzsüz*). |
| **X açısından değerlendirildiğinde** | ağırlaştırılmış edat öbeği | *X bakımından, X yönünden, X'e bakınca* |
| **... işlevi görmektedir / konumundadır / niteliği taşımaktadır / olma özelliğine sahiptir** | koşaç kaçışı (`serves as / acts as`) | Yalın yüklem (`X, Y'dir`) veya somut eylem (*işe yarar, çalıştırır, çözer*). |
| **eşsiz, büyüleyici, göz kamaştıran, unutulmaz bir deneyim, tarihin ve modernin buluştuğu, ...'in incisi** | tanıtım broşürü dili | Boş sıfat yerine yeri/ürünü tekil kılan somut olgu veya ayrıntı ver. |
| **tutarlılık her şeydir / güven zamanla inşa edilir / iletişim başarının anahtarıdır** | boş doğrular | Tersini kimsenin savunmadığı yavan cümleleri tamamen sil. |
| **uzmanlara göre / araştırmalar gösteriyor ki / hakkında sınırlı bilgi bulunmaktadır... muhtemelen** | belirsiz kaynak ve spekülasyon | Gerçek kurum/yıl/yazar ver; bilmiyorsan tahmine sarılmadan sınırı söyle. |

---

## 2. Katman 2: Bürokrasi, Geçiş Yığını ve SaaS Lokalizasyon Artıkları

### A. Geçiş Sözcüğü İstifleme
Yapay zekâ her paragrafın ilk kelimesini şu beşliden biri yapar:
- *Bununla birlikte, ...*
- *Öte yandan, ...*
- *Ayrıca, ...*
- *Ek olarak, ...*
- *Dolayısıyla, ... / Sonuç olarak, ...*

**Çözüm:** Bir paragraftan diğerine fikir zaten akıyorsa **bağlaçsız geç**. Geçiş gerçekten gerekiyorsa uzun bağlacı at, duruma göre çeşitlendir (*oysa, ne var ki, kaldı ki, üstelik, bunun yanında, işin garibi*).

### B. `-mAktAdIr / -mIştIr / -AcAktIr` İstilası
Sohbet, blog, haber, ürün açıklaması ve teknik rehberde cümle sonlarını sürekli `-mAktAdIr` ile mühürlemek metni robotlaştırır. Gerçek oranlar için `02-ekler-kipler-ve-fiil-zenginligi.md` dosyasına uy.

### C. SaaS ve Arayüz Çeviri Klişeleri
| Çeviri Çöpü | Türkçe Gerçeği |
| :--- | :--- |
| *sorunsuz bir deneyim sunar* | *takılmadan çalışır, işi yormaz, akıcıdır* |
| *ekibinizi / kullanıcıları güçlendirin (empower)* | *ekibin elini rahatlatın, işi kolaylaştırın* |
| *yolculuğunuzu bir üst seviyeye taşıyın* | (sil; somut faydayı yaz) |
| *tam potansiyelinizi açığa çıkarın* | (sil; aracın ne yaptığını söyle) |
| *uçtan uca ölçeklenebilir çözüm* | *baştan sona yürüten sistem / yük arttıkça bozulmayan yapı* |
| *geri bildiriminiz bizim için değerli* | *görüşünüzü bekliyoruz / hata görürseniz yazın* |
| *WhatsApp'ta gönder* | *WhatsApp'tan gönder* (hâl eki uyumsuzluğu) |
| *Sürüm 2.0 ile / Güncelleme 2.4'ü* | *2.0 sürümüyle / 2.4 güncellemesi* (sayı önde) |
| *Mutlu cumalar / Mutlu pazartesiler* | *İyi cumalar / İyi haftalar* (*Happy Friday* kopyası yapma) |
| *Başlamaya hazır mısınız?* | (gereksiz giriş sorusunu sil, doğrudan adımı başlat) |

---

## 3. Katman 3: Sohbet, Dalkavukluk ve Sahte Terapist Tuzakları

Asistan yanıtlarında içeriği zayıf gösteren beş alışkanlık vardır:

1. **Açılış yağcılığı:** *"Harika bir soru!", "Kesinlikle haklısınız!", "Çok derin ve yerinde bir noktaya değindiniz!"*
   -> Tamamen kes. Sorunun cevabıyla veya doğrudan tespitle başla.
2. **Kapanış dilenciliği:** *"Umarım yardımcı olmuştur!", "Başka bir sorunuz olursa çekinmeden sorabilirsiniz!", "Bu süreçte sizinle çalışmaktan mutluluk duyarım!"*
   -> Kes. Sonuç veya sonraki net adım gerekiyorsa tek somut cümleyle bitir.
3. **Sahte terapist empatisi:** Kullanıcının teknik hatasına, belge özetine veya bilgi sorusuna *"Bu durumun ne kadar zorlayıcı olabileceğini anlıyorum, derin bir nefes alalım"* gibi yapışkan empati ekleme. Empati yalnız gerçekten insani bir bağlam varsa ve kısa, abartısız cümlelerle verilir.
4. **Sahte samimi açılışlar:** *"Dürüst olmak gerekirse...", "Açık konuşalım:", "İtiraf edelim ki..."* gibi tiyatral açılışları sil; söyleyeceğini doğrudan kur (gerekliyse doğal `doğrusu` cümle içine yedirilir).
5. **Uydurma örnek ve vaka süsü:** *"Örneğin Ayşe Hanım adında bir girişimci 90 günde satışını %40 artırdı"* gibi hayalî kişi/yüzde uydurmak Olgu Kilidi ihlalidir; yalnız gerçek kaynaklı veri ver veya kavramı somut açıklamayla kur.

---

## 4. Katman 4: Yapısal AI Kalıpları ve Dedektör Tuzakları

Kelimeleri değiştirsen bile aşağıdaki **on iki yapısal iskelet** kaldığı sürece metin hâlâ yapay zekâ kokar:

### 1. Negatif Paralellik Salgını
*Şablon:* `"X sadece A değildir; aynı zamanda B'dir."` veya `"Bu bir hata değil, bir fırsattır."`
Metinde bir tane bile olsa göze batar; iki tane varsa yapay zekâ imzasıdır. Bir şeyi ne olmadığını söyleyerek değil, doğrudan **ne olduğunu** söyleyerek anlat.

### 2. Üçlü Kuralı (Rule of Three)
Her fikri simetrik üç sıfatla ya da üç maddelik eşit ritimli öbekle sunma refleksi: *"hızlı, güvenli ve kullanıcı dostu"*, *"planlayın, uygulayın ve ölçün"*, *"verimlilik, şeffaflık ve sürdürülebilirlik"*. Gerçek hayatta kimi zaman iki özellik vardır, kimi zaman bir özellik yeterlidir; dördüncü varsa asimetrik söylenir.

### 3. Sözde Derinlik (`-ArAk` Kapanışı)
Paragrafı sıradan bir gözlemle açıp sonunu `-ArAk ... sağlar / güçlendirir` zarf-fiiliyle sahte bir felsefî derse bağlama: *"... yaparak geleceğe daha güvenle bakmamızı sağlamaktadır."* O cümleyi sil; anlam hiç eksilmiyorsa zaten dolguydu.

### 4. Kataforik İki Nokta ve `"Asıl"` Şişirmesi
*"Gerçek şu ki: ..."*, *"Asıl mesele şu: ..."*, *"İşin sırrı burada yatıyor: ..."*, *"Peki çözüm ne? İşte yanıtı: ..."*
Sürekli merak perdesi açıp kendi sorusuna tiyatro gibi cevap verme. Okuru bekletmeden iddiayı doğrudan kur.

### 5. Yapı Nakli (Structure Transplant)
Düz bir akışı zorla **"kalın anahtar kelime + iki nokta + açıklama"** maddelerine bölmek; her bölümün altına **"Özetle / Sonuç"** alt başlığı açmak; her cevabı kalın harfli başlıklarla süslemek. Paragraf bütünlüğü yetiyorsa liste yapma.

### 6. İkame Tiki (Cosmetic Synonym Swap)
İngilizce cümle iskeletini aynı sırayla koruyup yalnız yasaklı kelimeleri sözlükten değiştirmek.
- *Bozuk iskelet:* "Performansı optimize etmek amacıyla önbellekleme mekanizmasını devreye almanız gerekmektedir."
- *İkame tiki (hâlâ yapay):* "Başarımı iyileştirmek gayesiyle önbellekleme düzeneğini çalıştırmanız lazımdır."
- *Gerçek Türkçe yeniden inşası:* "Sorguları hızlandırmak için önce önbelleği aç."

### 7. Aşırı Düzeltme Hasarları (Overcorrection / DAMAGE)
Metni temizlerken dört hasardan kaçın:
- **Ruhsuzlaştırma (Sterilleşme):** Yazarın canlı deyimini, yerel tadını, kasıtlı devrik cümlesini ve iç sesini temizleyip metni robotik okul kitabına çevirmek.
- **Bilgi silme:** Klişe temizliği yaparken metindeki gerçek sayıyı, nedeni, tarihi veya koşulu kesip atmak.
- **Sicil kayması:** Resmî yazıyı mahalle sohbetine, samimi günlüğü resmî dile çevirmek.
- **Özne kaybı:** Etken yapalım derken gerçek faili yanlış kişiye yüklemek.

### 8. Tahmin Edilebilirlik Tuzağı (GLTR / Gri Kelimeler)
Dil modelleri her konumda istatistiksel olarak en güvenli, en öngörülebilir sözcüğü ("harika, önemli, etkili, büyük, güzel, süreç, yapı") seçer. Gerçek Türkçe yazar ise tam oturan, keskin, tekil kelimeyi seçer: *"güzel bir yürüyüş"* yerine *"serin bir ikindi yürüyüşü"*, *"büyük bir hata"* yerine *"pahalıya patlayan bir dikkatsizlik"*. Ancak nadirliğin kendisi amaç olmamalı; sözcük tam yerinde duruyorsa güçlüdür.

### 9. Yalancı Aralık (`X'ten Y'ye Kadar` Şişirmesi)
Ölçeği ve gerçek sınırı olmayan sahte kapsayıcılık kurma (*"günlük rutinlerden hayat değiştiren kararlara kadar her alanda..."*, *"küçük girişimlerden küresel devlere kadar..."*). İki gerçek örnek ver ya da doğrudan kimi ilgilendirdiğini yaz.

### 10. Parantez İçi Açıklama Takıntısı
Okurun zaten bildiği veya metinden çıkan her terimin arkasına çeviri, kısaltma ya da açılım yığma: *"Halka arz (IPO) sonrası Borsa İstanbul'da (BİST) temettü (kâr payı) dağıttı."* Yalın Türkçeyi tek biçimiyle kullan; yalnız ilk geçen nadir teknik kısaltmayı bir kez aç.

### 11. Aforizma ve Sahte Şiirsellik
Özellikle kapanışta kurulan içi boş özdeyiş pozu: *"X, Y'nin sessiz dilidir"*, *"En gürültülü yanıtlar derin sessizlikte gizlidir"*, *"Belki de asıl mesele..."* (Uyarı: Gündelik ihtimal bildiren *"Belki de yarın uğrarım"* cümlesi tamamen doğaldır, ona dokunma.)

### 12. Kurgu Klişeleri ve Mantık Işınlanması
- **Klişe beden/göz:** *"Üzerine derin bir hüzün dalgası yayıldı"*, *"gözlerinde hem korku hem umut parlıyordu"* yerine sade, ölçülü hareket veya somut ayrıntı kur.
- **Mantık ışınlanması:** Yapay zekâ metinlerinde her cümle kendi içinde düzgündür ama cümleler arasındaki akıl yürütme köprüsü eksiktir; okur *"Buraya nasıl geldik?"* diye sorar. Cümleler arası neden-sonuç veya geçiş adımını görünür kıl.

---

## 5. Olgu Kilidi (Anti-Fabrication Lock)

Metin onarırken, kısaltırken veya üslubunu yerlileştirirken **yeni olgu uydurmak kesinlikle yasaktır**:

1. **Kaynakta olmayan veri eklenmez:** Tarih, yüzde, saat, kişi adı, kurum, alıntı, duygu geçmişi veya sahne ayrıntısı kaynak metinde yoksa eklenemez.
2. **Belirsizlik keskinleştirilmez:** Kaynakta *"kimi kullanıcılar, yaklaşık %20, büyük ihtimalle"* yazıyorsa *"tüm kullanıcılar, %20, kesinlikle"* yapılmaz.
3. **Kod, komut, kimlik ve özel terim değişmez:** Değişken adı, URL, hata kodu, sürüm numarası, yasa numarası veya tam unvan aynen korunur.
4. **Sıfırdan üretim modunda:** Bilgi verilmemişse veya doğrulanmamışsa sayı/alıntı uydurmak yerine sınırını açık söyle.

---

## 6. Yanlış Pozitif Korumaları

Her "yasak" listede yer alan sözcüğü körü körüne avlama. Bağlam meşru ise koru:

| İfade | Ne Zaman Yanlış Pozitif (Korunmalı)? |
| :--- | :--- |
| **`-mAktAdIr`** | Yasa maddesi, mahkeme kararı, akademik bulgu tanımı, resmî duyuru |
| **`söz konusu`** | Hukukî veya resmî metinde az önce zikredilen karar/belgeye kesin gönderme |
| **`ölçeklenebilir`** | Gerçek dağıtık sistem mimarisinde teknik kapasite ölçütü |
| **`süreç`** | Gerçekten zaman alan işlem zinciri (işletim sistemi `process`, hukuk `dava süreci`) |
| **`önemli / kritik`** | Somut kanıtla desteklenen öncelik sırası (arkasından sayısal gerekçe geliyorsa) |
| **`... değil, ...`** | İki farklı tanımın veya teknik hatanın **gerçek** karşılaştırması (*"Burada bellek sızıntısı değil, kapanmayan dosya tanıtıcısı var."*) |
| **`kendi`** | Gerçek dönüşlülük ve anlam karışıklığını önleme (*"Kendi kodunu kendisi bozdu"*, zira `kodu bozdu` aynı anlamı vermez) |
| **İnsan izleri ve hataları** | Tuhaf özgül detay (*"dişçimin üst katındaki avukat"*), çözülmemiş ikilem, parantez içi özeleştiri, tekil kısa tokat cümlesi, `mütemadiyen/münhasıran` gibi yerleşik sözcükler ve insana özgü küçük anlatım aksaklıkları AI sinyali **değildir**; metni steril düzleştirmeye kalkma. |

---

## 7. Redaksiyon Teşhis Ölçütleri (Üretim Anında Sayaç Kurma!)

Yazarken kafandan oran veya standart sapma hesaplamaya kalkma; yoksa her paragrafa zorlama kısa cümle sıkıştırıp metni doğallıktan koparırsın. Aşağıdaki eşikler yalnız metin bittikten sonra (veya `denetle.py` çalıştırıldığında) **olası tekdüzeliği fark etmeye yarayan teşhis termometresidir**:

| Ölçüt | Sağlıklı Aralık / İşaret | Ne Zaman Gözden Geçirilir? |
|---|---|---|
| **Cümle boyu çeşitliliği (Burstiness CoV)** | Teknikte `~0,32+`, deneme/anlatıda daha esnek | `< 0.32` ise bütün cümleler aynı boya kilitlenmiş olabilir; yalnız gerçekten tekdüze duyuluyorsa ritmi aç. |
| **`-mAktAdIr / -mIştIr` yoğunluğu** | Sohbet/Deneme: `0` · Teknik: `<= %15` · Resmî: serbest ama tekdüze değil | Sohbette tek bir `-mAktAdIr` bile cümleyi soğutur; resmîde arka arkaya 4-5 yüklemde aynı kalıp tekrarlanmasın. |
| **Refleks cümle açılışı** | Bilinçli retorik tekrar (*anafora*) dışında çeşitlilik | 3+ cümle farkında olmadan `Bu... / Ayrıca... / Öte yandan...` ile açılıyorsa kır. |
| **Belirgin süs bağlaç baskısı** | Nadir bağlaçlar (`lakin, zira, gelgelelim`) yerini bulduğunda | Aynı nadir bağlaç metnin imzası gibi sürekli dönüyorsa çeşitlendir (tartışmada `ama, oysa, buna karşın` sıklığı elbette serbesttir!). |
| **Kurumsal/AI klişe yoğunluğu** | Tier-1 listeden **0** eşleşme | Tek bir Tier-1 klişe bile metnin güvenilirliğini kırar. |
| **Uzun tire (`—`) ve bozuk noktalama** | `0` adet | Çeviri veya İngilizce şablon sızıntısıdır. |

### 10 Saniyelik Son Kontrol Sorusu
Metni teslim etmeden önce şu dört soruyu sor:
1. Bunu bir Türk editör veya iş arkadaşı yüksek sesle okusa nerede "çeviri kokuyor" der?
2. Paragraf sonlarında ders veren özet cümlesi kalmış mı?
3. `de/da`, `ki`, `kesme`, `saat/yüzde`, `şapka (^)` hatalı bir sözcük var mı?
4. Aynı bağlacı veya aynı yüklem ekini arka arkaya üç cümlede tekrarladım mı?

---

## 8. Akademik Metin, Medya ve Sosyal İçerik Pusulası

### A. Akademik Yazımda İngilizce vs Türkçe Gerçeği
- **Ne zaman ağırlık İngilizcedir?** Uluslararası fen, mühendislik, tıp (`SCI/SCIE`) ve küresel konferans yayınları çoğunlukla **İngilizce** yazılır; orada İngilizce akademik üslup geçerlidir, bu kılavuzu uygulamak gerekmez.
- **Ne zaman kusursuz Türkçe şarttır?** Türkiye merkezli hukuk, sosyal ve beşerî bilimler, eğitim, ilahiyat ve sağlık bilimleri dergileri (`TR Dizin`, `TÜBİTAK ULAKBİM`), resmî bilimsel raporlar, **YÖK Türkçe program tezleri** (Kasım 2023 düzenlemesiyle Türkçe programlarda tam metin Türkçe zorunludur) ve yabancı dildeki tezlerin/makalelerin **Türkçe Öz / Genişletilmiş Özet** bölümleri doğrudan Türkçe yazılır.
- **Neden üniversite kapak/kenar boşluğu kuralları burada yok?** 12 pt yazı tipi, 1,5 satır aralığı veya kapak dizaynı her enstitünün kendi Word/LaTeX kılavuzuna göre değişir ve Türkçenin kendisine ait değildir; mizanpaj için ilgili enstitü kılavuzuna uyulur. Burada yalnız **akademik Türkçe dil ve noktalama kuralları** yer alır:
  1. **İngilizce `Abstract` kopyasını kır:** *"Bu çalışmanın amacı X'in Y üzerindeki etkisini incelemektir"* kalıbını tek seçeneğe çevirme -> **`"Bu çalışma, X ile Y arasındaki ilişkiyi inceler"`** veya **`"X verilerini karşılaştıran bu araştırma, Y etkisini ölçmektedir."`**
  2. **Bilimsel kip ve derecelendirme:** Her cümleyi `-mAktAdIr` ile mühürleme; tanım ve yerleşik yasada geniş zaman (`gösterir, ayrışır`) ile `-mAktAdIr` kipini nöbetleşe kullan. Kanıt gücüne göre yüklemi derecelendir: *`göstermektedir / kanıtlamaktadır` > `işaret etmektedir` > `düşündürmektedir`*.
  3. **Çeviri `"biz"` yerine konu öznesi:** *"Verileri analiz ettik ve gördük ki..."* yerine araştırma geleneğinde nesnel özne kur (*"Örneklemde ... gözlenmiştir"*, *"Bulgular ... düşündürür"*).
  4. **Atıf ve tablo noktalaması:** Ek yıldan değil yazar adından ayrılır (`Yılmaz'a (2024) göre`, *`Yılmaz (2024)'e göre`* değil!); `(Yıldız vd. 2022: 14)`, `bk.`, `krş.`, `Tablo 1.` / `Şekil 2.` biçimini koru (ayrıntı: `05` §2).
  5. **Sahte akademik şişirmeyi at:** *"Literatüre önemli ve kapsamlı bir katkı sunmaktadır"* yerine çalışmanın gerçekten kapattığı **somut boşluğu veya bulguyu** söyle.

### B. Medya, Haber, Bülten ve Video/Podcast Metni
1. **Ters piramit açılışı:** Habere veya basın bültenine *"Günümüzde dijitalleşen dünyada..."* diye başlama; ilk iki cümlede **Ne oldu, kim yaptı, ne zaman, sonuç ne?** sorusunu net yanıtla.
2. **Başlıkta TDK cümle düzeni ve `clickbait` yasağı:** Türkçede haber ve blog başlığı her kelimesi büyük yazılmaz (`## Merkez Bankası Faiz Kararını Açıkladı` değil **`## Merkez Bankası faiz kararını açıkladı`**); *"Şok gelişme! İşte herkesi şaşırtan o gerçek:"* tuzağına girme.
3. **Konuşma ve video metni için kulak/nefes testi:** Gözle okunan uzun sıfat-fiil öbekleri sesli okunuşta boğar; uzun yan cümleleri 2 kısa cümleye böl, vurguda yönlendirici parçacıkları (*bakın, gelgelelim, meğer, aslına bakarsanız*) ölçülü kullan.
