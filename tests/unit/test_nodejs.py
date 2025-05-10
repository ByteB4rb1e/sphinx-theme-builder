import re
import unittest.mock

import pytest

from sphinx_theme_builder._internal.nodejs import require_cmd_semver


class Test_match_cmd_semver:

    def test_default(self):
        """"""
        with unittest.mock.patch(
            "subprocess.check_output",
            return_value = b"v18.19.3"
        ) as check_output_mock:
            require_cmd_semver(
                version = (18, 19, 1),
                command = ["foobar", "--version"]
            )

    def test_not_semver_output(self):
        """"""
        with unittest.mock.patch(
            "subprocess.check_output",
            return_value = b"foobar"
        ) as check_output_mock:

            with pytest.raises(Exception) as e:
                require_cmd_semver(
                    version = (1, 0, 0),
                    command = ["foobar", "--version"]
                )

            assert e.match('supplied pattern did not match on command')

    def test_not_semver_pattern(self):
        """"""
        with unittest.mock.patch(
            "subprocess.check_output",
            return_value = b"v1.0.0.0"
        ) as check_output_mock:

            with pytest.raises(Exception) as e:
                require_cmd_semver(
                    version = (1, 0, 0),
                    command = ["foobar", "--version"],
                    pattern = re.compile(r'v([0-9]+).([0-9]+).([0-9]+).([0-9]+)'),
                )

            assert e.match('supplied pattern did not supply amount')

    def test_major_mismatch(self):
        """"""
        with unittest.mock.patch(
            "subprocess.check_output",
            return_value = b"v0.0.0"
        ) as check_output_mock:

            with pytest.raises(Exception) as e:
                require_cmd_semver(
                    version = (1, 0, 0),
                    command = ["foobar", "--version"]
                )

            assert e.match('v0.0.0 < v1.0.0')

    def test_minor_mismatch(self):
        """"""
        with unittest.mock.patch(
            "subprocess.check_output",
            return_value = b"v1.0.0"
        ) as check_output_mock:

            with pytest.raises(Exception) as e:
                require_cmd_semver(
                    version = (1, 1, 0),
                    command = ["foobar", "--version"]
                )

            assert e.match('v1.0.0 < v1.1.0')

    def test_patch_mismatch(self):
        """"""
        with unittest.mock.patch(
            "subprocess.check_output",
            return_value = b"v1.1.0"
        ) as check_output_mock:

            with pytest.raises(Exception) as e:
                require_cmd_semver(
                    version = (1, 1, 1),
                    command = ["foobar", "--version"]
                )

            assert e.match('v1.1.0 < v1.1.1')
