# FormWizard
## Бот для автоматизированного заполнения шаблонов документов

### Запуск локально
1. Добавляем файл `.env` на основе `.env.example`
2. Устанавливаем UV если отсутствует `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. Создаем окружение `uv sync`
4. Запускаем `PYTHONPATH=. uv run src/main.py`

### Запуск через DOCKER
1. Добавляем файл `.env` на основе `.env.example`
2. Собираем образ `docker build . -t=form_wizard -f=docker/Dockerfile`
3. Запускаем `docker run -d --env-file=.env --name form_wizard form_wizard`
