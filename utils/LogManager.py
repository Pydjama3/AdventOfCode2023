from termcolor import colored


class LogManager:
    def __init__(self, answer_heading: str):
        self._log_answers = True
        self._log_checks = True
        self._log_tests = True
        self._log_errors = True
        self.head = answer_heading

    def heading(self):
        print(colored(self.head, color="light_grey"))

    def answer(self, *args, **kwargs):
        if self._log_answers:
            print(colored(self.stringify(*args, _sep=kwargs.get('_sep') if kwargs.get('_sep') else " "), color="green"), **kwargs)

    def check(self, prompt=None):
        if self._log_checks:
            return input(colored(prompt if prompt else "", color="yellow"))

    def test_log(self, *args, **kwargs):
        if self._log_tests:
            print(colored(self.stringify(*args, _sep=kwargs.get('_sep') if kwargs.get('_sep') else " "), color="blue"), **kwargs)

    def error(self, *args, **kwargs):
        if self._log_errors:
            print(colored(self.stringify(*args, _sep=kwargs.get('_sep') if kwargs.get('_sep') else " "), color="red"), **kwargs)

    @staticmethod
    def stringify(*args, _sep=" "):
        return _sep.join([str(arg) for arg in args])

    @property
    def answers(self):
        return self._log_answers

    @answers.setter
    def answers(self, value):
        self._log_answers = value

    @property
    def checks(self):
        return self._log_checks

    @checks.setter
    def checks(self, value):
        self._log_checks = value

    @property
    def tests(self):
        return self._log_tests

    @tests.setter
    def tests(self, value):
        self._log_tests = value

    @property
    def errors(self):
        return self._log_errors

    @errors.setter
    def errors(self, value):
        self._log_errors = value
