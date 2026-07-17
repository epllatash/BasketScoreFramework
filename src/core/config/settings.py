from pathlib import Path

# Carpeta raíz del proyecto
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Carpetas principales
ASSETS_DIR = PROJECT_ROOT / "assets"
CONFIG_DIR = PROJECT_ROOT / "config"
LOGS_DIR = PROJECT_ROOT / "logs"
DATABASE_DIR = PROJECT_ROOT / "database"

# Información de la aplicación
APP_NAME = "BasketScore Framework"
APP_VERSION = "0.1.0"
COMPANY = "Black Panther Software"

# Crear carpetas automáticamente si no existen
LOGS_DIR.mkdir(exist_ok=True)
DATABASE_DIR.mkdir(exist_ok=True)
