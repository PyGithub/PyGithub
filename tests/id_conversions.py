from . import Framework

from github.id_conversions import db_id_and_type_to_node_id, node_id_to_db_id_and_type

class TestIDConversions(Framework.TestCase):
    TEST_GQL_ID = "MDEwOlJlcG9zaXRvcnkzNTQ0NDkw"
    TEST_GQL_TYPE_NAME = "Repository"
    TEST_DB_ID = 3544490

    def test_db_id_and_type_to_node_id(self):
        self.assertEqual(db_id_and_type_to_node_id(self.__class__.TEST_DB_ID, self.__class__.TEST_GQL_TYPE_NAME), self.__class__.TEST_GQL_ID)

    def test_node_id_to_db_id_and_type(self):
        self.assertEqual(node_id_to_db_id_and_type(self.__class__.TEST_GQL_ID), (self.__class__.TEST_DB_ID, self.__class__.TEST_GQL_TYPE_NAME))
