#!/bin/bash

echo "🔍 Checking for tracked files that match patterns in .gitignore..."

# Ensure we are in a git repo
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "❌ This is not a Git repository. Please run this script in the root of a Git repo."
    exit 1
fi

# Get all tracked files that should be ignored
IGNORED=$(git ls-files -z | git check-ignore --stdin -z)

if [ -z "$IGNORED" ]; then
    echo "✅ No tracked files match .gitignore. Repository is clean."
    exit 0
fi

echo "⚠️ The following tracked files should be ignored and will be removed from Git tracking:"
echo "$IGNORED" | tr '\0' '\n'

# Remove from Git index
echo "🚮 Removing files from Git index..."
echo "$IGNORED" | xargs -0 git rm --cached

# Create commit
echo "📝 Committing removal..."
git commit -m "Remove tracked files that match .gitignore patterns"

# Push to remote
echo "📤 Pushing to origin..."
git push origin HEAD

echo "✅ Cleanup complete."
