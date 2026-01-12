from unittest import TestCase
from .register_script import register_script, script_classes
from .script import Script


class TestRegisterHandler(TestCase):
    def setUp(self):
        script_classes = []

    def test_a_handler_instance_is_added(self):
        @register_script
        class TestScript(Script):
            @classmethod
            def can_handle(file):
                return False

            def create_script_for(file):
                return None
        
        self.assertIsInstance(script_classes[0], TestScript)
