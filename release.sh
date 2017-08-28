#!/usr/bin/env bash
# Exit on first error
set -e

# Parse our CLI arguments
version_number="$1"
if test "$version_number" = ""; then
  echo "Expected a version to be provided to \`release.sh\` but none was provided." 1>&2
  echo "Usage: $0 [version] # (e.g. $0 1.0.0)" 1>&2
  exit 1
fi

# Bump the version
echo "__version__ = '$version_number'" > flake8_class_newline/__version__.py

# Verify our version made it into the file
if ! grep "$version_number" flake8_class_newline/__version__.py &> /dev/null; then
  echo "Expected \`__version__\` to update via \`sed\` but it didn't" 1>&2
  exit 1
fi

# Commit the change
git add flake8_class_newline/__version__.py
git commit -a -m "Release $version_number"

# Tag the release
git tag "$version_number"

# Publish the release to GitHub
git push
git push --tags
