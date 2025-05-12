## 📄 zadanie1.md – Sprawozdanie do Zadania 1  
Autor: **Szymon Marczak**

### 1. Aplikacja pogodowa
Aplikacja webowa oparta na Flask pozwala użytkownikowi wybrać kraj i miasto, a następnie pobiera aktualne dane pogodowe z OpenWeatherMap API.

### 2. Dockerfile
Wieloetapowe budowanie z wykorzystaniem python:3.12-slim. Dodano metadane autora i HEALTHCHECK.

### 3. Polecenia

a) Budowanie obrazu:
```bash
docker build -t szymonmarczak/weather-app .
```

b) Uruchomienie kontenera:
```bash
docker run -d -p 5000:5000 --name weather-container -e WEATHER_API_KEY=YOUR_API_KEY szymonmarczak/weather-app
```

c) Podgląd logów:
```bash
docker logs weather-container
```

d) Sprawdzenie warstw i rozmiaru:
```bash
docker history szymonmarczak/weather-app
docker image inspect szymonmarczak/weather-app --format='{{.Size}}'
```

### 4. Repozytoria (uzupełnić po publikacji)
- GitHub: https://github.com/twoj-user/weather-app
- DockerHub: https://hub.docker.com/r/szymonmarczak/weather-app