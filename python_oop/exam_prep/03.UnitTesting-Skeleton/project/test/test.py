from unittest import TestCase, main
from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('Star Wars', 1979, 4.9)

    def test_init_with_correct_data(self):
        self.assertEqual('Star Wars', self.movie.name)
        self.assertEqual(1979, self.movie.year)
        self.assertEqual(4.9, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_validation_raises(self):
        with self.assertRaises(ValueError) as ex:
            using = Movie('', 1979, 4.9)
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_name_with_correct_data(self):
        self.assertEqual('Star Wars', self.movie.name)

    def test_year_validation_raises(self):
        with self.assertRaises(ValueError) as ex:
            using = Movie('Star Wars', 1886, 4.9)
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_year_with_correct_data(self):
        self.assertEqual(1979, self.movie.year)

    def test_rating_with_correct_data(self):
        self.assertEqual(4.9, self.movie.rating)

    def test_add_actor_method_with_correct_data(self):
        self.movie.add_actor('Harrison')
        self.movie.add_actor('Ford')
        self.assertEqual(['Harrison', 'Ford'], self.movie.actors)

    def test_add_actor_method_with_incorrect_data(self):
        self.movie.add_actor('Harrison')
        actual = self.movie.add_actor('Harrison')
        result = f"Harrison is already added in the list of actors!"
        self.assertEqual(result, actual)

    def test_gt_method(self):
        other = Movie('Cars', 2006, 4.5)
        result = other < self.movie
        second_result = self.movie < other
        another_one = Movie("Toy's story", 2004, 5.00)
        third_result = another_one > self.movie
        self.assertEqual(f'"{self.movie.name}" is better than "{other.name}"', result)
        self.assertEqual(f'"{self.movie.name}" is better than "{other.name}"', second_result)
        self.assertEqual(f'"{another_one.name}" is better than "{self.movie.name}"', third_result)

    def test_gt_method_on_the_other_side(self):
        another_one = Movie("Toy's story", 2004, 5.00)
        third_result = another_one > self.movie

        self.assertEqual(f'"{another_one.name}" is better than "{self.movie.name}"', third_result)

    def test_repr_method_works_correctly(self):
        self.movie.add_actor('George')
        self.movie.add_actor('Clooney')
        expected_result = f"Name: {self.movie.name}\n" \
                          f"Year of Release: {self.movie.year}\n" \
                          f"Rating: {self.movie.rating:.2f}\n" \
                          f"Cast: George, Clooney"
        self.assertEqual(expected_result, repr(self.movie))


if __name__ == '__main__':
    main()
