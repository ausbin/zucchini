from .exceptions import InvalidGraderConfigError
from .grader_interface import GraderInterface, Part
from .threaded_grader import ThreadedGrader
from .prompt_grader import PromptGrader
from .open_file_grader import OpenFileGrader
from .libcheck_grader import LibcheckGrader
from .junit_json_grader import JUnitJSONGrader

__all__ = ['InvalidGraderConfigError', 'GraderInterface', 'Part',
           'ThreadedGrader', 'PromptGrader', 'OpenFileGrader',
           'LibcheckGrader', 'JUnitJSONGrader']

_GRADERS = (
    PromptGrader,
    OpenFileGrader,
    LibcheckGrader,
    JUnitJSONGrader,
)
AVAILABLE_GRADERS = {cls.__name__: cls for cls in _GRADERS}
