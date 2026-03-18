import unittest
from io import StringIO
from todo import Task, TaskPool

class TestTaskPool(unittest.TestCase):

    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("Test Task")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        self.assertIn("Update Login UI", [t.title for t in open_tasks])

    def test_get_done_tasks(self):
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        self.assertIn("Add Login UI", [t.title for t in done_tasks])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)
    captured_output = StringIO()
    result = unittest.TextTestRunner(stream=captured_output, verbosity=2).run(suite)
    output_lines = captured_output.getvalue().splitlines()
    for line in output_lines:
        if "ok" in line:
            print(line.split(' ')[0] + ' ... ok')
    total_tests = result.testsRun
    failed_tests = [t[0] for t in result.failures + result.errors]
    passed_tests = [test for test in suite if test not in failed_tests]
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {len(passed_tests)} ({(len(passed_tests) / total_tests * 100):.2f}%)")
    print(f"Failed: {len(failed_tests)} ({(len(failed_tests) / total_tests * 100):.2f}%)")