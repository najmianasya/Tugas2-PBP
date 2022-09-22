# Tugas 3 PBP

Nama: Najmi Anasya Calyla

NPM: 2106639825

Kelas: PBP C

Link Aplikasi Heroku: https://tugas2-pbp-katalog.herokuapp.com/

## Jelaskan perbedaan antara JSON, XML, dan HTML!
* JavaScript Object Notation (JSON) merupakan format data delivery berbentuk text yang sintaksnya merupakan turunan dari object JavaScript. Data pada JSON disimpan dalam bentuk key dan value. Data dari JSON dapat dikirim dan diterima menggunakan AJAX, diimplementasikan menggunakan jQuery, dan dijalankan di atas layer protocol HTTP/HTTPS.
* Extensive Markup Language (XML) merupakan format data delivery yang memiliki struktur seperti tree yang dimulai dari root, lalu branch, hingga berakhir pada leaves. Setiap elemen pada dokumen XML harus memiliki closing tag yang bersifat case sensitive. Data dari XML dapat dikirim dan diterima menggunakan WebSocket, diimplementasikan menggunakan jQuery dan Socket.js, serta dijalankan di atas layer protocol HTTP/HTTPS.
* HyperText Markup Language (HTML) merupakan markup language yang digunakan untuk membuat halaman website dan aplikasi web. File HTML digunakan untuk mendeskripsikan struktur dari sebuah halaman website yang akan ditampilkan pada browser. Konten dari elemen-elemen pada file HTML dibuka dan ditutup oleh tags.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Ketika mengembangkan suatu platform, terkadang pengembang perlu mengirimkan data dari suatu stack ke stack lain. Dengan adanya data delivery dalam format HTML, XML, dan JSON, data akan lebih mudah untuk dikirim dan diterima dari suatu perangkat ke perangkat lain atau dari suatu platform ke platform lain.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Membuat aplikasi baru bernama mywatchlist dengan menjalankan perintah code(python manage.py startapp).
* Menambahkan path mywatchlist pada bagian urlpatterns dari file urls.py di direktori project_django dan menambahkan 'mywatchlist' pada bagian INSTALLED_APPS dari file settings.py.
* Membuat model data berupa atribut watched, title, rating, release_date, serta review dalam Class Mywatchlist pada file models.py.
* Menambahkan data untuk MyWatchList pada file initial_watchlist_data.json di folder fixtures dan melakukan migrasi dengan menjalankan perintah code(python manage.py makemigrations) dan code(python manage.py migrate).
* Membuat fungsi show_wishlist (halaman utama), show_html (penyajian data dalam bentuk HTML), show_xml (penyajian data dalam bentuk XML), serta show_json (penyajian data dalam bentuk JSON) pada file views.py dan mengimpor fungsi-fungsi tersebut ke dalam file urls.py yang ada pada direktori mywatchlist.
* Menambahkan path url ke dalam urlpatterns untuk mengakses ketiga fungsi yang sudah diimpor tadi.

## Mengakses ketiga URL menggunakan Postman

### HTML
![](https://raw.githubusercontent.com/najmianasya/Tugas2-PBP/main/assets/postman_html.png)

### XML
![](https://raw.githubusercontent.com/najmianasya/Tugas2-PBP/main/assets/postman_xml.png)

### JSON
![](https://raw.githubusercontent.com/najmianasya/Tugas2-PBP/main/assets/postman_json.png)
