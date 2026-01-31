# GitHub Copilot Instructions — SICMI Django Site

Use these project-specific rules to be immediately productive when coding in this repo.

## Overview
- Stack: Django 5, `whitenoise` static, Cloudinary media, Render deploy.
- Project root: [sicmi_site](sicmi_site) (Django project) + [sicmi_app](sicmi_app) (main app).
- Templates: [templates](templates) with a shared layout in [templates/base.html](templates/base.html).
- Static assets: [static](static) during dev; collected to [staticfiles](staticfiles) in deploy.

## Architecture
- URLs: [sicmi_site/urls.py](sicmi_site/urls.py) mounts `sicmi_app` under `i18n_patterns` (French-only). Dev serves media/static when `DEBUG=True`.
- App routes: [sicmi_app/urls.py](sicmi_app/urls.py) maps pages: `home`, `a-propos`, `services`, `projets`, `contact`, `qhse`, `ateliers`, `recherche`, `equipe`, plus `debug/cloudinary`.
- Views: [sicmi_app/views.py](sicmi_app/views.py) use `select_related`/`prefetch_related` for performance; paginate projects (6/page); filter via `GET` params.
- Settings: [sicmi_site/settings.py](sicmi_site/settings.py) configures `cloudinary_storage` for media and `CompressedManifestStaticFilesStorage` via `whitenoise` for static.

## Data Models
- Core entities in [sicmi_app/models.py](sicmi_app/models.py):
  - `ServiceCategory` → `Service` → `ServiceImage`
  - `Project` → `ProjectImage` (with `is_primary` for hero images)
  - `TeamMember`
  - `ContactRequest`
  - `Atelier` → `AtelierImage`
- Ordering is defined at the model level; prefer respecting these when querying.

## Templates & Static
- Base layout: [templates/base.html](templates/base.html) includes header/nav/footer and defers all JS for performance.
- Page templates: e.g. [templates/services.html](templates/services.html), [templates/projects.html](templates/projects.html), etc.
- Internationalization is disabled (`USE_I18N=False`); do not add `{% trans %}` or i18n loaders.

## Developer Workflow
- Local run:
  ```bash
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver
  ```
- Performance patterns in views:
  - Use `select_related('category')` for `Service`.
  - Use `prefetch_related('images')` for `Project`/`Atelier`.
  - Paginate collections with `Paginator(..., 6)`.
- Forms: `ContactForm` in [sicmi_app/forms.py](sicmi_app/forms.py) saves `ContactRequest`; email sending is intentionally disabled for Render free tier.

## Deployment (Render)
- Build/start via [render.yaml](render.yaml) and [Procfile](Procfile).
- Build steps in [build.sh](build.sh): `collectstatic`, `migrate`, then custom data loaders (`create_admin`, `load_team_members`, `load_ateliers`).
- Required env vars: `SECRET_KEY`, `DATABASE_URL`, `PYTHON_VERSION`, optional `CLOUDINARY_*` for media.
- Keep-alive guidance in [KEEP_ALIVE_GUIDE.md](KEEP_ALIVE_GUIDE.md); debugging Cloudinary at [/debug/cloudinary](sicmi_app/urls.py#L7).

## Conventions & Patterns
- Language: French-only content and routes.
- Media: stored via Cloudinary; file fields use long `upload_to` paths (e.g., `projects/gallery/`). Avoid local writes in production.
- Static: reference via `/static/...`; `whitenoise` handles compression and manifest in deploy.
- Querying: prefer `.select_related()` / `.prefetch_related()` where applicable; avoid N+1.
- Templates: keep JS `defer`; follow existing block structure in `base.html`.

## Useful Management Commands
- Data/admin setup (used in deploy):
  ```bash
  python manage.py create_admin
  python manage.py load_team_members
  python manage.py load_ateliers
  ```
- Other helpers in [sicmi_app/management/commands](sicmi_app/management/commands/).

## Debugging Tips
- Cloudinary config check: `/debug/cloudinary` → returns JSON with storage flags ([sicmi_app/views_debug.py](sicmi_app/views_debug.py)).
- Performance fixes documented in [PERFORMANCE_FIX.md](PERFORMANCE_FIX.md).
- Render deploy steps in [DEPLOY_RENDER.md](DEPLOY_RENDER.md).

## When Adding Features
- New pages: add route in [sicmi_app/urls.py](sicmi_app/urls.py), view in [sicmi_app/views.py](sicmi_app/views.py), template in [templates](templates), link via header/nav includes.
- New models/images: define in [sicmi_app/models.py](sicmi_app/models.py), run `makemigrations`/`migrate`, and consider a loader in `management/commands` if initial data is needed.
- Lists with images: use `.prefetch_related('images')` and pass ordered querysets to templates to keep response fast.

Questions or gaps? Comment in PRs or ask to clarify specific workflows (local dev, Cloudinary creds, Render env).