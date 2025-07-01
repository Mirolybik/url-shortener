URL Shortener Service 🧾

A lightweight URL shortening microservice built with FastAPI , Redis , and Docker .

---

📌 Description
This service allows you to:

Convert long URLs into unique short keys (e.g., https://example.com → http://localhost:8000/abc123).
Redirect users via short URLs.
Delete short URLs.
Automatically expire short URLs after a configurable TTL (Time-to-Live).
All data is stored in Redis for high performance and low latency.

--- 

🛠️ Installation & Setup

1. Clone the Repository
```bash
git clone https://github.com/your-username/url-shortener.git   
cd url-shortener
```
2. Create .env File
```bash
cp .env.example .env
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run with Docker Compose
```bash
docker-compose up -d
```

---

🌐 API Usage

Shorten a URL

Request:
```bash
curl -X POST "http://localhost:8000/shorten" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://github.com/Mirolybik?tab=repositories"}'
```

Redirect to Original URL
```bash
curl -I "http://localhost:8000/abc123"
```

Delete a Short URL
```bash
curl -X DELETE "http://localhost:8000/abc123"
```

---

🧪 Testing

Run unit tests with:
```bash
pytest tests/
```