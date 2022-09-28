# Tugas 4 PBP

Nama: Najmi Anasya Calyla

NPM: 2106639825

Kelas: PBP C

Link Aplikasi Heroku: https://tugas2-pbp-katalog.herokuapp.com/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
`{% csrf_token %}` merupakan potongan kode yang berfungsi untuk melindungi website serta pengguna dari serangan Cross Site Request Forgeries (CSRF). CSRF merupakan serangan di mana sebuah form yang telah dimodifikasi di situs lain dikirim kembali kepada pengguna yang telah terautentikasi sehingga dapat menyebabkan eksploitasi data pengguna oleh pihak yang tidak bertanggung jawab. Menggunakan `{% csrf_token %}`, Django dapat membuat suatu token pada server-side dan memastikan bahwa setiap request yang diterima oleh server mengandung token tersebut. Jika request tidak mengandung token tersebut, maka request tidak akan dieksekusi sehingga data pengguna dapat terlindungi. Jika suatu website tidak mengimplementasikan `{% csrf_token %}`, maka website tersebut akan berada dalam risiko yang lebih tinggi untuk mendapat serangan CSRF dari pihak yang tidak bertanggung jawab. 

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa. Generator seperti `{{ form.as_table }}` membantu men-generate HTML code dari Django form yang ada di file `forms.py`. Dengan menggunakan generator, proses rendering dari form berjalan secara otomatis. Meski demikian, kita juga dapat me-render form secara manual, yakni dengan membuat Django form class pada file `forms.py`, membuat fungsi yang sesuai dan instance dari class yang telah dibuat sebelumnya di file `views.py`, serta memasukkan variabel yang ada pada bagian `context` ke file HTML di direktori `templates`. Dengan menggunakan generator, halaman HTML akan ditampilkan secara rapi dan error akan dihandle secara otomatis. Namun ketika membuat form secara manual, kita harus merapikan tampilan halaman HTML dengan mengakses setiap field yang ada sebagai atribut dari form menggunakan `{{ form.nama_field }}` dan menghandle error secara manual. Terkadang, kita perlu membuat form secara manual, salah satunya adalah ketika kita ingin membuat sebuah form dengan tampilan yang dipercantik menggunakan CSS.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika pengguna men-submit data melalui sebuah HTML form, akan terbuat sebuah request ke alamat yang tertera pada atribut `action` pada form. Kemudian, server akan memeriksa kevalidan dari form serta data dari form tersebut. Jika form atau data tidak valid, maka server akan menampilkan error message atau meminta input form kembali hingga form dan data yang dikirim dapat dipastikan valid. Jika form dan data valid, maka data akan disimpan pada database yang dimodelkan pada file `models.py` dan menjalankan actions pada data. Kemudian `urls.py` akan me-redirect pengguna ke URL yang tertera pada atribut `action` pada form tersebut dan mencari views yang sesuai pada `views.py`. Terakhir, server akan men-generate halaman html yang lengkap dan mengirimnya kepada user sebagai response.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Membuat aplikasi baru bernama `todolist` dengan menjalankan perintah `python manage.py startapp`.
* Menambahkan path `todolist/` pada bagian `urlpatterns` dari file `urls.py` di direktori `project_django` dan menambahkan `'todolist'` pada bagian `INSTALLED_APPS` dari file `settings.py`.
* Membuat model data `Task` dengan atribut `user`, `date`, `title`, dan `description` pada file `models.py`.
* Membuat file `todolist.html` pada direktori `templates` dan fungsi `show_todolist` pada file `views.py` untuk mengimplementasikan halaman utama `todolist`.
* Membuat halaman form untuk pembuatan task pada file `forms.py`, kemudian membuat file `create_task.html` pada direktori `templates` serta fungsi `create_task`pada file `views.py` untuk mengimplementasikan form pembuatan task baru.
* Membuat file-file html pada direktori `templates` dan fungsi-fungsi pada file `views.py` untuk implementasi form registrasi, login, dan logout.
* Mengimport dan menambahkan path url dari fungsi-fungsi yang sudah dibuat sebelumnya pada file `views.py` ke dalam bagian `urlpatterns` pada file `urls.py` agar setiap views dapat diakses dengan url yang sesuai.

## References
https://www.educative.io/answers/what-is-a-csrf-token-in-django
https://docs.djangoproject.com/en/4.0/topics/forms/#rendering-fields-manually
https://www.geeksforgeeks.org/render-django-form-fields-manually/
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
https://www.codesnail.com/todo-app-in-django-part-5-create-retrieve-update-and-delete-task-crud-operation-in-django/