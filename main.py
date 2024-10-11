# suite_12_3.py
import unittest


# Декоратор для пропуска тестов
def skip_if_frozen(test):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print(f"Тесты в этом кейсе заморожены: {test.__name__}")
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return test(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        # Здесь идет логика теста
        self.assertTrue(True)

    @skip_if_frozen
    def test_run(self):
        # Здесь идет логика теста
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        # Здесь идет логика теста
        self.assertTrue(True)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Замороженные тесты

    @skip_if_frozen
    def test_first_tournament(self):
        # Здесь идет логика теста
        self.assertTrue(True)

    @skip_if_frozen
    def test_second_tournament(self):
        # Здесь идет логика теста
        self.assertTrue(True)

    @skip_if_frozen
    def test_third_tournament(self):
        # Здесь идет логика теста
        self.assertTrue(True)


if __name__ == "__main__":
    # Создаем тестовый набор
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)