import sys
import unittest

import Framework
import AllTests


def main(argv):
    if "--record" in argv:
        Framework.activateRecordMode()
        argv = [arg for arg in argv if arg != "--record"]

    unittest.main(module=AllTests, argv=argv)


if __name__ == "__main__":
    main(sys.argv)
