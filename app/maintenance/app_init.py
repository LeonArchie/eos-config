# SPDX-License-Identifier: AGPL-3.0-only WITH LICENSE-ADDITIONAL
# Copyright (C) 2025 Петунин Лев Михайлович

from flask import Flask

from maintenance.logging_config import setup_logging
from maintenance.request_logging import log_request_info, log_request_response
from maintenance.app_blueprint import register_blueprints, register_error_handlers

logger = setup_logging()

def create_app():
    """Создание и инициализация Flask приложения"""
    app = Flask(__name__)
    
    # Настройка middleware
    @app.before_request
    def before_request():
        log_request_info()

    @app.after_request
    def after_request(response):
        return log_request_response(response)
  
    # Регистрация blueprint'ов
    register_blueprints(app)

    # Регистрация обработчиков ошибок
    register_error_handlers(app)
    
    logger.info("Приложение успешно инициализировано")
    return app
