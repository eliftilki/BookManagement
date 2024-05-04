# Stock API Bildirimi

Bu API, stok yönetimi için bir RESTful API sunmaktadır. Aşağıdaki özellikler dahil edilmiştir:

- Stok listesini alma
- Yeni bir stok ekleyebilme
- Mevcut stokları güncelleme
- Tüm stokları silme

## Kullanım

API'yi kullanırken lütfen aşağıdaki konulara dikkat edin:

- Stok eklerken veya güncellerken, her isteğin bir stok öğesi içermesi gerekmektedir. Bu öğe en azından bir adet ve bir miktar içermelidir.
- Tüm stokları güncellerken, tüm mevcut stokların veri yükünü içermelidir. Eksik veya eksik öğeler kabul edilmez.
- Tüm stokları silme işlemi geri alınamaz. Bu işlem sonrasında tüm stoklar veritabanından kalıcı olarak silinir.

.

