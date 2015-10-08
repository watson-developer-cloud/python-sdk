# Questions

If you are having difficulties using the APIs or have a question about the IBM Watson Services,
please ask a question on [dW Answers][dw] or [Stack Overflow][stackoverflow].

# Issues

If you encounter an issue with the Python SDK, you are welcome to submit a [bug report](https://github.com/watson-developer-cloud/python-sdk/issues).
Before that, please search for similar issues. It's possible somebody has encountered this issue already.

## Pull Requests

If you want to contribute to the repository, here's a quick guide:
  1. Fork the repository
  2. develop and test your code changes with [pytest].
    * Respect the original code [style guide][styleguide].
    * Only use spaces for indentation.
    * Create minimal diffs - disable on save actions like reformat source code or organize imports. If you feel the source code should be reformatted create a separate PR for this change.
    * Check for unnecessary whitespace with git diff --check before committing.
  3. Make the test pass
  4. Commit your changes
  5. Push to your fork and submit a pull request to the `dev` branch

## Running the tests

You probably want to set up a [virtualenv].

 1. Clone this repository:
    ```
    git clone https://github.com/watson-developer-cloud/python-sdk.git
    ```
 2. Install the sdk as an editable package using the current source:
    ```
    pip install --editable .
    ```
 3. Install the test dependencies with:
```
pip install -r requirements-dev.txt
```
 4. Run the test cases with:
    ```
    py.test test
    ```

## Additional Resources
+ [General GitHub documentation](https://help.github.com/)
+ [GitHub pull request documentation](https://help.github.com/send-pull-requests/)

[dw]: https://developer.ibm.com/answers/questions/ask/?topics=watson
[stackoverflow]: http://stackoverflow.com/questions/ask?tags=ibm-watson
[styleguide]: http://google.github.io/styleguide/pyguide.html
[pytest]: http://pytest.org/latest/
[virtualenv]: http://virtualenv.readthedocs.org/en/latest/index.html
