# Real 1-20-1 Packwiz Pack

[![Validate Packwiz Metadata](https://github.com/Asofwar/real-1-20-1-packwiz/actions/workflows/validate-packwiz.yml/badge.svg)](https://github.com/Asofwar/real-1-20-1-packwiz/actions/workflows/validate-packwiz.yml)
[![Refresh Packwiz Hashes](https://github.com/Asofwar/real-1-20-1-packwiz/actions/workflows/refresh-packwiz-hashes.yml/badge.svg)](https://github.com/Asofwar/real-1-20-1-packwiz/actions/workflows/refresh-packwiz-hashes.yml)

Универсальная клиентская сборка `Minecraft 1.20.1` на `Fabric` для Prism Launcher с автообновлением через `packwiz`.

## Что хранится в репозитории

- `pack.toml` - главная точка входа packwiz
- `index-main.toml` - индекс файлов и хэшей
- `mods/` - метаданные модов `*.pw.toml`
- `config/` - клиентские конфиги
- `defaultconfigs/` - дефолтные конфиги модов
- `resourcepacks/` - ресурспаки
- `shaderpacks/` - шейдеры
- `kubejs/` - скрипты и ассеты KubeJS
- `scripts/` - служебные проверки

Сборка рассчитана и на Windows, и на macOS.

## Точка входа

```text
https://raw.githubusercontent.com/Asofwar/real-1-20-1-packwiz/main/pack.toml
```

## Как работает обновление

- перед стартом Prism вызывает `packwiz-installer-bootstrap`
- клиент сверяет локальные файлы с `pack.toml` и `index-main.toml`
- если сборка изменилась, нужные файлы скачиваются автоматически

## Автопроверки

В репозитории включены GitHub Actions:

- `Validate Packwiz Metadata` - проверяет согласованность `mods/*.pw.toml`, `index-main.toml` и `pack.toml`
- `Refresh Packwiz Hashes` - нормализует line endings и пересчитывает packwiz-хэши при изменениях

## Если у клиента проблемы

Если Prism показывает `Failed file downloads` или клиент не пускает на сервер из-за рассинхрона:

1. Закройте Prism Launcher.
2. В проблемном инстансе удалите `minecraft/packwiz.json`.
3. Удалите случайные `minecraft/mods/*.pw.toml`, если они появились рядом с `.jar`.
4. Запустите инстанс снова.

Если проблема не ушла, проверьте статус workflow в репозитории и актуальность `pack.toml`.

## Технические параметры

- Minecraft: `1.20.1`
- Loader: `Fabric 0.16.10`
- Формат: `packwiz:1.1.0`

## Ссылки

- Репозиторий: [Asofwar/real-1-20-1-packwiz](https://github.com/Asofwar/real-1-20-1-packwiz)
- `pack.toml`: [raw link](https://raw.githubusercontent.com/Asofwar/real-1-20-1-packwiz/main/pack.toml)
