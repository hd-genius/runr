from unittest import TestCase
from .register_handler import register_handler, script_handlers
from .script_handler import ScriptHandler


class TestRegisterHandler(TestCase):
    def setUp(self):
        script_handlers = []

    def test_a_handler_instance_is_added(self):
        @register_handler
        class TestHandler(ScriptHandler):
            def can_handle(file):
                return False

            def create_script_for(file):
                return None
        self.assertIsInstance(script_handlers[0], TestHandler)
