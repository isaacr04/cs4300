# Homework 1 - Isaac Rodriguez

## Install Dependencies

For running test files and demonstrating packages in task7,
install `pytest`, `requests`, and `bs4`
    
```
pip install pytest requests bs4
```

Task 7 uses `requests` and `bs4` to GET request an example website
and print the first `<p>` block as plain text.

## Running Tests

The pyproject.toml file provides all the settings for pytest.
To run, make sure you are in the homework1 directory
```
cd homework1
```

and simply run
```
pytest
```

to view the results of the tests.