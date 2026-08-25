# Semana 02 — Entorno virtual y buenas prácticas

## Entorno virtual

El entorno virtual se creó una única vez en la raíz del repositorio (no dentro
de esta carpeta) con:

```bash
python3 -m venv venv
```

Para activarlo en Windows (PowerShell), desde la raíz del repositorio:

```bash
.\venv\Scripts\Activate.ps1
```

## requirements.txt

Con el entorno activado se instaló matplotlib y se generó el archivo de
dependencias, también en la raíz:

```bash
pip install matplotlib
pip freeze > requirements.txt
```

## Cómo reproducir este entorno

Otra persona puede reproducir el entorno exacto desde la raíz del repositorio con:

```bash
python3 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```