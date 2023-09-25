

How to contribute
=================

You noticed an incorrect stub and want to fix it ? Here is how you can do that.

Note that there are two ways. One where you recreate a whole stub testing environment and ensure that your fix
works fine. The second where you rely on the CI for the testing environment.

The CI way
----------

This is the easiest/quickest way in terms of setup.

1. Create a fork of `pyside2-stubs`


2. Clone your forked repo of `pyside2-stubs`


3. Add test showing the incorrect stub. For example, I noticed that `QAction.setShortcut()` was declared to support
   only `QKeySequence` whereas a simple string is also supported.

   So I created a new file `tests\qaction.py` using the correct code usage, but detected incorrectly by mypy:

        from PySide2.QtWidgets import QAction

        a = QAction()
        a.setShortcut('Ctrl+F')


4. Fix the PySide2 stubs. In my case, I changed the signature of `QAction.setShortcut()`

   from:


        def setShortcut(a: QKeySequence) -> None: ...
   
   to:

        def setShortcut(a: typing.Union[QKeySequence, str]) -> None: ...


5. Commit the change and push it to your repo.


6. Create a pull request against `pyside2-stubs`. The PR will run the CI for your change and ensure that all tests continue
   to pass successfully. I'll be happy to merge the result.




The manual way
--------------

Here, you take all the steps to reproduce a complete stub testing environment to include your change.

1. Create a fork of `pyside2-stubs`

2. Clone your forked repo of `pyside2-stubs`

3. Create a virtual environment (I used `.env` as a name for my virtual environment) and activate it.


        python -m venv .env  
        .env\scripts\activate


4. Install the required packages for running the tests.

        python -m pip install -r dev-requirements.txt

    Note: running pip as a python module is necessary because `dev-requirements.txt` modify pip itself.
          This can be confirmed by trying to run `pip install -r dev-requirements.txt`

5. Make your current directory an editable installed package.


        pip install -e . --config-settings editable_mode=strict

   Note: the `editable_mode` option is required for Mypy to pick up the editable installation as of recent versions of setuptools.
         See https://github.com/python/mypy/issues/13392.


6. Make sure the tests run correctly as they are:

        $ pytest -v
        [...]
        ================================================= 60 passed in 13.07s =================================================
        $

    There should be no failure reported.

   
7. Add test showing the incorrect stub definitions. For example, I noticed that `QAction.setShortcut()` was declared to support
   only `QKeySequence` whereas a simple string is also supported.

   So I created a new file `tests\qaction.py` using the correct code usage, but detected incorrectly by mypy:

        from PySide2.QtWidgets import QAction

        a = QAction()
        a.setShortcut('Ctrl+F')


8. Run the tests again. Your new file should be picked up and reported as an error by the mypy test.


        (.env2) c:\oss\PyQt-stubs\PySide2-stubs>pytest -v
        ================================================= test session starts =================================================
        platform win32 -- Python 3.10.2, pytest-7.1.3, pluggy-1.0.0 -- c:\oss\PyQt-stubs\PySide2-stubs\.env2\Scripts\python.exe
        cachedir: .pytest_cache
        rootdir: c:\oss\PyQt-stubs\PySide2-stubs
        collected 60 items

        tests/test_examples_here.py::test_examples_with_mypy[qaction.py] FAILED                                          [  1%]
        tests/test_examples_here.py::test_examples_with_mypy[qapplication.py] PASSED                                     [  3%]
        [...]
        tests/test_examples_here.py::test_examples_execution[signal_slot.py] PASSED                                      [ 98%]
        tests/test_examples_here.py::test_examples_execution[slot.py] PASSED                                             [100%]

        ====================================================== FAILURES =======================================================
        _________________________________________ test_examples_with_mypy[qaction.py] _________________________________________

        filepath = WindowsPath('c:/oss/PyQt-stubs/PySide2-stubs/tests/qaction.py')

            @pytest.mark.parametrize(
                "filepath",
                list(gen_file_list()),
                ids=[v.relative_to(TESTS_DIR).as_posix() for v in gen_file_list()],
            )
            def test_examples_with_mypy(filepath: Path) -> None:
                """Run mypy over example files."""
                stdout, stderr, exitcode = api.run([os.fspath(filepath)] + ['--show-error-codes'])
                if stdout:
                    print(stdout)
                if stderr:
                    print(stderr)

        >       assert stdout.startswith("Success: no issues found")
        E       assert False
        E        +  where False = <built-in method startswith of str object at 0x00000188704F6D30>('Success: no issues found')
        E        +    where <built-in method startswith of str object at 0x00000188704F6D30> = 'tests\\qaction.py:4: error: Argument 1 to "setShortcut" of "QAction" has incompatible type "int"; expected "Union[QKeySequence, str]"  [arg-type]\nFound 1 error in 1 file (checked 1 source file)\n'.startswith

        tests\test_examples_here.py:42: AssertionError
        ------------------------------------------------ Captured stdout call -------------------------------------------------
        tests\qaction.py:4: error: Argument 1 to "setShortcut" of "QAction" has incompatible type "str"; expected "QKeySequence"  [arg-type]
        Found 1 error in 1 file (checked 1 source file)

        =============================================== short test summary info ===============================================
        FAILED tests/test_examples_here.py::test_examples_with_mypy[qaction.py] - assert False
        ============================================ 1 failed, 59 passed in 8.82s =============================================

        (.env2) c:\oss\PyQt-stubs\PySide2-stubs>


    Note that you can run your new test only by using: `pytest -k "your test name" -v`


9. Fix the PySide2 stubs. In my case, I changed the signature of `QAction.setShortcut()` 

   from:

       def setShortcut(a: QKeySequence) -> None: ...

   to:

       def setShortcut(a: typing.Union[QKeySequence, str]) -> None: ...


10. Rerun the tests. If it looks like mypy is still using the old stubs, delete `.mypy-cache` . It helps.
   You should now see no error, but two more tests successful.

        $ pytest -v
        [...]
        ================================================= 62 passed in 13.07s =================================================
        $

11. Commit your changes and push them to your repository.

12. Create a pull request. I'll be glad to merge it. The CI will run basically the same tests that you did over your changes.
