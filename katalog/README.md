# Tugas 2 PBP

Nama: Najmi Anasya Calyla
NPM: 2106639825
Kelas: PBP C
Link Aplikasi Heroku: https://tugas2-pbp-katalog.herokuapp.com/

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

![](https://raw.githubusercontent.com/najmianasya/Tugas2-PBP/cdb20a587f70a2b6dfd9392cbde9c8e12719d7aa/assets/django_request_response.svg)

Ketika terdapat sebuah request, request tersebut akan masuk ke dalam urls.py yang akan melakukan routing dan mengekstrak argumen dari request tersebut. Kemudian, argumen tersebut akan di-forward dan dipetakan ke views yang sesuai. Views akan mengakses html template yang berada di dalam sub-direktori templates dan mengakses database melalui models.py yang akan memodelkan bentuk data yang disimpan di database. Selanjutnya, data yg diperoleh dari models.py akan digabungkan (merged) dengan html template oleh proses yang terjadi pada views. Dari hasil penggabungan tersebut akan terbentuk sebuah halaman html yang lengkap yang akan dikirim kepada user sebagai response.

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment merupakan sebuah tool yang dapat membantu menjaga project dan dependencies yang diperlukan terpisah dengan membuat lingkungan virtual yang terisolasi. Django memanfaatkan virtual environment untuk membangun dan mengeksekusi sebuah aplikasi. Penggunaan virtual environment dalam pembuatan aplikasi web berbasis Django tidaklah wajib, namun sangat disarankan. Meski kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, adanya virtual environment dapat membantu dalam mengorganisir package dan dependencies untuk setiap project. Dengan demikian, project dapat tetap dijalankan dengan versi yang konsisten pada perangkat yang berbeda-beda.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

### Poin 1
Pada file views.py yang ada pada folder katalog, saya membuat sebuah fungsi bernama show_katalog yang menerima parameter request dan mengembalikan render(request, "katalog.html"). Pada fungsi tersebut, saya juga menambahkan variabel context yang akan menyimpan variabel list_barang, nama, serta npm yang menyimpan data. Kemudian, saya menambahkan context sebagai parameter ketiga pada pengembalian fungsi render pada fungsi show_katalog. Dengan demikian, data yang disimpan pada variabel context akan ikut di-render oleh Django sehingga ndata tersebut dapat terlihat pada halaman HTML.

### Poin 2
Pada file urls.py yang terletak di direktori katalog, saya menambahkan path('', show_katalog, name='show_katalog') pada bagian urlpatterns. Hal tersebut saya lakukan untuk membuat routing terhadap fungsi views sehingga nantinya halaman HTML dapat ditampilkan melalui browser. Di samping itu, saya juga menambahkan path('katalog/', include('katalog.urls')) pada bagian urlpatterns pada file urls.py yang terletak di direktori project_django. Dengan demikian, ketika urls.py mengekstrak argumen 'katalog/', request dapat diteruskan ke views yang sesuai.

### Poin 3
Untuk memetakan data yang didapatkan ke dalam HTML, saya mengganti bagian bertuliskan 'Fill me!' pada file katalog.html dengan nama variabel yang tersimpan pada context di file views.py diawali dan diakhiri dengan kurung kurawal. Sebagai contoh, untuk mengakses variabel nama, maka saya perlu menuliskan {{nama}} pada bagian yang sebelumnya bertuliskan 'Fill me!'. Di samping itu, file views.py juga terhubung dengan models.py, sehingga kita dapat mengakses isi dari variabel list_barang yang tersimpan di database dan menampilkannya pada halaman HTML. 

### Poin 4
Sebelum memulai proses deployment, saya terlebih dahulu membuat sebuah aplikasi baru di Heroku bernama tugas2-pbp-katalog. Kemudian pada GitHub, saya menambahkan 2 repository secret baru, yakni HEROKU_API_KEY dan HEROKU_APP_NAME, pada bagian Settings -> Secrets -> Actions. Selanjutnya, saya menyimpan variabel-variabel tersebut dan menjalankan kembali workflow yang sebelumnya gagal pada tab Actions.