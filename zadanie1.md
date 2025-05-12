## zadanie1.md – Sprawozdanie do Zadania 1  
Autor: **Szymon Marczak**

### 3. Polecenia

a) Budowanie obrazu:
```bash
docker build -t msajmon/weather-app .
```

b) Uruchomienie kontenera:
```bash
docker run -d -p 5000:5000 --name weather-container -e WEATHER_API_KEY=e3f83988b6f2d5bd947c61c8a2161934 msajmon/weather-app
```

c) Podgląd logów:
```bash
docker logs weather-container
```

d) Sprawdzenie warstw i rozmiaru:
```bash
docker history msajmon/weather-app
docker image inspect msajmon/weather-app --format='{{.Size}}'
```

### Repozytoria
- GitHub: [https://github.com/msajmon/weather-app]
- DockerHub: [https://hub.docker.com/r/msajmon/weather-app]