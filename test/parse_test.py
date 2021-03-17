import unittest

import valheimlog

from datetime import datetime

class TestParse(unittest.TestCase):
    def test_parse_character_line(self):
        input_line = "03/12/2021 12:54:37: Got character ZDOID from FartMeister : 1708501107:1"

        expected = (
            datetime(2021, 3, 12, 12, 54, 37),
            "FartMeister",
            1708501107,
            True
        )
        actual = valheimlog.parse(input_line)
        self.assertEqual(expected, actual)

    def test_parse_character_line_ws(self):
        input_line = "03/12/2021 12:54:37: Got character ZDOID from FartMeister : 1708501107:1\r\n"

        expected = (
            datetime(2021, 3, 12, 12, 54, 37),
            "FartMeister",
            1708501107,
            True
        )
        actual = valheimlog.parse(input_line)
        self.assertEqual(expected, actual)

    def test_parse_other_line(self):
        input_lines = ["03/12/2021 12:54:37: garbage other lines we don't care about",
                       "Unloading 0 unused Assets to reduce memory usage. Loaded Objects now: 1116798.",
                       "Unloading 0 Unused Serialized files (Serialized files now loaded: 0)",
                       "(Filename: ./Runtime/Export/Debug/Debug.bindings.h Line: 35)"
                       ]
        for line in input_lines:
            actual = valheimlog.parse(line)
            self.assertIsNone(actual)


if __name__ == "__main__":
    unittest.main()
