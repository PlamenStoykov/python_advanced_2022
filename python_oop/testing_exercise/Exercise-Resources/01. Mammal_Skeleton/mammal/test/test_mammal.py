from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    KINGDOM = "animals"
    NAME = 'Bat'
    SOUND = "sound"
    TYPE = "flying"

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test_initialising_method_should_create_proper_obj(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual(self.KINGDOM, self.mammal._Mammal__kingdom)

    def test_make_sound_method_returns_proper_result(self):
        actual_result = self.mammal.make_sound()
        expected_result = f"{self.NAME} makes {self.SOUND}"
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom_method_returns_animals(self):
        actual_result = self.mammal.get_kingdom()
        self.assertEqual(self.KINGDOM, actual_result)

    def test_info_method(self):
        self.assertEqual(f"{self.NAME} is of type {self.TYPE}", self.mammal.info())


if __name__ == '__main__':
    main()
