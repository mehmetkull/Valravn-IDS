# Faz 1 - CIC-IDS-2017 ile Temel Random Forest Yaklaşımı

## Amaç

Projenin ilk fazında, ağ akışlarını **normal** ve **saldırı** olarak ayırabilen güçlü ve yorumlanabilir bir temel model oluşturulmuştur. Bu aşamada tek veri kaynağı üzerinde veri kalitesi, özellik seçimi, model kararlılığı ve hiperparametre optimizasyonu incelenmiştir.

Faz 1, nihai canlı sistem değildir. Sonraki fazlarda kullanılan Random Forest ilk karar katmanının ve değerlendirme yönteminin bilimsel temelini oluşturur.

## Veri Kaynağı

Çalışmada CIC-IDS-2017 veri kümesi kullanılmıştır. Veri kümesi; normal kullanıcı davranışlarıyla birlikte DoS, DDoS, PortScan, Bot, Brute Force ve web saldırıları gibi farklı saldırı türlerine ait etiketli ağ akışları içerir.

İlk veri hazırlama sürecinde:

- Yaklaşık 2,83 milyon ham akış kaydı birleştirilmiştir.
- Eksik, sonsuz ve yinelenen değerler denetlenmiştir.
- Çok sınıflı saldırı adları ikili sınıflandırma için `normal=0`, `saldırı=1` biçimine dönüştürülmüştür.
- Temizleme sonrasında yaklaşık 2,52 milyon kayıt değerlendirmeye alınmıştır.
- Eğitim ve test ayrımında sınıf oranları korunmuştur.

Veri kümesi bu public repoda dağıtılmamaktadır. Resmî veri kaynağının lisans ve kullanım koşulları geçerlidir.

## Ön İşleme Adımları

1. Günlük CSV dosyalarının ortak tabloda birleştirilmesi
2. Eksik ve sonsuz değerlerin temizlenmesi
3. Yinelenen kayıtların denetlenmesi
4. Saldırı etiketlerinin ikili sınıfa dönüştürülmesi
5. Düşük varyanslı özelliklerin belirlenmesi
6. Yüksek korelasyonlu özellik gruplarının incelenmesi
7. Model için nihai özellik kümesinin seçilmesi
8. Eğitim ve test kümelerinin ayrılması

Özellik azaltmanın amacı yalnızca model boyutunu küçültmek değildir. Aynı bilgiyi tekrar eden veya ayırt edici bilgi taşımayan alanların çıkarılması, modelin daha kararlı ve yorumlanabilir olmasını sağlar.

## Neden Random Forest?

Random Forest şu nedenlerle temel model olarak seçilmiştir:

- Tablo biçimindeki ağ akışı özelliklerinde yüksek başarı,
- Doğrusal olmayan ilişkileri öğrenebilme,
- Özellik ölçeklendirmesini zorunlu kılmama,
- Paralel eğitim ve hızlı çıkarım,
- Özellik önemlerini raporlayabilme,
- Gürültülü özelliklere karşı görece dayanıklılık.

Model önce varsayılan ayarlarla değerlendirilmiş, ardından rastgele arama ve daha dar kapsamlı ızgara aramasıyla hiperparametreler incelenmiştir. Yeniden üretilebilirlik için rastgelelik değeri sabitlenmiştir.

## Sonuçlar

Beş katlı çapraz doğrulamada yaklaşık 2,02 milyon eğitim örneği ve 66 özellik kullanılmıştır:

| Ölçüt | Ortalama |
|---|---:|
| F1 | 0,99265 |
| Precision | 0,99649 |
| Recall | 0,98891 |
| Accuracy | 0,99591 |
| ROC-AUC | 0,99985 |

Hiperparametre araştırmaları sonrasında yaklaşık `0,9940` F1-macro ve `%99,67` doğruluk elde edilmiştir. Bu sonuçlar CIC-IDS-2017 içindeki ayrılmış değerlendirme bölümleri için geçerlidir; farklı ağlarda aynı performansı garanti etmez.

Özellik önem analizinde paket boyutu istatistikleri, ileri/geri yön trafik hacmi ve hedef port gibi alanların öne çıktığı görülmüştür. Hedef porta bağımlılık ayrıca incelenmiş ve modelin tek bir özelliğe aşırı bağlanmaması hedeflenmiştir.

## Faz 1'den Çıkarılan Dersler

- Random Forest ağ akışı sınıflandırması için güçlü ve hızlı bir temel sağlamıştır.
- Yüksek test başarısı, farklı ağ kaynaklarında genelleme garantisi değildir.
- Özelliklerin yalnızca adı değil, hangi araçla ve nasıl hesaplandığı da önemlidir.
- Tek veri kaynağına bağımlılığı azaltmak için yeni veri ve model aileleri gereklidir.

Bu bulgular [Faz 2](../phase2/README.md) çalışmalarını başlatmıştır.

