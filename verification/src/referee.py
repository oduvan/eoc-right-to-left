from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "left_join"
    FUNCTION_NAMES = {
        "python_3": "left_join",
        "js_node": "leftJoin"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: '''def cover(func, data):
    return func(tuple(data))
'''
    }