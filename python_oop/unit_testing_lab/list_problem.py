class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def test_init_method_with_incorrect_data_provided(self):
        using = IntegerList('a', 'b', 'c', 3.5)
        self.assertEqual([], using._IntegerList__data)

    def test_init_method_with_no_data_provided(self):
        using = IntegerList()
        self.assertEqual([], using._IntegerList__data)

    def test_init_method_with_correct_data_provided(self):
        using = IntegerList(1, 'asd', 4)
        self.assertEqual([1, 4], using._IntegerList__data)
        self.assertEqual(1, using.get_index(4))

    def test_add_method_work_correctly(self):
        using = IntegerList(5)
        using.add(4)
        self.assertEqual([5, 4], using._IntegerList__data)
        self.assertEqual([5, 4, 3], using.add(3))

    def test_add_method_work_raises(self):
        with self.assertRaises(ValueError) as ex:
            using = IntegerList(5)
            using.add('asd')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_works_correctly(self):
        using = IntegerList(5, 4)
        self.assertEqual(4, using.remove_index(1))
        using = IntegerList(5)
        using.remove_index(0)
        self.assertEqual([], using._IntegerList__data)

    def test_remove_index_works_correctly_testing_the_returned_obj(self):
        using = IntegerList(5, 4)
        using.remove_index(1)
        self.assertEqual([5], using._IntegerList__data)

    def test_remove_method_work_raises(self):
        with self.assertRaises(IndexError) as ex:
            using = IntegerList(5, 4)
            using.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_method_work_raises_with_greater_idx(self):
        with self.assertRaises(IndexError) as ex:
            using = IntegerList(5, 4)
            using.remove_index(6)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_correctly(self):
        using = IntegerList(5, 4, 6)
        self.assertEqual(6, using.get(2))

    def test_get_raises(self):
        with self.assertRaises(IndexError) as ex:
            using = IntegerList(5)
            using.get(7)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            using = IntegerList(5)
            using.insert(2, 3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_works_correctly(self):
        using = IntegerList(1, 2, 3, 4)
        self.assertEqual([1, 2, 3, 4], using._IntegerList__data)

    def test_insert_method_el_is_not_int(self):
        with self.assertRaises(ValueError) as ex:
            using = IntegerList(5, 6, 7, 8)
            using.insert(2, 3.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest(self):
        using = IntegerList(1, 2)
        self.assertEqual(2, using.get_biggest())

    def test_get_index_works_correctly(self):
        using = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual(0, using.get_index(1))

    def test_get_data(self):
        using = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual([1, 2, 3, 4, 5], using._IntegerList__data)
        result = using.get_data()
        self.assertEqual([1, 2, 3, 4, 5], result)


if __name__ == "__main__":
    main()
