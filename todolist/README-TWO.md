# Tugas 6 PBP

Nama: Najmi Anasya Calyla

NPM: 2106639825

Kelas: PBP C

Link Aplikasi Heroku: https://tugas2-pbp-katalog.herokuapp.com/todolist/

##  Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronus programming merupakan teknik pemrograman yang memungkinkan pengguna untuk tetap berinteraksi dengan halaman web saat menunggu response dari user. Pada asynchronus programming, ketika suatu operasi sedang berjalan, maka operasi lain pun dapat tetap berjalan dan tidak perlu menunggu hingga suatu operasi tersebut selesai berjalan. 

Synchronus programming merupakan teknik pemrograman yang hanya memungkinkan satu operasi untuk berjalan dalam suatu waktu. Synchronus programming mengikuti urutan click, wait, refresh sehingga interaksi user dengan halaman web hanya dapat dilakukan setelah halaman web berhasil di load.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming merupakan paradigma pemrograman di mana flow dari program akan ditentukan oleh events. Events dapat di-trigger salah satunya oleh interaksi user dengan halaman web, contohnya ketika user menklik sebuah button atau menekan suatu key. Salah satu contoh penerapan Event-Driven Programming pada tugas ini adalah pada bagian `document.getElementById("add-todo").onclick = addTodolist;` di mana ketika user menklik button dengan id `add-todo` yang terletak pada modal, fungsi `addTodolist()` akan dijalankan secara asinkronus dan sebuah card yang berisi task baru akan ditambahkan.

## Jelaskan penerapan asynchronous programming pada AJAX.
AJAX (Asynchronous JavaScript and XML) merupakan salah satu teknik penggunaan JavaScript yang memungkinkan halaman web untuk memperbarui data secara asinkronus dengan mengirimkan data ke server di balik layar, sehingga perbaruan sebagian elemen data dapat dilakukan oleh browser tanpa me-reload keseluruhan halaman. Ketika terjadi sebuah event pada halaman web, maka JavaScript akan membuat sebuah `XMLHttpRequest` object yang akan mengirimkan request ke server. Kemudian, server akan memroses request tersebut
dan mengembalikan response kepada halaman web yang akan dibaca oleh JavaScript. Selanjutnya, JavaScript akan men-trigger action sesuai dengan request.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Membuat fungsi baru bernama `show_todolist_json` pada file `views.py` yang mengembalikan seluruh data task dalam bentuk JSON.
* Mengimport fungsi `show_todolist_json` dan menambahkan path `/json` pada file `urls.py` di direktori `todolist`.
* Membuat fungsi untuk melakukan pengambilan task menggunakan `AJAX GET` pada bagian `<script></script>` dari file `todolist.html`.
* Membuat modal menggunakan Bootstrap dan menyesuaikan isinya dengan isian form di file `forms.py`.
* Membuat fungsi baru bernama `add_task` pada file `views.py` untuk menambahkan task baru ke dalam database.
* Mengimport fungsi `add_task` dan menambahkan path `/add` pada file `urls.py` di direktori `todolist`.
* Membuat fungsi untuk menghubungkan form dengan path menggunakan `AJAX POST` pada bagian `<script></script>` dari file `todolist.html`. Ketika user menklik button `Tambah Task Baru` pada modal, maka card yang berisi task baru akan dibuat.

## References
* https://studybay.com/blog/event-driven-development-features/
* https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-5#pengenalan-ajax