class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def test_if_cats_size_is_oncresed_afer_eating(self):
        cat = Cat('Gar')
        cat.eat()
        self.assertEqual(1, cat.size)
    def test_if_cat_is_fed_after_eaitng(self):
        cat = Cat('Gar')
        cat.eat()
        self.assertTrue(cat.fed)
    def test_if_raises_after_eat_fed_cat(self):
        with self.assertRaises(Exception) as ex:
            cat = Cat('Gar')
            cat.eat()
            cat.eat()
        self.assertEqual('Already fed.',str(ex.exception))
    def test_if_caT_cannot_sleep_after_fed(self):
        with self.assertRaises(Exception) as ex:
            cat = Cat('Gar')
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
    def test_if_cat_is_sleepy_after_sleep(self):
        cat = Cat('Kiko')
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)
if __name__ == '__main__':
    main()
