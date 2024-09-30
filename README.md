## Architecture Diagram
```mermaid
graph TD;
    subgraph "Frontend/UI"
        Streamlit
    end
    subgraph "Backend/API"
        FastAPI
    end
    subgraph "Data Storage"
        PostgreSQL
    end
    subgraph "Data Processing"
        Spark
        Airflow
    end
    subgraph "External Data Sources"
        Financial_APIs["Financial APIs (e.g., Alpha Vantage)"]
        News_APIs["News APIs (e.g., NewsAPI)"]
    end
    
    Streamlit -->|User Input / Data Request| FastAPI
    FastAPI -->|Serves Processed Data| Streamlit
    FastAPI -->|Queries Processed Data| PostgreSQL
    Spark -->|Batch Processing of Financial & News Data| PostgreSQL
    Airflow -->|Orchestrates Batch Jobs| Spark
    Airflow -->|Ingests Data| Financial_APIs & News_APIs
    Financial_APIs -->|Ingest Data| Airflow
    News_APIs -->|Ingest Data| Airflow

```
## Data Flow Diagram
```mermaid
graph TD;
    Financial_APIs["Financial APIs"] -->|Data Ingestion| Airflow
    News_APIs["News APIs"] -->|Data Ingestion| Airflow
    Airflow -->|Triggers Spark Jobs| Spark
    Spark -->|Processes Stock & News Data| PostgreSQL
    PostgreSQL -->|Stores Processed Data| FastAPI
    FastAPI -->|Serves Data to UI| Streamlit
    Streamlit -->|Displays Financial Data & Sentiment| User

```
## Entity Relationship Diagram
```mermaid
erDiagram
    STOCKS {
        int id PK
        string ticker
        string name
        string sector
        string exchange
    }
    
    STOCK_PRICES {
        int id PK
        int stock_id FK
        date price_date
        decimal open_price
        decimal close_price
        decimal high_price
        decimal low_price
        bigint volume
        timestamp created_at
    }
    
    NEWS_ARTICLES {
        int id PK
        string ticker FK
        string article_title
        string article_url
        timestamp publish_date
        string source
        timestamp created_at
    }
    
    NEWS_SENTIMENTS {
        int id PK
        int article_id FK
        decimal sentiment_score
        timestamp created_at
    }
    
    STOCKS ||--o{ STOCK_PRICES : has
    STOCKS ||--o{ NEWS_ARTICLES : has
    NEWS_ARTICLES ||--o{ NEWS_SENTIMENTS : has

```
## Instructions
1. Create a `.env` and add API Keys for Alphavantage and FMP
```
ALPHAVANTAGE_API_KEY=XXXX
FMP_API_KEY=XXXX
``` 