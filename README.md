# Real 1-20-1 Packwiz Pack

[![Validate Packwiz Metadata](https://github.com/Asofwar/real-1-20-1-packwiz/actions/workflows/validate-packwiz.yml/badge.svg)](https://github.com/Asofwar/real-1-20-1-packwiz/actions/workflows/validate-packwiz.yml)
[![Refresh Packwiz Hashes](https://github.com/Asofwar/real-1-20-1-packwiz/actions/workflows/refresh-packwiz-hashes.yml/badge.svg)](https://github.com/Asofwar/real-1-20-1-packwiz/actions/workflows/refresh-packwiz-hashes.yml)

Универсальная клиентская сборка `Minecraft 1.20.1` на `Fabric` для Prism Launcher с автообновлением через `packwiz`.

## Что это

Этот репозиторий хранит:

- список модов
- конфиги клиента
- ресурс-паки
- шейдеры
- packwiz-метаданные для автоматического обновления

Клиент можно использовать и на Windows, и на macOS.

## Установка

### Вариант 1. Через готовый Prism-инстанс

Импортируйте подготовленный Prism-инстанс и запускайте игру как обычно.
При старте `packwiz` сам проверит обновления и подтянет недостающие файлы.

### Вариант 2. Через `packwiz` напрямую

Точка входа пакета:

```text
https://raw.githubusercontent.com/Asofwar/real-1-20-1-packwiz/main/pack.toml
```

## Как работает обновление

- перед запуском Prism вызывает `packwiz-installer-bootstrap`
- клиент сверяет локальные файлы с `pack.toml` и `index`
- если в сборке что-то изменилось, нужные файлы скачиваются автоматически

## Структура репозитория

- `pack.toml` и `pack-20260627.toml` — точки входа packwiz
- `index-main.toml` и `index-20260627.toml` — индекс файлов и хэшей
- `mods/` — описания модов `*.pw.toml`
- `config/` — клиентские конфиги
- `defaultconfigs/` — дефолтные конфиги модов
- `resourcepacks/` — ресурс-паки
- `shaderpacks/` — шейдеры
- `kubejs/` — скрипты и ассеты KubeJS
- `scripts/` — служебные скрипты проверки

## Автопроверки

В репозитории включены GitHub Actions:

- `Validate Packwiz Metadata`
  - проверяет, что `*.pw.toml`, `index*.toml` и `pack*.toml` согласованы между собой
  - ловит ошибки хэшей и проблемы с переводами строк
- `Refresh Packwiz Hashes`
  - автоматически нормализует line endings и пересчитывает packwiz-хэши при изменениях

## Если у клиента проблемы

Если Prism показывает `Failed file downloads` или клиент не пускает на сервер из-за несовпадения модов:

1. Закройте Prism Launcher.
2. В проблемном инстансе удалите:
   - `minecraft/packwiz.json`
   - `minecraft/packwiz-installer.jar`
   - случайные `minecraft/mods/*.pw.toml`
3. Запустите инстанс снова.

Если проблема не ушла, проверьте статус workflow в этом репозитории и актуальность `pack.toml`.

## Технические параметры

- Minecraft: `1.20.1`
- Loader: `Fabric 0.16.10`
- Формат: `packwiz:1.1.0`

## Ссылки

- Репозиторий: [Asofwar/real-1-20-1-packwiz](https://github.com/Asofwar/real-1-20-1-packwiz)
- `pack.toml`: [raw link](https://raw.githubusercontent.com/Asofwar/real-1-20-1-packwiz/main/pack.toml)
