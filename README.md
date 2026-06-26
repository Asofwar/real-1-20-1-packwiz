# Real 1-20-1 Mac Packwiz Repo

Этот каталог готов к публикации как GitHub-репозиторий для `packwiz`.

Что внутри:
- `pack.toml` и `index.toml`
- `mods/`
- `config/`
- `kubejs/`
- `defaultconfigs/`
- `resourcepacks/`

Как опубликовать:
1. Создайте пустой GitHub-репозиторий.
2. Скопируйте содержимое этой папки в репозиторий.
3. Выполните:

```bash
git init
git add .
git commit -m "Initial packwiz pack"
git branch -M main
git remote add origin https://github.com/<github-user>/<repo-name>.git
git push -u origin main
```

Pack URL для Prism/macOS-инстанса:

```text
https://raw.githubusercontent.com/<github-user>/<repo-name>/main/pack.toml
```

После первого пуша используйте соседний шаблон Prism-инстанса и скрипт `configure-packwiz-github.ps1`,
чтобы подставить ваш реальный URL и собрать zip для друзей.
