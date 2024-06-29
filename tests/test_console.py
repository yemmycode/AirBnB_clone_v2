#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand testing setup.

        Temporarily rename any existing file.json.
        Reset FileStorage objects dictionary.
        Create an instance of the command interpreter.
        """
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """HBNBCommand testing teardown.

        Restore original file.json.
        Delete the test HBNBCommand instance.
        """
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

        del cls.HBNB

    def setUp(self):
        """Reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create_for_errors(self):
        """Test create command errors."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create asdfsfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_create_command_validity(self):
        """Test create command."""
        classes = ["BaseModel", "User", "State", "Place", "City", "Review", "Amenity"]
        ids = {}

        for cls_name in classes:
            with patch("sys.stdout", new=StringIO()) as f:
                self.HBNB.onecmd(f"create {cls_name}")
                ids[cls_name] = f.getvalue().strip()

        for cls_name, obj_id in ids.items():
            with patch("sys.stdout", new=StringIO()) as f:
                self.HBNB.onecmd(f"all {cls_name}")
                self.assertIn(obj_id, f.getvalue())

    def test_create_command_with_kwargs(self):
        """Test create command with kwargs."""
        with patch("sys.stdout", new=StringIO()) as f:
            call = ('create Place city_id="0001" name="My_house" number_rooms=4 latitude=37.77 longitude=43.434')
            self.HBNB.onecmd(call)
            pl = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            output = f.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'name': 'My_house'", output)
            self.assertIn("'number_rooms': 4", output)
            self.assertIn("'latitude': 37.77", output)
            self.assertIn("'longitude': 43.434", output)


if __name__ == "__main__":
    unittest.main()
