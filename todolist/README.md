# Tugas 4 PBP

Nama: Najmi Anasya Calyla

NPM: 2106639825

Kelas: PBP C

Link Aplikasi Heroku: https://tugas2-pbp-katalog.herokuapp.com/todolist/

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
* https://www.educative.io/answers/what-is-a-csrf-token-in-django
* https://docs.djangoproject.com/en/4.0/topics/forms/#rendering-fields-manually
* https://www.geeksforgeeks.org/render-django-form-fields-manually/
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
* https://www.codesnail.com/todo-app-in-django-part-5-create-retrieve-update-and-delete-task-crud-operation-in-django/


---


# Tugas 5 PBP

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
* Pada inline style, kode CSS diletakkan di dalam tag dari elemen-elemen HTML menggunakan atribut `style`, contohnya `<body style="background-color: blue;">`.
Kelebihan: berguna ketika ingin melakukan perubahan dengan cepat dan mengujicoba style tertentu pada suatu elemen.
Kekurangan: cenderung kurang efektif jika harus menerapkan style yang sama ke beberapa elemen berbeda, membuat file HTML terlihat penuh dan kurang rapi.
* Pada internal style, kode CSS diletakkan di bagian `<head>` dari file HTML dalam tag `<style></style>`.
Kelebihan: dapat menerapkan style tertentu secara khusus untuk suatu halaman HTML sehingga tidak bercampur dengan style untuk halaman HTML lainnya.
Kekurangan: menambahkan kode CSS ke dalam file HTML berpotensi memperbesar ukuran memori file dan memperlambat loading time.
* Pada external style, kode CSS diletakkan di file khusus (.css) dan dapat dihubungkan dengan file HTML dengan cara mencantumkan link atau path dari file .css tersebut pada atribut `href` dalam tag `<link/>` dan meletakkannya pada bagian `<head>` dari file HTML.
Kelebihan: dapat digunakan untuk beberapa halaman HTML secara bersamaan, membuat struktur file HTML menjadi lebih rapi.
Kekurangan: jika terdapat perubahan, maka halaman HTML berpotensi untuk tidak di-render dengan benar hingga file CSS di-save dan di-load ke dalam file HTML dengan benar.

## Jelaskan tag HTML5 yang kamu ketahui.
Di luar dari tag HTML dasar seperti `<title>`, `<body>`, `<p>`, dan `<div>` yang tersedia pada HTML, beberapa tag baru pada HTML5 yang saya ketahui adalah:
* Tag `<article>`, yang digunakan untuk mendefinisikan konten yang bersifat independen terhadap konten lainnya pada dokumen atau halaman HTML
* tag `<aside>`, yang digunakan untuk mendefinisikan elemen pelengkap dari artikel utama pada dokumen atau halaman HTML, contohnya sidebar
* Tag `<footer>`, yang digunakan untuk mendefinisikan footer dari dokumen atau halaman HTML
* Tag `<header>`, yang digunakan untuk mendefinisikan title dan heading dari dokumen atau halaman HTML
* Tag `<nav>`, yang digunakan untuk mendefinisikan section navigasi dari dokumen atau halaman HTML yang dapat membantu user dalam menavigasi halaman web
* Tag `<section>`, yang digunakan untuk membagi konten yang ada pada dokumen atau halaman HTML ke beberapa bagian

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
* Universal selector (`*`) digunakan untuk men-select semua elemen yang ada di dalam file.
* Element selector (`elementname`) digunakan untuk men-select semua elemen dengan tipe tertentu, contohnya `h1` akan men-select semua elemen `h1` yang ada di dalam file.
* Class selector (`.classname`) digunakan untuk men-select semua elemen dengan atribut class tertentu, contohnya `.login` akan men-select semua elemen dengan atribut `class="login"`.
* ID Selector (`#idname`) digunakan untuk men-select elemen dengan atribut id tersebut, contohnya `#one` akan men-select elemen dengan atribut `id="one"`.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
* Pertama, saya memasukkan link stylesheet CSS Bootstrap serta path dari file CSS yang saya kustomisasi ke dalam file `base.html`.
* Kemudian, saya melakukan styling pada berbagai elemen dari halaman-halaman HTML yang ada di tugas 4, seperti halaman login, registrasi, halaman to-do list, serta halaman form untuk membuat task baru. Hal tersebut saya lakukan dengan memanfaatkan Bootstrap dan mengatur file CSS agar halaman HTML dapat terlihat seperti yang saya harapkan.
* Untuk membuat halaman-halaman tersebut responsif, saya memanfaatkan breakpoints pada Bootstrap yang mengimplementasikan media queries CSS. Breakpoints yang saat ini tersedia pada Bootstrap adalah `sm` (small), `md` (medium), `lg` (large), `xl`(extra large), serta `xxl` (extra extra large). Breakpoints dapat diimplementasikan dengan komponen lain dari Bootstrap, antara lain `grid` dan `spacing`.

## References
* https://www.hostinger.com/tutorials/difference-between-inline-external-and-internal-css
* https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors
* https://www.geeksforgeeks.org/html5-new-tags/