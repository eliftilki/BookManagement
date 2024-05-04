# Kullanacağımız temel imajı belirleme (Python temel imajı)
FROM python:3.9-slim

# Uygulamanın çalışması için gerekli olan dosyaları kopyalama
COPY . /app
WORKDIR /app

# Uygulamanın gereksinimlerini yükleyin
RUN pip install --no-cache-dir flask flask_swagger_ui flask_cors

# Uygulamayı çalıştırma
CMD ["python", "api_client.py"]

