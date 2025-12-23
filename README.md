# Desafio Lacrei Saude – API

API desenvolvida como parte do desafio tecnico da Lacrei Saude. O projeto foi estruturado com foco em boas praticas de arquitetura, qualidade de codigo, containerizacao e pipeline de CI/CD.

## Visao geral
- Backend em Django + Django REST Framework.
- Banco de dados PostgreSQL.
- Execucao local com Poetry e via Docker.
- CI/CD com GitHub Actions e deploy em EC2 com imagens no GHCR.

## Setup local (sem Docker)

### Pre-requisitos
- Python 3.13+
- PostgreSQL 15+
- Poetry 2.x

### Variaveis de ambiente (exemplo)
```bash
export DATABASE_URL="postgresql://lacrei:lacrei@localhost:5432/lacrei"
export ALLOWED_HOSTS="localhost,127.0.0.1"
```

### Instalar dependencias e rodar
```bash
poetry install
poetry run python src/manage.py migrate
poetry run python src/manage.py runserver
```

## Setup via Docker

### Subir servicos
```bash
docker compose up -d --build
```

### Ver logs
```bash
docker compose logs -f api
```

### Encerrar
```bash
docker compose down
```

## Execucao dos testes
```bash
poetry run python src/manage.py test
```

## Fluxo de deploy (CI/CD)
- CI no GitHub Actions: instala dependencias, roda lint e testes.
- Build da imagem Docker e push para o GitHub Container Registry (GHCR).
- Deploy automatizado via SSH para EC2, usando a imagem publicada.
- Ambientes separados para staging e producao.

## Justificativas tecnicas
- **Django + DRF**: maturidade, produtividade e ecossistema robusto para APIs.
- **PostgreSQL**: banco relacional confiavel para dados transacionais.
- **Poetry**: gerenciamento de dependencias e ambiente previsivel.
- **Docker + Compose**: ambiente reproduzivel e facil de subir localmente.
- **CI/CD no GitHub Actions**: integracao nativa com o repositorio e suporte a pipelines simples.
- **Deploy em EC2**: controle total do ambiente e facilidade de rollback via imagem.

## Proposta de rollback funcional
- **Blue/Green**: manter dois servicos (blue e green) e alternar o balanceador para o ambiente estavel.
- **Revert no GitHub Actions**: disparar workflow manual que faz rollback para a ultima imagem conhecida como estavel.
- **Preview Deploy**: criar ambientes temporarios para PRs, validando antes de promover para producao.

## Estrutura do projeto
- `src/config/`: settings, URLs e entrypoints ASGI/WSGI.
- `src/core/`: app principal (models, serializers, views).
- `tests/`: testes da API.
