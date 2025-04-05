# Menggunakan image python versi terbaru yang mendukung Django 5.2
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Menyalin requirements.txt ke dalam image
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Menyalin semua file proyek ke dalam container
COPY . /app/

# Menjalankan server Django pada port 8009
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
