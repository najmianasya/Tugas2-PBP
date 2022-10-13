# Tugas 6 PBP

Nama: Najmi Anasya Calyla

NPM: 2106639825

Kelas: PBP C

Link Aplikasi Heroku: https://tugas2-pbp-katalog.herokuapp.com/todolist/

##  Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronus programming merupakan teknik pemrograman yang memungkinkan pengguna untuk tetap berinteraksi dengan halaman website saat menunggu response dari user. Pada asynchronus programming, ketika suatu operasi sedang berjalan, maka operasi lain pun dapat tetap berjalan dan tidak perlu menunggu hingga suatu operasi tersebut selesai beejalan. 

Synchronus programming merupakan teknik pemrograman yang hanya memungkinkan satu operasi untuk berjalan dalam suatu waktu. Synchronus programming mengikuti urutan click, wait, refresh sehingga interaksi user dengan halaman website hanya dapat dilakukan setelah halaman website berhasil di load.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming merupakan paradigma pemrograman di mana flow dari program akan ditentukan oleh events. Events dapat di-trigger salah satunya oleh interaksi user dengan halaman website, contohnya ketika user menklik sebuah button atau menekan suatu key. Salah satu contoh penerapan Event-Driven Programming pada tugas ini adalah pada bagian `document.getElementById("add-todo").onclick = addTodolist;` di mana ketika user menklik button dengan id `add-todo` yang terletak pada modal, fungsi `addTodolist` akan dijalankan dan sebuah card yang berisi task baru akan ditambahkan.

## Jelaskan penerapan asynchronous programming pada AJAX.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.