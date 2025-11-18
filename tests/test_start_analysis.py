import subprocess
from pathlib import Path
from datetime import datetime
import shutil

def test_start_analysis_creates_directory():
    """Test that start-analysis creates correct directory structure"""
    # Setup: clean any existing test analysis
    test_dir = Path("analysis/hypothesis-testing")
    if test_dir.exists():
        shutil.rmtree(test_dir)

    # Execute
    result = subprocess.run(
        ["just", "start-analysis", "hypothesis-testing", "test-analysis"],
        capture_output=True,
        text=True
    )

    # Verify directory created with date
    today = datetime.now().strftime("%Y-%m-%d")
    expected_dir = Path(f"analysis/hypothesis-testing/{today}-test-analysis")
    assert expected_dir.exists()

    # Verify template files were copied
    assert (expected_dir / "README.md").exists()
    assert (expected_dir / "00 - overview.md").exists()
    assert (expected_dir / ".query-template.md").exists()

def test_start_analysis_prevents_duplicates():
    """Test that start-analysis handles existing directories"""
    # Create an existing analysis directory
    today = datetime.now().strftime("%Y-%m-%d")
    existing_dir = Path(f"analysis/hypothesis-testing/{today}-duplicate-test")
    existing_dir.mkdir(parents=True, exist_ok=True)

    # Execute - should prompt or error
    result = subprocess.run(
        ["just", "start-analysis", "hypothesis-testing", "duplicate-test"],
        capture_output=True,
        text=True,
        input="n\n"  # Answer 'no' to overwrite prompt
    )

    # Verify it didn't silently overwrite
    assert "already exists" in result.stdout or result.returncode != 0
