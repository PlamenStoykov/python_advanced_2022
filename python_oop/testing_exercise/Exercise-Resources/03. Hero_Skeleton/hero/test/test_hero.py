from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Eevee', 21, 99.9, 33.5)
        self.enemy_hero = Hero('Snorlax', 20, 90, 22.5)

    def test_if_init_works_properly(self):
        self.assertEqual('Eevee', self.hero.username)
        self.assertEqual(21, self.hero.level)
        self.assertEqual(99.9, self.hero.health)
        self.assertEqual(33.5, self.hero.damage)

    def test_battle_method_raises_error_fighting_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_raises_error_fighting_with_no_health(self):
        with self.assertRaises(ValueError) as ex:
            self.hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_method_raises_error_fighting_enemy_with_no_health(self):
        with self.assertRaises(ValueError) as ex:
            self.enemy_hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_draw_battle_method_scenario(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(result, "Draw")

    def test_you_win_battle_method_scenario(self):
        using = Hero('Ratata', 1, 10, 0.5)
        result = self.hero.battle(using)
        self.assertEqual(result, "You win")
        self.assertEqual(22, self.hero.level)
        self.assertEqual(104.9-0.5, self.hero.health)
        self.assertEqual(38.5, self.hero.damage)

    def test_you_lose_battle_method_scenario(self):
        using = Hero('Mew', 50, 10000, 49.5)
        result = self.hero.battle(using)
        self.assertEqual(result, "You lose")
        self.assertEqual(51, using.level)
        self.assertEqual(10005-703.5, using.health)
        self.assertEqual(54.5, using.damage)

    def test_string_method_works_properly(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                   f"Health: {self.hero.health}\n" \
                   f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected, str(self.hero))


if __name__ == '__main__':
    main()
