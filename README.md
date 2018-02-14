# premanclaymore
[Jaring Preman - Nodevfee]

Bukan tidak ikhlas, tapi....

Pool : (tested nanopool)
nanopool.org dwarfpool.com ethpool.org ethermine.org

Claymore : (tested 10.5 10.6)
Semua versi, disarankan versi terbaru

Koin : (tested ETH ETC)
Apapun, yang penting pakai claymore

Langkahnya :
1. Install Phyton 2.7.1 https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi
2. Buat ip statis sesuai konfigurasi internet yg digunakan (untuk check bisa di cmd ipconfig/all)
3. Tambah ip baru di advance -> Ip setting -> Add : IP Address : 194.12.12.2 Subnet mask : 255.255.255.255 (SS terlampir)

Untuk memastingan sudah benar, bisa di ping melalui cmd ke ip 194.12.12.2 jika reply time nya 1ms berarti sudah benar

4. buat file nodev.bat --- stratum_proxy.py 0.0.0.0 8008 [alamat pool] (spasi) [port] (spasi) [alamat wallet]
contoh : stratum_proxy.py 0.0.0.0 8008 eth-asia1.nanopool.org 9999 0x39d27d66c14f7372553b1ba59833c6ba8981a76a
5. jalankan file nodev.bat
7. edit alamat yg di bat claymore menjadi 194.12.12.2:8008
8. jalankan bat claymore nya

*note
donlot dulu preman.zip (anggirahman.com/preman.zip)
1 Gateway hanya bisa pakai 1 jaring
jika berjalan baik, DevFee akan terdeteksi oleh jaring sebagai "PREMAN", jika di pool sudah ada worker "rba" berarti sudah berhasil.

[tidak perlu donasi]

Semoga berhasil menjaring preman.
