1️⃣ PRODUCTION-GRADE TEKNİK MİMARİ

Amaç:

Platform bağımsız

Veri odaklı

API-first

Düşük maliyetli ama ölçeklenebilir

🔷 YÜKSEK SEVİYE MİMARİ
Client (Web / Bot / API Consumer)
        │
        ▼
API Gateway
        │
        ▼
Application Layer (FastAPI)
        │
 ┌───────────────┬────────────────┬────────────────┐
 ▼               ▼                ▼                ▼
GeoEngine    RankingEngine     NLPParser       ExplanationEngine
                │                │                │
                └──────►  Data Layer  ◄──────────┘
                             │
                    PostgreSQL + PostGIS
                             │
                           Redis
                             │
                      Analytics / Logs
🔹 1. Client Layer

Web App (Next.js)

Telegram Bot

Public REST API

Mobil app ile başlama. Web + bot yeterli.

🔹 2. API Gateway

Amaç:

Rate limiting

Auth

Abuse protection

Başlangıçta:

Cloudflare free

Basit JWT auth

🔹 3. Application Layer

Stack:

Python

FastAPI

Uvicorn

Bu katman sadece orkestrasyon yapar.
İş mantığı modüllerde.

🔥 CORE SERVİSLER
🔷 GeoEngine

Sorumluluk:

Mesafe hesaplama

Bounding box

Geo clustering

Teknoloji:

PostgreSQL + PostGIS

Haversine fallback

Burada AI yok.
Tamamen deterministik.

🔷 RankingEngine

Sorumluluk:

Restoran sıralama

CTR tahmini

Relevance scoring

Başlangıç:

Rule-based scoring:

distance_weight

rating_weight

popularity_weight

open_status

Sonra:

XGBoost ranking model

LLM burada kullanılmaz.

🔷 NLPParser (AI)

Sorumluluk:
Kullanıcı query’sini yapısal filtreye çevirmek.

Input:
“5 dakika yürüme mesafesinde açık vegan mekân”

Output:

{
  max_distance: 400m,
  category: "vegan",
  open_now: true
}

Model:
GPT-class LLM (low temperature)

Token kontrolü kritik.

🔷 ExplanationEngine (AI)

Sorumluluk:

Mekân açıklaması üretmek

Konum tarifi yazmak

Öne çıkan özellikleri özetlemek

Burada LLM kullanılır.
Ama sadece üretim için.

🔷 Data Layer
PostgreSQL + PostGIS

Tablolar:

places

id

name

lat

lon

category

rating

open_hours

source

updated_at

user_events

user_id (anon id)

query

clicked_place_id

timestamp

location_cluster

place_metrics

place_id

impressions

clicks

ctr

last_updated

🔷 Redis

Kullanım:

Sık aranan query cache

En yakın 10 sonuç cache

Rate limit

🔷 Analytics

Başlangıç:

Basit event logging

Sonra:

Self-hosted analytics

Funnel analizi

En kritik veri:

Query → Click conversion

🔷 Veri Toplama Stratejisi

Başlangıç veri kaynağı:

OpenStreetMap

Kullanıcı katkısı

Platform scraping yok.

🔷 Ölçeklenebilirlik Planı

Aşama 1:

Monolith

Tek server

Aşama 2:

Service separation

Ranking ayrı container

Aşama 3:

Horizontal scaling

Read replicas

🔷 Güvenlik

API rate limit

Input sanitization

Abuse detection

LLM prompt injection'a dikkat.