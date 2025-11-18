from pathlib import Path

def test_template_has_readme():
    """Test that template contains README"""
    readme = Path("analysis/_template/README.md")
    assert readme.exists()

    content = readme.read_text()
    assert "Analysis Session" in content
    assert "Data Sources" in content

def test_template_has_metadata():
    """Test that template includes metadata file"""
    metadata = Path("analysis/_template/00 - overview.md")
    assert metadata.exists()

    content = metadata.read_text()
    assert "# Analysis Overview" in content
    assert "## Analytical Goal" in content

def test_template_has_query_template():
    """Test that template includes query template helper"""
    query_template = Path("analysis/_template/.query-template.md")
    assert query_template.exists()

    content = query_template.read_text()
    assert "## Rationale" in content
    assert "## Query" in content
    assert "## Results" in content
    assert "## Interpretation" in content
