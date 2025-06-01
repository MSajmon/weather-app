# Zadanie 2 – CI/CD z Dockerem i GitHub Actions

## ⚙️ Opis działania workflow

Workflow znajduje się w `.github/workflows/docker-publish.yml`.

Główne kroki:
1. **Checkout repozytorium**
2. **Buildx** – umożliwia multi-arch build.
3. **Docker Scout** – skanowanie obrazu tymczasowego (`temp`) pod kątem CVE.
4. **Publikacja** – obraz przesyłany do GHCR tylko, jeśli skan nie wykryje krytycznych/zagrażających luk.

---

## 🧱 Tagowanie obrazów

Obrazy są tagowane automatycznie jako:

- `latest` – dla gałęzi `main`,
- `ghcr.io/msajmon/weather-app:<commit_sha>` – identyfikacja obrazu po commicie,
- `ghcr.io/msajmon/weather-app:<ref_name>` – np. `v1.0.0` jeśli tag został użyty.

### Cache image

Obraz cache’ujący tworzony jest w publicznym repozytorium DockerHub:

docker.io/<DOCKERHUB_USERNAME>/zadanko1-cache:latest

Dzięki temu buildy mogą wykorzystywać wcześniej zbudowane warstwy, co przyspiesza proces.

**Uzasadnienie**: Takie tagowanie zapewnia kontrolę wersji, łatwe roll-backi oraz zgodność z dobrymi praktykami CI/CD ([semver.org](https://semver.org)).

---

##  Wymagane sekrety

W repozytorium GitHub muszą być ustawione następujące sekrety:

| Nazwa              | Opis                               |
|--------------------|------------------------------------|
| `GHCR_TOKEN`        | Token do logowania w `ghcr.io`     |
| `DOCKERHUB_USERNAME`| Login do DockerHub                |
| `DOCKERHUB_TOKEN`   | Token do logowania DockerHub      |

---

## ✅ Test działania

Pipeline został uruchomiony poprzez `push` do `main`. Po pozytywnym skanowaniu CVE obraz został przesłany do `ghcr.io`.

---

##  Skanowanie bezpieczeństwa – Docker Scout

Zastosowano **Docker Scout**, ponieważ:

- dobrze integruje się z Docker CLI i GitHub Actions,
- nie wymaga dodatkowej konfiguracji ani rejestracji,
- zapewnia szybkie i czytelne wyniki.

Alternatywą mogło być narzędzie Trivy, jednak Scout był prostszy w integracji z workflow GitHub Actions.

---

## Link do pomyślnie wykonanego łańcucha
(https://github.com/MSajmon/weather-app/actions/runs/15379376090/job/43268136791)

## 📌 Podsumowanie

Pipeline został skonfigurowany zgodnie z założeniami zadania 2 i przeszedł testowe uruchomienie z sukcesem
