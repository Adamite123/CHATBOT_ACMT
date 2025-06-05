# Welcome to AIS 👋
![Version](https://img.shields.io/badge/version-0.1-blue.svg?cacheSeconds=2592000)

> CHATBOT ACMT by PBO

## Author

👤 **COP TEAM**


# How to Run This Django Project

Follow these steps to set up and run the Django project:

## Prerequisites

- Python installed (version 3.x recommended)
- `pip` package manager (Jangan lupa centang pip waktu install python)
- Postgre installed

## Steps to Run

1. **Clone the Repository**  
   Clone the project repository to your local machine:

```bash
git clone <repository-url>
cd ICONIST
```

2. **Install Dependencies**  
   Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. **Buat Database di Postgre**  
   Nama database dan password database bebas jangan lupa bagian .env bisa disesuaikan.
   
   Penting!! jangan lupa tambahkan password saat install postgre


4. **Apply Migrations**  (Fungsinya untuk import Table didalam database)
   Run database migrations:

```bash
python manage.py migrate
```

5. **Run the Development Server**  
   Start the Django development server:

```bash
python manage.py runserver
```

```bash
python manage.py tailwind start (Jika tidak bisa, masuk folder static_src lalu run command ini)
```

6. **Access the Application**  
   Open your browser and navigate to:

```
http://127.0.0.1:8000/
```

## Additional Notes

- Jangan lupa `.env` file variable harus diseuaikan dengan settingan database postgre


# How to setting github on vscodes to use own branch
Setiap orang harus development di branch masing-masing. Dilarang asal merger ke master. Untuk dilakukan merger harus dilakukan komunikasi terlebih dahulu.

1. **Buat branch**
```
Membuat branch baru(berdasarkan nama) di https://github.com/Adamite123/CHATBOT_ACMT/branches (klik button new branch)
```

2. **Melihat Branch aktif**
Cek terhubung ke branch mana
```
git branch -a
```

3. **Masuk ke branch dari VSCodes**
Tentukan branch mana yang anda masuki
```
git checkout nama_branch
```

4. **Merge dari master**
Branch pertama kali dibuat pasti kosong oleh karena itu perlu di merge atau mengambil file dari repo master
```
git merge master
```

5. **Cek Log Branch**
Setiap perubahan akan tercatat di Log aktif(Log yang anda masuki), setiap dilakukan commit harus cek log untuk dipastikan perubahan tersimpan.