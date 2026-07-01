# Veri, Etiketleme ve Egitim

## Kaynaklar

Calismada CIC-IDS-2017 ve DAPT2020 ag trafik kayitlari kullanilmistir. Public depo bu veri kumelerini veya bunlardan uretilen akis tablolarini dagitmaz; veri lisanslari ve resmi dagitim kosullari kaynak saglayicilara aittir.

## NFStream'e gecis

Ilk deneylerde tablo tabanli akis ozellikleri kullanilmistir. Canli sistemde ayni ozellik anlamini yeniden uretebilmek icin ham PCAP dosyalari NFStream ile tekrar islenmis, egitim ve cikarim ortak `15/30` saniyelik profil ve 27 ozellik semasinda birlestirilmistir.

## Zaman duyarlı etiketleme

Bir NFStream akisi; adresler, portlar ve protokol bilgisiyle aday resmi kayitlara eslestirilir. Adaylar arasinda zaman araligi cakisan veya zamansal olarak en uyumlu olan kayit kullanilir. Boylece yalnizca ayni adres/port kombinasyonunun gunun farkli saatlerinde gorulmesi, yanlis etiket aktarimi icin yeterli sayilmaz.

## Egitim ayrimi

Egitim, kalibrasyon ve final test bolumleri ayri tutulmustur. Olceklendirici yalnizca egitim bolumunde uydurulmustur. RF 150 agac, azami derinlik 20 ve `log2` ozellik secimiyle; TabNet 5 karar adimi, 64 karar/attention boyutu ve `entmax` maskeleme ile egitilmistir. Rastgelelik uretilebilirlik icin `random_state/seed=42` ile sabitlenmistir.

Model secimi yalnizca tek bir dogruluk degerine degil; precision, recall, F1, yanlis pozitif orani, kaynak bazli davranis ve esik taramasina dayanir.
