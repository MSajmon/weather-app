#  Zadanie 2 – CI/CD z wykorzystaniem GitHub Actions
Repozytorium zawiera konfigurację łańcucha CI/CD w usłudze GitHub Actions dla aplikacji pogodowej opracowanej w Zadaniu 1.


## Zakres działania pipeline'u
Pipeline (`.github/workflows/docker-publish.yml`) automatycznie:
1. Buduje obraz kontenera aplikacji z pliku `Dockerfile`
2. Wspiera platformy `linux/amd64` i `linux/arm64`
3. Wykorzystuje mechanizm cache BuildKit (eksporter: `registry`, backend: `registry`, tryb `max`)
4. Wykonuje skan bezpieczeństwa obrazu przy użyciu narzędzia **Trivy**
5. Publikuje obraz do **GitHub Container Registry (GHCR)**, jeśli nie wykryto podatności `CRITICAL` lub `HIGH`


## 🔐 Sekrety GitHub (Secrets)
W repozytorium utworzyłem następujące **sekrety**:
  `DOCKERHUB_USERNAME`    `DOCKERHUB_TOKEN`


##  Tagowanie obrazów i danych cache
### Obrazy Docker:
- Publiczne obrazy aplikacji są publikowane do GitHub Container Registry (GHCR):
  - `ghcr.io/msajmon/weather-app:latest`
### Cache budowania:
- Cache warstw budowania jest przechowywany w publicznym repozytorium DockerHub:
  - `docker.io/msajmon/weather-app-cache:buildcache`


## Testowanie bezpieczeństwa (CVE)
W łańcuchu CI/CD używany jest **Trivy**, który sprawdza zbudowany obraz pod kątem podatności bezpieczeństwa:
