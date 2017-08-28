# 1.5.0
- PEP8 specifies only methods need a surrounding blank line, therefore class arguments are allowed on the newline.

# 1.4.0
- Went from physical lines to logical lines, since classes with multiple line base classes do not need to be flagged.


# 1.2.1
- Fixed an issue where the line numbers of one file would bleed into the second file, therefore eventually producing errors on every line

# 1.2.0
- For simplicity, completely rewrote the line checker into a function
- Removed the docstrings configuration option previously added in 1.1.0, will add this again in the future.

# 1.1.0
- Added configuration setting to ignore docstrings on a newline

# 1.0.0
- Added new line checker