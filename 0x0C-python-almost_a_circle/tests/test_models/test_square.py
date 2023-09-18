#!/usr/bin/python3
# test_square.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines unittests for models/square.py.

Unittest classes:
    TestSquare_instantiation
    TestSquare_size
    TestSquare_x
    TestSquare_y
    TestSquare_order_of_initialization
    TestSquare_area
    TestSquare_stdout
    TestSquare_update_args
    TestSquare_update_kwargs
    TestSquare_to_dictionary
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(5), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(5), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(2)
        s2 = Square(3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(5, 1)
        s2 = Square(1, 5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(5, 3, 3)
        s2 = Square(3, 3, 5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(1, Square(15, 22, 42, 1).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(21, 24, 23, 14, 15)

    def test_width_getter(self):
        s = Square(45, 1, 3, 12)
        s.size = 22
        self.assertEqual(22, s.width)

    def test_height_getter(self):
        s = Square(54, 15, 59, 25)
        s.size = 55
        self.assertEqual(55, s.height)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(2, 5, 2, 1).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 11, 21, 5).size)

    def test_size_setter(self):
        s = Square(2, 4, 3, 1)
        s.size = 6
        self.assertEqual(6, s.size)

    def test_x_getter(self):
        self.assertEqual(0, Square(5).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(5).y)


class TestSquare_size(unittest.TestCase):
    """testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("testing")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(3))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"testing": 5, "testing": 3}, 1)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 5, 13)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([15, 21, 23])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({51, 42, 13}, 42)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((14, 12, 53), 32, 23)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({11, 42, 53, 21}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(3))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'testing')

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'testing'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'testing'))

    # Test size values
    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5, 12)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 5)


class TestSquare_x(unittest.TestCase):
    """testing initialization of Square x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "testing")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, 1.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, complex(3))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {"testing": 21, "testing": 42}, 32)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, [4, 3, 1])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {5, 5, 5})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, (3, 6, 11))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, frozenset({5, 33, 1, 4}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(22, range(3))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, memoryview(b'testing'))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, b'testing')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, bytearray(b'testing'))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -4, 3)

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)


class TestSquare_y(unittest.TestCase):
    """testing initialization of Square y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, "testing")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, 1.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 4, complex(3))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, {"testing": 41, "testing": 32})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 2, [5, 1, 7])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, {3, 1, 6})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, (4, 1, 1))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 1, frozenset({5, 3, 1, 22}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 1, range(7))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 32, b'testing')

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 5, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 2, float('nan'))

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, bytearray(b'testing'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 32, memoryview(b'testing'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(6, 40, -3)


class TestSquare_order_of_initialization(unittest.TestCase):
    """testing order of Square attribute initialization."""

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("testing", "testing x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("testing", 3, "testing")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, "testing", "testing")


class TestSquare_area(unittest.TestCase):
    """testing the area method of the Square class."""

    def test_area_small(self):
        self.assertEqual(25, Square(5, 3, 3, 12).area())

    def test_area_large(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changed_attributes(self):
        s = Square(5, 20, 20, 11)
        s.size = 9
        self.assertEqual(81, s.area())

    def test_area_one_arg(self):
        s = Square(1, 5, 3, 4)
        with self.assertRaises(TypeError):
            s.area(5)


class TestSquare_stdout(unittest.TestCase):
    """testing __str__ and display methods of Square class."""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        s = Square(5)
        capture = TestSquare_stdout.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 5\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        s = Square(2, 2)
        correct = "[Square] ({}) 2/0 - 2".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_str_method_size_x_y(self):
        s = Square(2, 5, 11)
        correct = "[Square] ({}) 5/11 - 2".format(s.id)
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        s = Square(22, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 22", str(s))

    def test_str_method_changed_attributes(self):
        s = Square(2, 0, 0, [2])
        s.size = 66
        s.x = 3
        s.y = 6
        self.assertEqual("[Square] ([2]) 3/6 - 66", str(s))

    def test_str_method_one_arg(self):
        s = Square(2, 5, 1, 3)
        with self.assertRaises(TypeError):
            s.__str__(1)

    # Test display method
    def test_display_size(self):
        s = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        s = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        s = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        s = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquare_update_args(unittest.TestCase):
    """testing update args method of the Square class."""

    def test_update_args_zero(self):
        s = Square(5, 5, 5, 5)
        s.update()
        self.assertEqual("[Square] (5) 5/5 - 5", str(s))

    def test_update_args_one(self):
        s = Square(5, 5, 5, 5)
        s.update(2)
        self.assertEqual("[Square] (2) 5/5 - 5", str(s))

    def test_update_args_two(self):
        s = Square(5, 5, 5, 5)
        s.update(4, 12)
        self.assertEqual("[Square] (4) 5/5 - 12", str(s))

    def test_update_args_three(self):
        s = Square(5, 5, 5, 5)
        s.update(55, 22, 33)
        self.assertEqual("[Square] (55) 33/5 - 22", str(s))

    def test_update_args_four(self):
        s = Square(4, 4, 4, 4)
        s.update(1, 5, 22, 3)
        self.assertEqual("[Square] (1) 22/3 - 5", str(s))

    def test_update_args_more_than_four(self):
        s = Square(5, 5, 5, 5)
        s.update(2, 44, 22, 1, 7)
        self.assertEqual("[Square] (2) 22/1 - 44", str(s))

    def test_update_args_width_setter(self):
        s = Square(5, 5, 5, 5)
        s.update(22, 13)
        self.assertEqual(13, s.width)

    def test_update_args_height_setter(self):
        s = Square(1, 2, 3, 4)
        s.update(22, 5)
        self.assertEqual(5, s.height)

    def test_update_args_None_id(self):
        s = Square(5, 5, 5, 5)
        s.update(None)
        correct = "[Square] ({}) 5/5 - 5".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        s = Square(5, 5, 5, 5)
        s.update(None, 12, 7)
        correct = "[Square] ({}) 7/5 - 12".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        s = Square(4, 4, 5, 2)
        s.update(55, 22, 31, 411)
        s.update(1, 15, 1, 1)
        self.assertEqual("[Square] (1) 1/1 - 15", str(s))

    def test_update_args_invalid_size_type(self):
        s = Square(3, 44, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(22, "testing")

    def test_update_args_size_zero(self):
        s = Square(5, 5, 5, 55)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(22, 0)

    def test_update_args_size_negative(self):
        s = Square(2, 2, 2, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(11, -5)

    def test_update_args_invalid_x(self):
        s = Square(5, 5, 4, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(2, 3, "testing")

    def test_update_args_x_negative(self):
        s = Square(2, 5, 5, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(11, 21, -7)

    def test_update_args_invalid_y(self):
        s = Square(5, 4, 4, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(5, 4, 4, "testing")

    def test_update_args_y_negative(self):
        s = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(2, 4, 55, -5)

    def test_update_args_size_before_x(self):
        s = Square(22, 1, 11, 55)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(3, "testing", "testing")

    def test_update_args_size_before_y(self):
        s = Square(1, 55, 4, 33)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "testing", 2, "testing")

    def test_update_args_x_before_y(self):
        s = Square(5, 2, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(5, 15, "testing", "testing")


class TestSquare_update_kwargs(unittest.TestCase):
    """testing update kwargs method of Square class."""

    def test_update_kwargs_one(self):
        s = Square(5, 5, 5, 5)
        s.update(id=3)
        self.assertEqual("[Square] (3) 5/5 - 5", str(s))

    def test_update_kwargs_two(self):
        s = Square(5, 5, 5, 5)
        s.update(size=5, id=7)
        self.assertEqual("[Square] (7) 5/5 - 5", str(s))

    def test_update_kwargs_three(self):
        s = Square(5, 5, 5, 5)
        s.update(y=4, size=22, id=11)
        self.assertEqual("[Square] (11) 5/4 - 22", str(s))

    def test_update_kwargs_four(self):
        s = Square(4, 4, 4, 4)
        s.update(id=11, x=5, y=2, size=15)
        self.assertEqual("[Square] (11) 5/2 - 15", str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(4, 4, 4, 4)
        s.update(id=5, size=12)
        self.assertEqual(12, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(4, 4, 4, 4)
        s.update(id=3, size=5)
        self.assertEqual(5, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(5, 5, 5, 5)
        s.update(id=None)
        correct = "[Square] ({}) 5/5 - 5".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(4, 4, 4, 4)
        s.update(id=None, size=5, x=22)
        correct = "[Square] ({}) 22/4 - 5".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        s = Square(5, 5, 5, 5)
        s.update(id=22, x=1)
        s.update(y=11, x=4, size=5)
        self.assertEqual("[Square] (22) 4/11 - 5", str(s))

    def test_update_kwargs_invalid_size(self):
        s = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="testing")

    def test_update_kwargs_size_zero(self):
        s = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-4)

    def test_update_kwargs_invalid_x(self):
        s = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="testing")

    def test_update_kwargs_x_negative(self):
        s = Square(5, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-22)

    def test_update_kwargs_invalid_y(self):
        s = Square(4, 4, 5, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="testing")

    def test_update_kwargs_y_negative(self):
        s = Square(4, 4, 4, 4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-2)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(11, 4, y=10)
        self.assertEqual("[Square] (11) 10/10 - 4", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=3, id=11, a=1, b=54)
        self.assertEqual("[Square] (11) 10/10 - 3", str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
