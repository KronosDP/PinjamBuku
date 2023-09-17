# Tugas 2
1. 
- Pertama, saya mengaktifkan _virtual environment_ dengan cara melakukan `python -m venv env`. Setelah itu saya menyiapkan sebuah berkas `requirements.txt` dan menambahkan _dependancies_ yang saya perlukan untuk project ini. Kemudian pada _virtual environment_, saya menjalankan perintah `pip install -r requirements` untuk menginstall _dependencies_ tersebut. Lalu, saya membuat project django baru bernama `PinjamBuku`. Tidak lupa, saya juga mengubah `ALLOWED_HOST` pada `settings.py` supaya menjadi `*` untuk mengizinkan akses dari semua `host`.
- Setelah itu, saya membuat aplikasi `main` pada proyek ini dan kemudian aplikasi tersebut ditambakan ke `settings.py` pada proyek saya. Kemudian, pada `main` saya melakukan konfigurasi routing URL aplikasi main. Hal ini dilakukan dengan cara mengedit `urls.py`. Hal ini dilakukan agar kita dapat melakukan `.../main` untuk pergi ke aplikasi ini. Tidak lupa, saya juka mengedit `urls.py` pada tingkat proyek untuk mengecek jika ada substring yang bisa diarahkan ke aplikasi kita. Dengan begitu, dapat dilakukan routing ketika kita menambahkan string pada pencarian.
- Setelah itu, dibuat model (kumpulan data) yang terdiri dari 3 atribut yaitu _name, amount,_ dan _description_. Kemudian, dibuatlah `views.py` yang merupakan sebuah fungsi yang mengambil _web request_ dan mengembalikan _web response_. Dalam kasus ini, yang dikembalikan adalah `main.html`. Perhatikan juga bahwa pada `urls.py` digunakan untuk memetakan `views.py`.
2. ![Berikut adalah gambarnya](AssetReadme/Bagan_tugas2.png)
3. Kita menggunakan _virtual environment_ untuk mempermudah urusan _dependencies_ pada proyek kita. Selain itu, kita juga melakukan _environment_ yang terisolasi yang membuat kita lebih aman untuk mengembangkan proyek kita. _Virtual environment_ sebenarnya bisa saja tidak digunakan ketika kita ingin membuat sebuah proyek django, tetapi, _dependency_ yang kita lakukan bisa saja bertabrakan. Oleh karena itu, sebaiknya kita menggunakan _virtual environment_
4. 
- MVC (model-view-controller):
* Model: Logika dan data
* View: Tampilan aplikasi
* Controller: Request, manipulasi data, dan mengatur tampilan view
- MVT (model-view-template):
* Model: Logika dan data
* View: Tampilan aplikasi
* Template: Memisahkan logika tampilan dari kode Python (Perhatikan bahwa kita menggunakan html disini)
- MVVM (Model-View-ViewModel):
* Model: Logika dan data
* View: Tampilan aplikasi
* ViewModel: Konversi data dari model ke format yang diinginkan pada view

Perbedaan terletak pada controller, template, dan ViewModel. MVC fokus pada kontrol aliran aplikasi, MVT menggunakan template, dan MVVM menggunakan ViewModel sebagai perantara view dan model.

# Tugas 3
1. `POST` digunakan untuk mengirim data ((_file, form data,_ dsb) kepada server. Jika berhasil, akan dikembalikan HTTP _status code_ 201. Pada lain sisi, `GET` digunakan untuk mendapatkan (membaca) data. Jika berhasil, akan dikembalikan HTTP _status code_ 200 (OK).
2. `HTML` adalah _markup language_ untuk dokumen yang didesain agar dapat muncul pada _web browser_. Pada lain sisi, terdapat `JSON` dan `XML` yang secara umum digunakan untuk penyimpanan dan pertukaran data. Hal yang membedakannya adalah `XML` menggunakan _XML DOM_ untuk melakukan _looping_ pada keseluruhan dokumen kemudian _value_ diambil dan disimpan pada variabel. Sedangkan `JSON` mengambil _JSON string_ yang perlu di-_parse_.
3. Sederhananya, `JSON` lebih mudah di-_parsing_ daripada `XML`. Untuk contoh kasarnya, perhatikan saja contoh `JSOn` dan `XML`, terlihat bahwa `JSON` lebih pendek.
4. Membuat `forms.py` dan menambahkan beberapa fungsi pada `views.py` untuk dapat mengirimkan data dan mendapatkan data. Pada dasarnya, kita membuat `forms.py` untuk menyimpan data ke _form_. Disana, terdapat beberapa hal yang disimpan dalam form, yaitu _name, amount,_ dan _description_. Setelah itu, dibuatlah fungsi `create_book` pada `views.py` yang salah satunya `create_book.html`. Fungsi ini digunakan untuk pergi ke `create_book.html` jika tombol `Add New Book` ditekan yang akan mengaktifkan fungsi `create_book`. Perhatikan juga bahwa dilakukan validasi terhadap form dan _redirect_ setelah data form berhasil disimpan. Kemudian, kita akan membuat fungsi show xml dan json, kemudian show xml dan json by id. Keempat fungsi ini kita buat pada `views.py` dan melakukan return data spesifik yang ingin kita return, entah itu `all` maupun berdasarkan `id`. Tidak lupa, kita menambahkan kode pada `urls.py` untuk dapat melihat hal-hal yang kita ingin lihat jika kita memasukkan url tersebut.
5. Gambar:
![Gambar view html](AssetReadme/html_tugas3.png)
![Gambar view JSON](AssetReadme/json_tugas3.png)
![Gambar view XML](AssetReadme/xml_tugas3.png)
![Gambar view JSON by id](AssetReadme/jsonbyid_tugas3.png)
![Gambar view XML by id](AssetReadme/xmlbyid_tugas3.png)