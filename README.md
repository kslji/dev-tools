# DevUtils Microservice

A FastAPI microservice providing a collection of developer utility APIs including JWT encoding/decoding, Base64 encoding/decoding, UUID generation, SQL formatting, Regex testing, and YAML validation/formatting.

## Features & Endpoints

### 1. JWT Utilities
* **Encode JWT** (`POST /api/v1/jwt/encode`)
  * Generates a signed JSON Web Token.
* **Decode JWT** (`POST /api/v1/jwt/decode`)
  * Decodes and validates JWTs (supports verification or extraction only).

### 2. Base64 Utilities
* **Encode Base64** (`POST /api/v1/base64/encode`)
  * Encodes text to standard or URL-safe Base64.
* **Decode Base64** (`POST /api/v1/base64/decode`)
  * Decodes standard or URL-safe Base64 strings.

### 3. UUID Generator
* **Generate UUIDs** (`GET /api/v1/uuid/generate`)
  * Generates a specified count of v4 UUIDs.

### 4. SQL Formatter
* **Format SQL** (`POST /api/v1/sql/format`)
  * Reindents and formats SQL queries with optional case customization.

### 5. Regex Tester
* **Test Regex** (`POST /api/v1/regex/test`)
  * Validates regular expression patterns and finds matches/capture groups.

### 6. YAML Utilities
* **Validate YAML** (`POST /api/v1/yaml/validate`)
  * Checks if a YAML string is syntactically valid (reports line/column on error).
* **Format YAML** (`POST /api/v1/yaml/format`)
  * Beautifies and formats YAML strings.

---

## Getting Started

### Prerequisites
* Python 3.9+

### Setup and Running

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Uvicorn server**:
   ```bash
   # Defaults to port 8000
   python -m uvicorn app.main:app --reload
   ```

---

## Testing APIs (Examples)

### UUID Generation
```bash
curl -X GET "http://127.0.0.1:8000/api/v1/uuid/generate?count=3"
```

### JWT Encode
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/jwt/encode" \
     -H "Content-Type: application/json" \
     -d '{"payload": {"sub": "1234567890", "name": "John Doe", "iat": 1516239022}, "key": "secret", "algorithm": "HS256"}'
```

### JWT Decode
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/jwt/decode" \
     -H "Content-Type: application/json" \
     -d '{"token": "YOUR_TOKEN_HERE", "verify": false}'
```

### SQL Format
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/sql/format" \
     -H "Content-Type: application/json" \
     -d '{"sql": "select * from users where id=1;", "keyword_case": "upper", "reindent": true, "indent_width": 2}'
```
