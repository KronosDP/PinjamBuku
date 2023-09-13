1. 
- Pertama, saya mengaktifkan _virtual environment_ dengan cara melakukan `python -m venv env`. Setelah itu saya menyiapkan sebuah berkas `requirements.txt` dan menambahkan _dependancies_ yang saya perlukan untuk project ini. Kemudian pada _virtual environment_, saya menjalankan perintah `pip install -r requirements` untuk menginstall _dependencies_ tersebut. Lalu, saya membuat project django baru bernama `PinjamBuku`. Tidak lupa, saya juga mengubah `ALLOWED_HOST` pada `settings.py` supaya menjadi `*` untuk mengizinkan akses dari semua `host`.
- Setelah itu, saya membuat aplikasi `main` pada proyek ini dan kemudian aplikasi tersebut ditambakan ke `settings.py` pada proyek saya. Kemudian, pada `main` saya melakukan konfigurasi routing URL aplikasi main. Hal ini dilakukan dengan cara mengedit `urls.py`. Hal ini dilakukan agar kita dapat melakukan `.../main` untuk pergi ke aplikasi ini. Tidak lupa, saya juka mengedit `urls.py` pada tingkat proyek untuk mengecek jika ada substring yang bisa diarahkan ke aplikasi kita. Dengan begitu, dapat dilakukan routing ketika kita menambahkan string pada pencarian.
- Setelah itu, dibuat model (kumpulan data) yang terdiri dari 3 atribut yaitu _name, amount,_ dan _description_. Kemudian, dibuatlah `views.py` yang merupakan sebuah fungsi yang mengambil _web request_ dan mengembalikan _web response_. Dalam kasus ini, yang dikembalikan adalah `main.html`. Perhatikan juga bahwa pada `urls.py` digunakan untuk memetakan `views.py`.
2. ![Berikut adalah gambarnya](Bagan_tugas2.png)
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