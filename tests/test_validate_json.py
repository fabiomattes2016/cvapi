from unittest import TestCase
from typing import List
from flask import url_for, Flask
from cvapi import create_app


def app_endpoint(app: Flask) -> List[str]:
    """
    Retorna todos os endpoints do `app`
    """
    return [e.endpoint for e in app.url_map.iter_rules()]


class FlaskBaseTestCase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()


class TestRouteValidateJson(FlaskBaseTestCase):
    def test_app_deve_conter_a_rota_validate_json(self):
        app = create_app()
        endpoints = app_endpoint(app)
        
        self.assertIn(
            'validate_json',
            endpoints,
            'o endpoint validade-json não existe no App'
        )


    def test_deve_retornar_uma_requisicao_valida(self):
        response = self.client.post(url_for('validate_json'))
        self.assertIn(response.status_code, list(range(100, 511)))


    def test_deve_receber_um_objeto_json(self):
        response = self.client.post(
            url_for('validate_json'),
            json={1: 2}
        )

        self.assertEqual(response.json, {'ok': 'dados válidos'})
    