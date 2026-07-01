# Degerlendirme ve Sinirlar

## Etiketli final test

389.963 akislik final testte cascade sonucu:

| TN | FP | FN | TP |
|---:|---:|---:|---:|
| 301.370 | 1.403 | 9.644 | 77.546 |

| Precision | Recall | F1 | FPR |
|---:|---:|---:|---:|
| 0.9822 | 0.8894 | 0.9335 | 0.00463 |

Bu metrikler veri ayrimindaki etiketlere gore hesaplanmistir. Farkli bir kurum aginda ayni performansin garanti edildigi anlamina gelmez.

## Kontrollu canli testler

Sistem izole VMware aginda Kali Linux kaynakli Nmap port taramasi ve kontrollu DoS trafigiyle gozlemlenmistir. Canli senaryolar karar yolunu, sayaclari, zaman grafikleri ve XAI ekranini gosteren vaka calismalaridir. Paket/akis duzeyinde bagimsiz kesin etiket olmadigi icin bu kayitlardan precision veya recall uretilmemistir.

## Sinirlar

- Sifreli uygulama icerigi incelenmez; karar akis istatistiklerine dayanir.
- Model egitim dagiliminin disindaki aglarda dagilim kaymasi gorulebilir.
- Cok kisa akislar bilerek yetersiz veri sinifina ayrilir.
- Yogunluk esikleri ag kapasitesine gore yeniden kalibre edilmelidir.
- Prototip, imza tabanli bir IDS'in tum kural kapsamini saglamaz.

Gelecek calismalarda daha zengin sentetik trafik, farkli aglardan dis dogrulama ve imza tabanli motorlarla yapay zeka kararlarinin birlestirilmesi degerlendirilebilir.
