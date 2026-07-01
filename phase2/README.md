# Faz 2 - Birleşik Veri ve Alternatif Model Aileleri

## Amaç

Faz 2'de Faz 1'in tek veri kaynağı ve tek model yaklaşımı genişletilmiştir. Farklı ağ trafiği kaynakları ortak sınıflandırma şemasında değerlendirilmiş; Random Forest, Autoencoder, LSTM-Autoencoder ve TabNet modelleri karşılaştırılmıştır.

Bu fazın temel araştırma soruları şunlardır:

1. Denetimli Random Forest modeli farklı kaynaklardan gelen veride başarısını koruyabilir mi?
2. Yalnız normal trafik öğrenen Autoencoder bilinmeyen davranışları ayırabilir mi?
3. LSTM-Autoencoder akışlar arasında zamansal örüntü yakalayabilir mi?
4. TabNet, tablo verisinde derin öğrenme alternatifi olarak kullanılabilir mi?
5. Hızlı ve maliyetli modeller kademeli bir karar sisteminde nasıl birleştirilebilir?

## Veri ve Ortak Şema

Ana deneylerde CIC-IDS-2017 ve DAPT2020 tabanlı akış kayıtları ortak ikili sınıflandırma şemasına getirilmiştir. Farklı kaynaklardan gelen alanlar eşleştirilmiş, etiketler `normal` ve `saldırı` biçiminde birleştirilmiş ve model türüne göre farklı veri temsilleri hazırlanmıştır.

| Model | Kullanılan temsil |
|---|---|
| Random Forest | Temizlenmiş ham sayısal özellikler |
| Autoencoder | Normal eğitim verisine uydurulmuş dayanıklı ölçekleme |
| LSTM-Autoencoder | Ölçeklenmiş veriden oluşturulan sabit uzunluklu pencereler |
| TabNet | Eğitim verisine uydurulmuş quantile dönüşümü |

Ölçekleyici ve dönüşümlerin yalnızca eğitim bölümünde öğrenilmesi veri sızıntısını önleyen temel ilkedir.

## Random Forest Sonucu

Faz 2 Random Forest modeli, birleşik veri üzerinde güçlü denetimli temel sağlamıştır:

| Ölçüt | Test sonucu |
|---|---:|
| Accuracy | 0,99061 |
| Precision | 0,97770 |
| Recall | 0,97531 |
| F1 | 0,97650 |
| PR-AUC | 0,99807 |

Karışıklık matrisi `TN=63.644`, `FP=356`, `FN=395`, `TP=15.605` olarak kaydedilmiştir.

## Autoencoder Sonucu

Autoencoder yalnız normal trafik üzerinde rekonstrüksiyon öğrenmiş ve yüksek rekonstrüksiyon hatasını anomali olarak değerlendirmiştir. Farklı gizli temsil boyutları karşılaştırılmıştır.

Seçilen deney sonucu:

| Ölçüt | Değer |
|---|---:|
| ROC-AUC | 0,84036 |
| Precision | 0,45659 |
| Recall | 0,67219 |
| F1 | 0,54380 |

Bu sonuç, rekonstrüksiyon hatasının kullanılan veri temsilinde tek başına yeterli karar kalitesi sağlamadığını göstermiştir. Autoencoder nihai canlı karar katmanına alınmamıştır.

## LSTM-Autoencoder Sonucu

LSTM-Autoencoder, 15 adımlı pencerelerde sıralı örüntü öğrenmek amacıyla denenmiştir. Ancak satırların önceden karıştırılmış olması ve akışlar arasında güvenilir kronolojik devamlılık bulunmaması, zaman serisi modelinin anlamlı sıra öğrenmesini sınırlamıştır.

| Ölçüt | Değer |
|---|---:|
| ROC-AUC | 0,52794 |
| Precision | 0,97406 |
| Recall | 0,21121 |
| F1 | 0,34715 |

Yüksek precision değerine rağmen düşük recall, saldırıların büyük bölümünün kaçırıldığını göstermektedir. Sonuç, zaman serisi modelinin yalnız mimari olarak eklenmesinin yeterli olmadığını; verinin gerçekten zaman sıralı hazırlanması gerektiğini ortaya koymuştur.

## TabNet Sonucu

TabNet, adım bazlı özellik seçimi yapabilen denetimli tablo modeli olarak değerlendirilmiştir. Dört karar adımı ve 23 özellikli dönüştürülmüş veri kullanılmıştır.

| Ölçüt | Test sonucu |
|---|---:|
| ROC-AUC | 0,99929 |
| PR-AUC | 0,99735 |
| Precision | 0,95633 |
| Recall | 0,98813 |
| F1 | 0,97197 |
| FPR | 0,01128 |

TabNet güçlü ayırma performansı sağlamıştır. Bununla birlikte tüm akışlarda çalıştırılması Random Forest'a göre daha yüksek hesaplama maliyeti oluşturur. Bu nedenle TabNet'in yalnız belirsiz örneklerde kullanılması daha uygun bulunmuştur.

## İlk Cascade Deneyleri

Faz 2'de CICFlowMeter, NFStream ve diğer akış çıkarıcılarla erken canlı IDS denemeleri yapılmıştır. Bu çalışmalar önemli bir teknik sorunu göstermiştir:

> Aynı isimli ağ akışı özelliği, farklı araçlarda farklı zaman aşımı, yön ve hesaplama kurallarıyla üretilebilir.

Model bir çıkarıcının özellikleriyle eğitilip farklı bir çıkarıcının özellikleriyle çalıştırıldığında dağılım kayması oluşabilir. Bu durum canlı sistemde yanlış alarm veya saldırı kaçırma riskini artırır.

## Faz 2'den Çıkarılan Dersler

- Denetimli RF ve TabNet modelleri, bu veri düzeninde Autoencoder yaklaşımlarından daha başarılıdır.
- LSTM-AE için gerçek kronolojik süreklilik içeren veri gereklidir.
- Her model ailesi kendi scaler ve özellik sırasıyla birlikte saklanmalıdır.
- Eğitim ile canlı çıkarım aynı akış semantiğini kullanmalıdır.
- TabNet'i tüm trafikte değil, RF'nin belirsiz bölgesinde çalıştırmak daha verimlidir.

Bu sonuçlar [Faz 3](../phase3/README.md) NFStream tabanlı RF–TabNet cascade mimarisini şekillendirmiştir.


