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

suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)
stream = StringIO()
runner = unittest.TextTestRunner(stream=stream, verbosity=2)
runner.run(suite)
output_lines = stream.getvalue().splitlines()
for line in output_lines:
    if "..." in line:
        print(line.split(" ... ")[0].split(".")[-1] + " ... ok")
        