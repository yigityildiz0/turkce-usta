#!/usr/bin/env python3
"""Türkçe metinlerde AI kalıplarını, sözdizimi tekdüzeliğini ve TDK/üslup hatalarını denetler."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

VOWELS = set("aeıioöuüAEIİOÖUÜâîûÂÎÛ")

REGISTERS = ("sohbet", "blog", "teknik", "kurumsal", "resmi", "edebi", "ux")

MAKTA_LIMITS = {
    "sohbet": 0.0,
    "blog": 0.0,
    "edebi": 0.0,
    "ux": 0.0,
    "teknik": 15.0,
    "kurumsal": 15.0,
    "resmi": 100.0,
}

TIER1_CLICHES = (
    (r"\b(?:büyük|kritik|hayati)\s+(?:bir\s+)?önem\s+taşı\w*", "Tier-1 klişe: 'önem taşımaktadır' yerine doğrudan 'kritiktir / belirleyicidir' kullan"),
    (r"\bkilit\s+(?:bir\s+)?rol\s+oyna\w*", "Tier-1 klişe: 'kilit rol oynamak' yerine somut etkiyi yaz"),
    (r"\bışık\s+tut\w*", "Tier-1 klişe: 'ışık tutmak' yerine 'açıklar / gösterir'"),
    (r"\bgözler\s+önüne\s+ser\w*", "Tier-1 klişe: 'gözler önüne sermek' yerine 'ortaya koyar / gösterir'"),
    (r"\bmercek\s+altına\s+al\w*", "Tier-1 klişe: 'mercek altına almak' yerine 'incelemek'"),
    (r"\bmasaya\s+yatır\w*", "Tier-1 klişe: 'masaya yatırmak' yerine 'ele almak / tartışmak'"),
    (r"\b(?:göz\s+önünde\s+bulundurulduğunda|dikkate\s+alındığında)\b", "Tier-1 klişe: İngilizce 'when taken into consideration' çevirisi"),
    (r"\b(?:kapı\s+arala\w*|zemin\s+hazırla\w*)\b", "Tier-1 klişe: 'kapı aralamak / zemin hazırlamak' yerine 'yol açar / başlatır'"),
    (r"\b(?:altını\s+çizmek|şunu\s+belirtmek|vurgulamak)\s+gerekir\s+ki\b", "Tier-1 dolgu giriş: gereksiz 'gerekir ki' öbeğini sil"),
    (r"\b(?:unutulmamalıdır\s+ki|göz\s+ardı\s+edilmemelidir)\b", "Tier-1 vaaz kalıbı: doğrudan olguyu yaz"),
    (r"\b(?:son\s+tahlilde|nihayetinde|günün\s+sonunda)\b", "Tier-1 klişe: 'sonuçta / kısacası' yeter"),
    (r"\bbu\s+(?:bağlamda|doğrultuda|çerçevede)\b", "Tier-1 geçiş klişesi: gerekmiyorsa sil"),
    (r"\bhızla\s+değişen\s+(?:dijital\s+)?dünya\w*", "Tier-1 boş giriş: 'hızla değişen dünyada' kalıbını çöpe at"),
    (r"\b(?:devrim\s+niteliğinde|çığır\s+açan|ezber\s+bozan|yadsınamaz\w*)\b", "Tier-1 abartı sıfatı: ne değiştiğini kanıtla anlat"),
    (r"\b(?:geniş\s+bir\s+yelpaze\w*|kusursuz\s+bir\s+şekilde)\b", "Tier-1 kalıp öbek: somut say veya 'aksamadan / pürüzsüz' de"),
    (r"\bsöz\s+konusu\s+olduğunda\b", "Tier-1 çeviri: 'when it comes to' calque kalıbı"),
    (r"\bsadece\s+.{2,60}?\s+(?:değil|kalma\w*),?\s+aynı\s+zamanda\b", "Tier-1 negatif paralellik: 'hem ... hem ...' veya yalın cümle kur"),
    (r"\b(?:gelin\s+.{2,40}?\s+keşfedelim|derinlere\s+inelim|derinlemesine\s+in\w*)\b", "Tier-1 anlatım klişesi: giriş tiyatrosunu kes"),
    (r"\b(?:dönüm\s+noktası|mihenk\s+taşı|vazgeçilmez\s+bir\s+unsur)\b", "Tier-1 şişirme ad öbeği"),
    (r"\b(?:geliştir\w*|tasarla\w*|uygula\w*)\s+yardımcı\s+ol\w*|\b(?:yardımcı|katkı)\s+(?:olmakla|sunmakla)\s+kalma\w*", "Tier-1 yapı: çeviri dolgu fiili"),
    (r"\byalnızca\s+.{2,60}?\s+(?:olmakla|göstermekle)\s+kalma\w*", "Tier-1 negatif paralellik: 'not only ... but also' kalıbı"),
    (r"\b(?:işlevi\s+görmekte\w*|konumunda\s+bulunmakta\w*|olarak\s+hizmet\s+vermekte\w*|niteliği\s+taşımakta\w*)", "Tier-1 koşaç kaçışı: yalın ad yüklemi veya somut eylem kur"),
    (r"\b(?:eşsiz|büyüleyici|göz\s+kamaştıran)\s+bir\s+(?:deneyim|atmosfer|yolculuk)\b", "Tier-1 broşür dili: boş övgü yerine somut ayrıntı ver"),
    (r"\bhakkında\s+sınırlı\s+bilgi\s+bulunmakta\w*", "Tier-1 belirsiz spekülasyon kalıbı: sınırı doğrudan söyle"),
    (r"\b(?:kapsamlı|bütünsel|holistik)\s+bir\s+(?:yaklaşım|bakış\s+açısı|çözüm)\b", "Tier-1 boş şemsiye sıfat"),
)

TIER2_PATTERNS = (
    (r"\bsorunsuz\s+bir\s+deneyim\b", "Tier-2 SaaS çevirisi: 'takılmadan çalışır / akıcıdır'"),
    (r"\bbir\s+üst\s+seviyeye\s+taşı\w*", "Tier-2 SaaS klişesi: somut fayda yaz"),
    (r"\btam\s+potansiyelin\w*\s+(?:açığa\s+çıkar|ortaya\s+koy)\w*", "Tier-2 pazarlama klişesi"),
    (r"\buçtan\s+uca\s+(?:ölçeklenebilir\s+)?çözüm\w*", "Tier-2 SaaS kalıbı"),
    (r"\bWhatsApp'ta\s+gönder\w*", "Tier-2 arayüz/hâl eki hatası -> 'WhatsApp'tan gönder'"),
    (r"\b(?:güncelleme|sürüm|versiyon|yama)\s+\d+(?:\.\d+){1,3}(?![.\d])(?<!\.\d{4})", "Tier-2 sürüm sırası -> sayı önde olmalı ('2.4 güncellemesi')"),
    (r"\bmutlu\s+(?:pazartesi|salı|çarşamba|perşembe|cuma|cumartesi|pazar)(?:ler|lar)\b", "Tier-2 çeviri selamı -> 'İyi cumalar / İyi haftalar'"),
    (r"^(?:Harika|Çok\s+güzel|Müthiş)\s+bir\s+soru\b", "Tier-3 dalkavukluk: doğrudan yanıta gir"),
    (r"^(?:Dürüst\s+olmak\s+gerekirse|Açık\s+konuşalım)\s*[:,]", "Tier-3 sahte samimi açılış: yargıyı doğrudan söyle"),
    (r"\b(?:Umarım\s+(?:bu\s+bilgiler\s+)?faydalı\s+olmuştur|Başka\s+bir\s+sorunuz\s+olursa)\b", "Tier-3 kapanış dilenciliği"),
)

TDK_TYPOS = (
    (r"\bherkez\w*\b", "'herkez' değil -> 'herkes'"),
    (r"\byanlız\w*\b", "'yanlız' değil -> 'yalnız'"),
    (r"\byalnış\w*\b", "'yalnış' değil -> 'yanlış'"),
    (r"\byada\b", "'yada' değil -> 'ya da' (ayrı)"),
    (r"\bşarz\w*\b", "'şarz' değil -> 'şarj'"),
    (r"\bsüpriz\w*\b", "'süpriz' değil -> 'sürpriz'"),
    (r"\bşöför\w*\b", "'şöför' değil -> 'şoför'"),
    (r"\binsiyatif\w*\b", "'insiyatif' değil -> 'inisiyatif'"),
    (r"\bklavuz\w*\b", "'klavuz' değil -> 'kılavuz'"),
    (r"\bdöküman\w*\b", "'döküman' değil -> 'doküman'"),
    (r"\btraş\w*\b", "'traş' değil -> 'tıraş'"),
    (r"\btekrardan\b", "'tekrardan' yerine -> 'tekrar / yeniden'"),
    (r"\byakinen\b", "'yakinen' değil -> 'yakından'"),
    (r"\borjinal\w*\b", "'orjinal' değil -> 'orijinal'"),
    (r"\bstajer\w*\b", "'stajer' değil -> 'stajyer'"),
    (r"\btesbit\w*\b", "'tesbit' değil -> 'tespit'"),
    (r"\btehtid\w*\b", "'tehtid' değil -> 'tehdit'"),
    (r"\bespiri\w*\b", "'espiri' değil -> 'espri'"),
    (r"\brestorant\w*\b", "'restorant' değil -> 'restoran'"),
    (r"\brepertuar\w*\b", "'repertuar' değil -> 'repertuvar'"),
    (r"\bvejeteryan\w*\b", "'vejeteryan' değil -> 'vejetaryen'"),
    (r"\btabiki\b", "'tabiki' değil -> 'tabii ki'"),
    (r"\btabi\s+ki\b", "'tabi ki' değil -> 'tabii ki'"),
    (r"\bküsür\w*\b", "'küsür' değil -> 'küsur'"),
    (r"\bbirşey\w*\b", "'birşey' değil -> 'bir şey'"),
    (r"\bherşey\w*\b", "'herşey' değil -> 'her şey'"),
    (r"\bhiçbirşey\w*\b", "'hiçbirşey' değil -> 'hiçbir şey'"),
    (r"\bbir\s+çok\b", "'bir çok' değil -> 'birçok' (bitişik)"),
    (r"\bbir\s+kaç\b", "'bir kaç' değil -> 'birkaç' (bitişik)"),
    (r"\bhiç\s+bir\w*\b", "'hiç bir' değil -> 'hiçbir' (bitişik)"),
    (r"\bvaz\s+geç\w*\b", "'vaz geçmek' değil -> 'vazgeçmek' (bitişik)"),
    (r"\bterket\w*\b", "'terketmek' değil -> 'terk etmek' (ayrı)"),
    (r"\bfarket\w*\b", "'farketmek' değil -> 'fark etmek' (ayrı)"),
    (r"\barzet\w*\b", "'arzetmek' değil -> 'arz etmek' (ayrı)"),
    (r"\bhaket\w*\b", "'haketmek' değil -> 'hak etmek' (ayrı)"),
    (r"\bva[ad]t\s+et\w*\b", "'vaat/vaad etmek' değil -> 'vadetmek' (bitişik)"),
    (r"\bdef\s+et\w*\b", "'def etmek' değil -> 'defetmek' (bitişik)"),
    (r"\bmen\s+et\w*\b", "'men etmek' değil -> 'menetmek' (bitişik)"),
    (r"\bmahv\s+et\w*\b", "'mahv etmek' değil -> 'mahvetmek' (bitişik)"),
    (r"\byanısıra\b", "'yanısıra' değil -> 'yanı sıra' (ayrı)"),
    (r"\bpeşisıra\b", "'peşisıra' değil -> 'peşi sıra' (ayrı)"),
    (r"\bhaftasonu\w*\b", "'haftasonu' değil -> 'hafta sonu' (ayrı)"),
    (r"\byurtiçi\w*\b", "'yurtiçi' değil -> 'yurt içi' (ayrı)"),
    (r"\byurtdışı\w*\b", "'yurtdışı' değil -> 'yurt dışı' (ayrı)"),
    (r"\bveritaban\w*\b", "'veritabanı' değil -> 'veri tabanı' (ayrı)"),
    (r"\bözgeçmiş\w*\b", "'özgeçmiş' değil -> 'öz geçmiş' (ayrı)"),
    (r"\bönsöz\w*\b", "'önsöz' değil -> 'ön söz' (ayrı)"),
    (r"\baltyazı\w*\b", "'altyazı' değil -> 'alt yazı' (ayrı)"),
    (r"\bdoğalgaz\w*\b", "'doğalgaz' değil -> 'doğal gaz' (ayrı)"),
    (r"\bkuruyemiş\w*\b", "'kuruyemiş' değil -> 'kuru yemiş' (ayrı)"),
    (r"\bunvan\w*\b", "TDK 12. baskı: 'unvan' değil -> 'ünvan'"),
    (r"\bkayyum\w*\b", "TDK 12. baskı: 'kayyum' değil -> 'kayyım'"),
    (r"\bçiğ\s+börek\w*\b", "TDK 12. baskı: 'çiğ börek' değil -> 'çi börek'"),
    (r"\byeşilsoğan\w*\b", "TDK 12. baskı: 'yeşilsoğan' değil -> 'yeşil soğan'"),
    (r"\byeşilbiber\w*\b", "TDK 12. baskı: 'yeşilbiber' değil -> 'yeşil biber'"),
    (r"\bhasıraltı\b", "TDK 12. baskı: 'hasıraltı' değil -> 'hasır altı'"),
    (r"\bdoğubeyazıt\w*\b", "TDK 12. baskı: 'Doğubeyazıt' değil -> 'Doğubayazıt'"),
    (r"\b(?:hukuğ\w*|evrağ\w*|stoğ\w*)\b", "Alıntı -k sert kalır -> hukuku, evrakı, stoku"),
    (r"\b(?:başlıyacak\w*|gelmiyen\w*|olmıyan\w*|anlıyacak\w*|bekliyen\w*|demiyen\w*|yemiyen\w*)\b", "Ünlü daralması yazıda yalnız -yor öncesi ve de-/ye- köklerinde olur -> başlayacak, gelmeyen..."),
    (r"\b(?:ombaşı\w*|bimbaşı\w*|sombahar\w*|gümbatım\w*)\b", "n-b çatışması birleşik sözcüklerde uygulanmaz -> onbaşı, binbaşı, sonbahar, günbatımı"),
    (r"\b(?:müdafisi|müdafiisi|müdafisin\w*|müdafiisin\w*)\b", "'müdafi' tek i ile yazılır; tamlamada 'müdafii' olur, çift iyelik (-si) gelmez"),
    (r"\bres'en\b", "Kesme yeri yanlış: TDK 'resen', yargı geleneği 're'sen' (asla 'res'en' değil)"),
    (r"\b(?:kağıt\w*|rüzgar\w*|dükkan\w*|hikaye\w*|mahkum\w*)\b", "TDK şapka (^) gerekir -> kâğıt, rüzgâr, dükkân, hikâye, mahkûm"),
    (r"\b(?:hâkim\s+ol\w*|hakim\s+karar\w*)\b", "hakim (bilge) / hâkim (yargıç) ayrımını bağlama göre kontrol et"),
    (r"\b(?:lâzım\w*|lâyık\w*)\b", "TDK'ye göre cins isimde ince l sonrası şapka konmaz -> lazım, layık"),
    (r"\bomuz\s+omza\b", "İkilemede ünlü düşmez -> 'omuz omuza'"),
    (r"\bburun\s+burna\b", "İkilemede ünlü düşmez -> 'burun buruna'"),
    (r"\bnesilden\s+nesle\b", "İkilemede ünlü düşmez -> 'nesilden nesile'"),
    (r"\b(?:TDK'ya|TDK'nın|TDK'da|TDK'dan|TBMM'ne|THY'na|THY'nın|SSK'ya|HMK'nun|CMK'nun|TMK'nun|TCK'nun)\b", "Büyük harfli kısaltmada ek harf okunuşuna göre gelir (TDK'ye, TBMM'ye, THY'nin, HMK'nin)"),
    (r"\b(?:cache'yi|cache'de|cache'a|queue'yi|queue'de|API'yı|API'ya|API'da|SQL'ı|SQL'a|JSON'i|JSON'e|merge'i|branch'ı|commit'ı|commit'de|URL'ı|URL'da|CPU'yi|CPU'de|GitHub'de|GitHub'ta|Google'de|Google'i|Node\.js'da|Node\.js'de|X'de|X'da)\b", "Terim son sesine göre ek almalı (ör. cache'i, queue'yu, URL'yi, CPU'yu, GitHub'da, Node.js'te, X'te)"),
    (r"\bhalihazırda\b", "TDK şapka (^) ve bitişik -> 'hâlihazırda'"),
    (r"\bçevrim(?:içi|dışı)\w*\b", "TDK ayrı yazım -> 'çevrim içi / çevrim dışı'"),
)

_UNITS = {1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz"}
_TENS = {1: "on", 2: "yirmi", 3: "otuz", 4: "kırk", 5: "elli"}
_BACK_VOWELS = set("aıou")
_FRONT_VOWELS = set("eiöü")
_HARD_CONSONANTS = set("fstkçşhp")
CONJUNCTION_WATCH = ("lakin", "zira", "hâlbuki", "halbuki", "nitekim", "meğer", "gelgelelim")


def _expected_time_suffix(hour: int, minute: int, ablative: bool) -> str:
    """'14.30' -> 'da' (otuzda), '13.00' -> 'te' (on üçte) uyumluluğunu hesaplar."""
    n = minute if minute else hour
    word = _UNITS[n % 10] if n % 10 else (_TENS.get(n // 10, "sıfır") if n else "sıfır")
    last_vowel = next(ch for ch in reversed(word) if ch in _BACK_VOWELS | _FRONT_VOWELS)
    vowel = "a" if last_vowel in _BACK_VOWELS else "e"
    consonant = "t" if word[-1] in _HARD_CONSONANTS else "d"
    return consonant + vowel + ("n" if ablative else "")


def tr_lower(text: str) -> str:
    """Türkçe I/İ dönüşümünü birleşen nokta artığı bırakmadan küçültür."""
    return text.replace("İ", "i").replace("I", "ı").lower()


def strip_non_prose(text: str) -> str:
    """YAML başlığını, kod bloklarını, satır içi kodları ve URL'leri temizler."""
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]+`", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text)
    return text


def split_sentences(prose: str) -> list[str]:
    """Markdown başlıklarını ve cümleleri kabaca ayırır."""
    lines = []
    for raw in prose.splitlines():
        s = raw.strip()
        if not s or s.startswith("#") or s.startswith("|") or re.fullmatch(r"[-*_]{3,}", s):
            continue
        s = re.sub(r"^(?:[-*+]\s+|\d+[.)]\s+|>\s+)", "", s)
        lines.append(s)
    joined = " ".join(lines)
    chunks = re.split(r"(?<=[.!?])\s+(?=[A-ZÇĞİÖŞÜ0-9\"“])", joined)
    return [c.strip() for c in chunks if len(c.split()) >= 2]


def atesman_score(words: list[str], sentence_count: int) -> float | None:
    """Türkçe Ateşman okunabilirlik puanını hesaplar."""
    if not words or sentence_count == 0:
        return None
    syllables = sum(sum(1 for ch in w if ch in VOWELS) for w in words)
    if syllables == 0:
        return None
    avg_syll = syllables / len(words)
    avg_len = len(words) / sentence_count
    return round(198.825 - 40.175 * avg_syll - 2.610 * avg_len, 1)


def find_issues(prose: str, sentences: list[str], register: str) -> list[dict[str, str]]:
    """Metin üzerindeki biçem, AI kalıbı ve TDK bulgularını toplar."""
    findings: list[dict[str, str]] = []

    def add(kind: str, msg: str, match: str) -> None:
        findings.append({"tur": kind, "mesaj": msg, "ornek": match.strip()})

    for pat, msg in TIER1_CLICHES:
        for m in re.finditer(pat, prose, flags=re.IGNORECASE):
            add("AI-Tier1", msg, m.group(0))

    for pat, msg in TIER2_PATTERNS:
        for m in re.finditer(pat, prose, flags=re.IGNORECASE | re.MULTILINE):
            add("AI-Tier2", msg, m.group(0))

    lower_prose = tr_lower(prose)
    for pat, msg in TDK_TYPOS:
        for m in re.finditer(pat, lower_prose):
            add("TDK", msg, prose[m.start():m.end()])

    for m in re.finditer(r"—", prose):
        add("Üslup", "Uzun tire (—) yerine virgül, ayraç veya kısa cümle kullan", "—")
        break

    for m in re.finditer(r"\d+\s*–\s*\d+", prose):
        add("TDK", "Sayı aralığında en-dash (–) değil kısa çizgi (-) kullan", m.group(0))

    for m in re.finditer(r"\b\w+,\s+(?:ve|veya|yahut)\b|\b(?:ve|veya|yahut),\s+\w+", prose, flags=re.IGNORECASE):
        add("TDK", "'ve / veya / yahut' önünde veya arkasında virgül konmaz", m.group(0))

    for m in re.finditer(r";\s*(?:ancak|fakat|lakin|dolayısıyla|öte yandan|bununla birlikte)\b", prose, flags=re.IGNORECASE):
        add("Üslup", "Noktalı virgül + geçiş köprüsü yerine iki ayrı cümle kur", m.group(0))

    for m in re.finditer(r"(?:\?\.\.\.|!\.\.\.)", prose):
        add("TDK", "Soru/ünlemden sonra üç nokta değil iki nokta (?.. veya !..) konur", m.group(0))

    for m in re.finditer(r"\b\d+\.'[ıiuü]nc[ıiuü]\b", prose, flags=re.IGNORECASE):
        add("TDK", "Sıra sayısında nokta ve ek birlikte konmaz (5. veya 5'inci yazılır)", m.group(0))

    for m in re.finditer(r"%\s+\d+|%\d+\.\d+", prose):
        add("TDK", "Yüzde işareti boşluksuz ve ondalık virgülle (%12,5) yazılır", m.group(0))

    for m in re.finditer(r"\b\d{1,3}(?:,\d{3})+\.\d+\b", prose):
        add("TDK", "Türkçede binlik ayırıcı nokta, kesir ayırıcı virgüldür (1.250,50)", m.group(0))

    for m in re.finditer(r"\b(?:hata|gecikme|arıza|sorun|çökme|zarar|kesinti)\w*\s+sayesinde\b", prose, flags=re.IGNORECASE):
        add("Dil-Bilgisi", "'sayesinde' yalnız olumlu sonuçlarda kullanılır -> olumsuzda 'yüzünden / nedeniyle'", m.group(0))

    if register == "resmi":
        for m in re.finditer(r"\bbilgilerinize\s+arz\s+olunur\b", prose, flags=re.IGNORECASE):
            add("Resmî-CK2646", "CK 2646 m. 16(12): 'Bilgilerinize sunulur.' veya makam hiyerarşisine göre 'arz/rica ederim.' kullan", m.group(0))

    duals = (
        ("resen", "re'sen"),
        ("zaman aşımı", "zamanaşımı"),
        ("iyi niyet", "iyiniyet"),
        ("el koyma", "elkoyma"),
    )
    for tdk_form, law_form in duals:
        has_tdk = re.search(rf"\b{re.escape(tdk_form)}\b", prose, flags=re.IGNORECASE)
        has_law = re.search(rf"\b{re.escape(law_form)}\b", prose, flags=re.IGNORECASE)
        if has_tdk and has_law:
            add("Tutarlılık", f"Aynı metinde iki farklı yazım karışmış: '{tdk_form}' (TDK) ile '{law_form}' (kanun) — tek sicilde tutarlı kal", f"{has_tdk.group(0)} / {has_law.group(0)}")

    for m in re.finditer(r"(?<!\d:)\b([01]?\d|2[0-3]):([0-5]\d)\b(?!:\d)", prose):
        add("TDK", f"Saat yazımında iki nokta (:) yerine nokta (.) kullan: {m.group(1)}.{m.group(2)}", m.group(0))

    for m in re.finditer(r"\b([01]?\d|2[0-3])\.([0-5]\d)'(d[ae]n?|t[ae]n?)\b", prose):
        hour, minute, suf = int(m.group(1)), int(m.group(2)), m.group(3).lower()
        expected = _expected_time_suffix(hour, minute, suf.endswith("n"))
        if suf != expected:
            add("TDK", f"Saat eki okunuşuna uymalı: {m.group(1)}.{m.group(2)}'{expected}", m.group(0))

    for m in re.finditer(r"(?m)^#{1,6}\s+[^\n]*?\s(?:Ve|İle|Ya|Veya|Yahut|Da|De|Ki)\s[^\n]*$", prose):
        add("TDK-Başlık", "Türkçe başlıkta bağlaçlar küçük yazılır ('ve, ile, ya, veya, da, ki')", m.group(0))

    for m in re.finditer(r"\([12]\d{3}\)'(?:[ae]|y[ae]|d[ae]n?)", prose):
        add("TDK-Akademik", "Atıfta ek yıla değil yazara eklenir (ör. Yılmaz'a (2024))", m.group(0))

    # Ardışık cümle başı tekrarı
    openers = [tr_lower(re.sub(r"^[\"“'(]+", "", s.split()[0])) for s in sentences if s.split()]
    streak = 1
    for i in range(1, len(openers)):
        if openers[i] == openers[i - 1]:
            streak += 1
            if streak == 3:
                add("Üslup-İpucu", f"3+ ardışık cümle aynı kelimeyle ('{openers[i]}') başlıyor; bilinçli anafora değilse çeşitlendirebilirsin", openers[i])
        else:
            streak = 1

    # Belirgin süs/nadir bağlaç yoğunluğu (kota değil, yalnız tik uyarısı)
    word_count = max(1, len(re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşüâîûÂÎÛ]+", prose)))
    limit_per_500 = max(3, math.ceil(word_count / 500 * 3))
    for conj in CONJUNCTION_WATCH:
        cnt = len(re.findall(rf"\b{re.escape(conj)}\b", lower_prose))
        if cnt > limit_per_500:
            add("Üslup-İpucu", f"'{conj}' bağlacı {cnt} kez yinelenmiş; doğal durmuyorsa başka bir geçiş veya bağlaçsız akış seçilebilir", conj)

    # -mAktAdIr yoğunluğu
    makta_hits = re.findall(r"\b\w+(?:maktadır|mektedir|mıştır|miştir|muştur|müştür|acaktır|ecektir)\b", lower_prose)
    if sentences:
        ratio = len(makta_hits) / len(sentences) * 100.0
        max_allowed = MAKTA_LIMITS[register]
        if ratio > max_allowed:
            add("Üslup", f"-mAktAdIr/-mIştIr oranı %{ratio:.1f}; '{register}' sicili sınırı <= %{max_allowed:.0f}", ", ".join(makta_hits[:3]))

    return findings


def analyze_text(text: str, register: str) -> dict:
    """Tam analiz raporunu sözlük olarak döndürür."""
    prose = strip_non_prose(text)
    words = re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşüâîûÂÎÛ0-9]+", prose)
    sentences = split_sentences(prose)
    lengths = [len(s.split()) for s in sentences]

    cov = None
    if len(lengths) >= 5:
        mean = sum(lengths) / len(lengths)
        var = sum((x - mean) ** 2 for x in lengths) / len(lengths)
        cov = round(math.sqrt(var) / mean, 2) if mean > 0 else 0.0

    findings = find_issues(prose, sentences, register)
    if cov is not None and cov < 0.32:
        findings.append({
            "tur": "Ritim-İpucu",
            "mesaj": f"Cümle boyları tekdüze görünüyor (CoV={cov:.2f}); metin robotik duyuluyorsa uzun-kısa ritmiyle nefes açılabilir",
            "ornek": f"cümle boyları={lengths[:8]}",
        })

    return {
        "sicil": register,
        "kelime_sayisi": len(words),
        "cumle_sayisi": len(sentences),
        "cov": cov,
        "atesman": atesman_score(words, len(sentences)),
        "bulgu_sayisi": len(findings),
        "bulgular": findings,
    }


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Türkçe metin denetleyici (TDK + AI temizliği + ritim).")
    parser.add_argument("dosya", help="Denetlenecek .md/.txt dosya yolu (veya '-' ile stdin)")
    parser.add_argument("--register", default="sohbet", choices=REGISTERS, help="Hedef sicil profili")
    parser.add_argument("--json", action="store_true", help="JSON çıktısı ver")
    args = parser.parse_args()

    if args.dosya == "-":
        # Windows'ta stdin yerel kod sayfasıyla (cp1254/cp857) açılır; Türkçe harfler bozulur.
        raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
    else:
        path = Path(args.dosya)
        if not path.is_file():
            print(f"Hata: Dosya bulunamadı -> {path}", file=sys.stderr)
            return 2
        raw = path.read_text(encoding="utf-8")

    report = analyze_text(raw, args.register)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        cov_str = f"{report['cov']:.2f}" if report["cov"] is not None else "n/a (<5 cümle)"
        ates_str = str(report["atesman"]) if report["atesman"] is not None else "n/a"
        print(f"Sicil: {report['sicil']} | Kelime: {report['kelime_sayisi']} | Cümle: {report['cumle_sayisi']} | CoV: {cov_str} | Ateşman: {ates_str}")
        print(f"Bulgu sayısı: {report['bulgu_sayisi']}")
        for idx, item in enumerate(report["bulgular"], start=1):
            print(f"  {idx}. [{item['tur']}] {item['mesaj']} -> \"{item['ornek']}\"")

    return 1 if report["bulgu_sayisi"] > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
