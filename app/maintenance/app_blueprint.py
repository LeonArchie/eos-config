# SPDX-License-Identifier: AGPL-3.0-only WITH LICENSE-ADDITIONAL
# Copyright (C) 2025 Петунин Лев Михайлович

from k8s.healthz import healthz_bp
from k8s.readyz import readyz_bp
from api.config_create.config_create import config_bp
from api.read.read_param import read_bp
from api.update.update_param import update_bp
from api.validate_create.validate_create import create_validate_bp
from maintenance.logging_config import setup_logging
from api.error_handlers import not_found

def register_blueprints(app):
    """Регистрация всех blueprint'ов в приложении"""
    app.register_blueprint(healthz_bp)
    app.register_blueprint(readyz_bp)
    app.register_blueprint(config_bp)
    app.register_blueprint(read_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(create_validate_bp)

def register_error_handlers(app):
    """Регистрация обработчиков ошибок"""
    app.register_error_handler(404, not_found)