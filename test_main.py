
#!/usr/bin/env python3
"""Comprehensive tests for Todo Console App."""

import pytest
from io import StringIO
from unittest.mock import patch, MagicMock
import main


class TestGenerateNextId:
    """Tests for _generate_next_id function."""

    def test_generate_id_empty_list(self):
        """Test ID generation with empty list."""
        result = main._generate_next_id([])
        assert result == 1

    def test_generate_id_one_task(self):
        """Test ID generation with one task."""
        tasks = [{'id': 1, 'title': 'Task 1', 'description': None, 'completed': False}]
        result = main._generate_next_id(tasks)
        assert result == 2

    def test_generate_id_multiple_tasks(self):
        """Test ID generation with multiple tasks."""
        tasks = [
            {'id': 1, 'title': 'Task 1', 'description': None, 'completed': False},
            {'id': 2, 'title': 'Task 2', 'description': None, 'completed': False},
            {'id': 3, 'title': 'Task 3', 'description': None, 'completed': False},
        ]
        result = main._generate_next_id(tasks)
        assert result == 4

    def test_generate_id_after_deletion(self):
        """Test ID generation after deleting tasks (gap in IDs)."""
        tasks = [
            {'id': 1, 'title': 'Task 1', 'description': None, 'completed': False},
            {'id': 5, 'title': 'Task 5', 'description': None, 'completed': False},
        ]
        result = main._generate_next_id(tasks)
        assert result == 6


class TestViewTasks:
    """Tests for view_tasks function."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_empty_tasks(self, mock_stdout):
        """Test viewing empty task list."""
        main.view_tasks([])
        assert "No tasks yet." in mock_stdout.getvalue()

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_single_task(self, mock_stdout):
        """Test viewing single task."""
        tasks = [{'id': 1, 'title': 'Task 1', 'description': 'Description', 'completed': False}]
        main.view_tasks(tasks)
        output = mock_stdout.getvalue()
        assert "Task 1" in output
        assert "[ ]" in output
        assert "Description" in output

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_completed_task(self, mock_stdout):
        """Test viewing completed task shows [✓] icon."""
        tasks = [{'id': 1, 'title': 'Task 1', 'description': None, 'completed': True}]
        main.view_tasks(tasks)
        output = mock_stdout.getvalue()
        assert "[✓]" in output

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_multiple_tasks(self, mock_stdout):
        """Test viewing multiple tasks."""
        tasks = [
            {'id': 1, 'title': 'Task 1', 'description': 'Desc 1', 'completed': True},
            {'id': 2, 'title': 'Task 2', 'description': None, 'completed': False},
            {'id': 3, 'title': 'Task 3', 'description': 'Desc 3', 'completed': False},
        ]
        main.view_tasks(tasks)
        output = mock_stdout.getvalue()
        assert "Task 1" in output
        assert "Task 2" in output
        assert "Task 3" in output
        assert output.count("[✓]") == 1
        assert output.count("[ ]") == 2

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_table_format(self, mock_stdout):
        """Test that view_tasks outputs table-like format with headers."""
        tasks = [{'id': 1, 'title': 'Task', 'description': None, 'completed': False}]
        main.view_tasks(tasks)
        output = mock_stdout.getvalue()
        assert "ID" in output
        assert "Title" in output
        assert "Status" in output
        assert "---" in output


class TestAddTask:
    """Tests for add_task function."""

    @patch('builtins.input', side_effect=['Buy groceries', 'Milk, eggs'])
    def test_add_task_with_description(self, mock_input):
        """Test adding a task with description."""
        tasks = []
        main.add_task(tasks)
        assert len(tasks) == 1
        assert tasks[0]['title'] == 'Buy groceries'
        assert tasks[0]['description'] == 'Milk, eggs'
        assert tasks[0]['completed'] is False
        assert tasks[0]['id'] == 1

    @patch('builtins.input', side_effect=['Buy groceries', ''])
    def test_add_task_without_description(self, mock_input):
        """Test adding a task without description."""
        tasks = []
        main.add_task(tasks)
        assert len(tasks) == 1
        assert tasks[0]['title'] == 'Buy groceries'
        assert tasks[0]['description'] is None

    @patch('builtins.input', side_effect=['Buy groceries', ''])
    def test_add_task_generates_unique_id(self, mock_input):
        """Test that each task gets a unique ID."""
        tasks = [{'id': 1, 'title': 'Existing', 'description': None, 'completed': False}]
        main.add_task(tasks)
        assert len(tasks) == 2
        assert tasks[1]['id'] == 2

    @patch('builtins.input', side_effect=['', 'Description'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task_empty_title_rejected(self, mock_stdout, mock_input):
        """Test that empty title is rejected."""
        tasks = []
        main.add_task(tasks)
        assert len(tasks) == 0
        assert "Title is required." in mock_stdout.getvalue()

    @patch('builtins.input', side_effect=['  ', 'Description'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task_whitespace_title_rejected(self, mock_stdout, mock_input):
        """Test that whitespace-only title is rejected."""
        tasks = []
        main.add_task(tasks)
        assert len(tasks) == 0
        assert "Title is required." in mock_stdout.getvalue()

    @patch('builtins.input', side_effect=['A' * 201, 'Description'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task_title_too_long_rejected(self, mock_stdout, mock_input):
        """Test that title longer than 200 characters is rejected."""
        tasks = []
        main.add_task(tasks)
        assert len(tasks) == 0
        assert "Title too long (max 200 characters)." in mock_stdout.getvalue()

    @patch('builtins.input', side_effect=['A' * 200, 'Description'])
    def test_add_task_title_max_length_accepted(self, mock_input):
        """Test that title exactly 200 characters is accepted."""
        tasks = []
        main.add_task(tasks)
        assert len(tasks) == 1
        assert len(tasks[0]['title']) == 200

    @patch('builtins.input', side_effect=['  Trimmed  ', '  Description  '])
    def test_add_task_strips_whitespace(self, mock_input):
        """Test that leading/trailing whitespace is stripped from inputs."""
        tasks = []
        main.add_task(tasks)
        assert len(tasks) == 1
        assert tasks[0]['title'] == 'Trimmed'
        assert tasks[0]['description'] == 'Description'

    @patch('builtins.input', side_effect=['Test Task', 'Test Description'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task_displays_confirmation(self, mock_stdout, mock_input):
        """Test that add_task displays confirmation message."""
        tasks = []
        main.add_task(tasks)
        output = mock_stdout.getvalue()
        assert "Task 'Test Task' added with ID 1." in output


class TestFindTaskById:
    """Tests for _find_task_by_id function."""

    def test_find_task_by_id_found(self):
        """Test finding an existing task by ID."""
        tasks = [
            {'id': 1, 'title': 'Task 1', 'description': None, 'completed': False},
            {'id': 2, 'title': 'Task 2', 'description': None, 'completed': False},
        ]
        result = main._find_task_by_id(tasks, 2)
        assert result is not None
        assert result['id'] == 2
        assert result['title'] == 'Task 2'

    def test_find_task_by_id_not_found(self):
        """Test finding a non-existent task by ID."""
        tasks = [
            {'id': 1, 'title': 'Task 1', 'description': None, 'completed': False},
        ]
        result = main._find_task_by_id(tasks, 99)
        assert result is None

    def test_find_task_by_id_empty_list(self):
        """Test finding a task in an empty list."""
        result = main._find_task_by_id([], 1)
        assert result is None


class TestToggleComplete:
    """Tests for toggle_complete function."""

    @patch('builtins.input', return_value='1')
    def test_toggle_complete_to_completed(self, mock_input):
        """Test toggling a task from incomplete to completed."""
        tasks = [{'id': 1, 'title': 'Task 1', 'description': None, 'completed': False}]
        main.toggle_complete(tasks)
        assert tasks[0]['completed'] is True

    @patch('builtins.input', return_value='1')
    def test_toggle_complete_to_incomplete(self, mock_input):
        """Test toggling a task from completed to incomplete."""
        tasks = [{'id': 1, 'title': 'Task 1', 'description': None, 'completed': True}]
        main.toggle_complete(tasks)
        assert tasks[0]['completed'] is False

    @patch('builtins.input', return_value='abc')
    @patch('sys.stdout', new_callable=StringIO)
    def test_toggle_complete_invalid_id_non_numeric(self, mock_stdout, mock_input):
        """Test toggle complete with non-numeric ID."""
        tasks = [{'id': 1, 'title': 'Task 1', 'description': None, 'completed': False}]
        main.toggle_complete(tasks)
        assert tasks[0]['completed'] is False  # Should not change
        assert "Invalid ID. Please enter a number." in mock_stdout.getvalue()

    @patch('builtins.input', return_value='99')
    @patch('sys.stdout', new_callable=StringIO)
    def test_toggle_complete_task_not_found(self, mock_stdout, mock_input):
        """Test toggle complete with non-existent task ID."""
        tasks = [{'id': 1, 'title': 'Task 1', 'description': None, 'completed': False}]
        main.toggle_complete(tasks)
        assert tasks[0]['completed'] is False  # Should not change
        assert "Task 99 not found." in mock_stdout.getvalue()

    @patch('builtins.input', return_value='2')
    def test_toggle_complete_correct_task(self, mock_input):
        """Test that toggle complete only affects the specified task."""
        tasks = [
            {'id': 1, 'title': 'Task 1', 'description': None, 'completed': False},
            {'id': 2, 'title': 'Task 2', 'description': None, 'completed': False},
            {'id': 3, 'title': 'Task 3', 'description': None, 'completed': False},
        ]
        main.toggle_complete(tasks)
        assert tasks[0]['completed'] is False
        assert tasks[1]['completed'] is True
        assert tasks[2]['completed'] is False

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=StringIO)
    def test_toggle_complete_displays_confirmation_completed(self, mock_stdout, mock_input):
        """Test that toggle complete displays confirmation when marking as completed."""
        tasks = [{'id': 1, 'title': 'Task 1', 'description': None, 'completed': False}]
        main.toggle_complete(tasks)
        output = mock_stdout.getvalue()
        assert "Task 1 marked as completed." in output

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=StringIO)
    def test_toggle_complete_displays_confirmation_incomplete(self, mock_stdout, mock_input):
        """Test that toggle complete displays confirmation when marking as incomplete."""
        tasks = [{'id': 1, 'title': 'Task 1', 'description': None, 'completed': True}]
        main.toggle_complete(tasks)
        output = mock_stdout.getvalue()
        assert "Task 1 marked as incomplete." in output

    @patch('builtins.input', return_value='  2  ')
    def test_toggle_complete_strips_whitespace(self, mock_input):
        """Test that toggle complete strips whitespace from ID input."""
        tasks = [
            {'id': 1, 'title': 'Task 1', 'description': None, 'completed': False},
            {'id': 2, 'title': 'Task 2', 'description': None, 'completed': False},
        ]
        main.toggle_complete(tasks)
        assert tasks[0]['completed'] is False
        assert tasks[1]['completed'] is True


class TestGetMenuChoice:
    """Tests for _get_menu_choice function."""

    @patch('builtins.input', return_value='1\n')
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_menu_choice_valid(self, mock_stdout, mock_input):
        """Test getting a valid menu choice."""
        result = main._get_menu_choice()
        assert result == 1

    @patch('builtins.input', return_value='0\n')
    def test_get_menu_choice_zero(self, mock_input):
        """Test getting menu choice 0."""
        result = main._get_menu_choice()
        assert result == 0

    @patch('builtins.input', return_value='5\n')
    def test_get_menu_choice_max(self, mock_input):
        """Test getting menu choice 5."""
        result = main._get_menu_choice()
        assert result == 5

    @patch('builtins.input', return_value='abc\n')
    def test_get_menu_choice_invalid_text(self, mock_input):
        """Test getting invalid menu choice (text)."""
        result = main._get_menu_choice()
        assert result is None

    @patch('builtins.input', return_value='3.5\n')
    def test_get_menu_choice_invalid_float(self, mock_input):
        """Test getting invalid menu choice (float)."""
        result = main._get_menu_choice()
        assert result is None


class TestMainFunction:
    """Tests for main() function."""

    @patch('builtins.input', return_value='0')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_exit_on_zero(self, mock_stdout, mock_input):
        """Test that main exits when user enters 0."""
        main.main()
        output = mock_stdout.getvalue()
        assert "Goodbye!" in output

    @patch('builtins.input', side_effect=['2', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_view_tasks_option(self, mock_stdout, mock_input):
        """Test main with view tasks option."""
        main.tasks = [
            {'id': 1, 'title': 'Test Task', 'description': None, 'completed': False}
        ]
        main.main()
        output = mock_stdout.getvalue()
        assert "Test Task" in output

    @patch('builtins.input', side_effect=['1', 'New Task', 'Description', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_add_task_option(self, mock_stdout, mock_input):
        """Test main with add task option."""
        main.tasks = []
        main.main()
        assert len(main.tasks) == 1
        assert main.tasks[0]['title'] == 'New Task'

    @patch('builtins.input', side_effect=['4', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_not_implemented_option(self, mock_stdout, mock_input):
        """Test main with not yet implemented options."""
        main.main()
        output = mock_stdout.getvalue()
        assert "Feature not yet implemented." in output

    @patch('builtins.input', side_effect=['invalid', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_invalid_choice_error(self, mock_stdout, mock_input):
        """Test main displays error for invalid menu choice."""
        main.main()
        output = mock_stdout.getvalue()
        assert "Invalid choice. Please enter 0-5." in output

    @patch('builtins.input', side_effect=['2', '2', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_continues_loop(self, mock_stdout, mock_input):
        """Test that main continues loop after option."""
        main.tasks = []
        main.main()
        output = mock_stdout.getvalue()
        assert output.count("=== Todo Console App ===") > 1


class TestIntegration:
    """Integration tests for complete workflows."""

    @patch('builtins.input', side_effect=['1', 'Task 1', '', '1', 'Task 2', 'Desc 2', '2', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_two_tasks_and_view(self, mock_stdout, mock_input):
        """Test adding two tasks and viewing them."""
        main.tasks = []
        main.main()
        output = mock_stdout.getvalue()
        assert len(main.tasks) == 2
        assert main.tasks[0]['title'] == 'Task 1'
        assert main.tasks[1]['title'] == 'Task 2'
        assert 'Task 1' in output
        assert 'Task 2' in output

    @patch('builtins.input', side_effect=['1', '', 'description', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_title_flow(self, mock_stdout, mock_input):
        """Test flow when user enters empty title."""
        main.tasks = []
        main.main()
        assert len(main.tasks) == 0
        assert "Title is required." in mock_stdout.getvalue()

    @patch('builtins.input', side_effect=['1', 'Task 1', '', '1', 'Task 2', '', '1', 'Task 3', '', '2', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiple_tasks_unique_ids(self, mock_stdout, mock_input):
        """Test that multiple tasks have unique IDs."""
        main.tasks = []
        main.main()
        assert len(main.tasks) == 3
        ids = [task['id'] for task in main.tasks]
        assert ids == [1, 2, 3]
        assert len(set(ids)) == 3
