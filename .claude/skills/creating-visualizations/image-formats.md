# Image-Based Visualization Formats with Kroki

This document provides guidance for creating image-based diagrams and visualizations using Kroki, complementing the terminal-based visualizations described in `terminal-formats.md`.

---

## When to Use Image-Based Visualizations

**Use image formats (Kroki) when:**
- Creating diagrams that need to be embedded in reports/presentations
- Visualizing complex relationships, hierarchies, or networks
- Documenting data lineage, schemas, or workflows
- Creating flowcharts, entity-relationship diagrams, or architecture diagrams
- Output will be viewed outside the terminal (web, PDF, documentation)

**Use terminal formats (plotext, etc.) when:**
- Working interactively in terminal/Jupyter notebooks
- Quick data exploration and analysis
- Output stays in markdown documentation
- Fast iteration without external dependencies

---

## What is Kroki?

**Kroki** is a unified diagram generation API that creates diagrams from textual descriptions. It supports 25+ diagram formats through a single HTTP interface.

**Key Features:**
- **Free & Open Source** (MIT licensed)
- **No installation required** for individual diagram tools
- **Multiple output formats**: SVG, PNG, PDF
- **Public service** (kroki.io) or **self-hosted** (Docker)
- **Simple HTTP API** - Generate diagrams via GET or POST requests

### How Kroki Works

```
Text Description → HTTP Request → Kroki API → Rendered Diagram (SVG/PNG/PDF)
```

**Example workflow:**
1. Write diagram description in format-specific syntax (Mermaid, GraphViz, etc.)
2. Send to Kroki via HTTP (GET with URL encoding or POST with plain text)
3. Receive rendered diagram as image
4. Embed in documentation or save to file

---

## Supported Data Visualization Formats

Kroki supports 25+ formats. For **data analysis and visualization**, these are most relevant:

| Format | Best For | Use Cases | Guide |
|--------|----------|-----------|-------|
| **Vega-Lite** | Statistical charts | Bar charts, line plots, scatter plots, distributions | [formats/vega-lite.md](./formats/vega-lite.md) |
| **Mermaid** | Flowcharts, timelines | Data workflows, Gantt charts, sequence diagrams | [formats/mermaid.md](./formats/mermaid.md) |
| **GraphViz (DOT)** | Network graphs | Data lineage, relationships, hierarchies | [formats/graphviz.md](./formats/graphviz.md) |
| **D2** | Modern diagrams | Architecture, data models, SQL tables | [formats/d2.md](./formats/d2.md) |
| **ERD** | Database schemas | Entity-relationship diagrams | [formats/erd.md](./formats/erd.md) |
| **DBML** | Database docs | Complete database documentation with details | [formats/dbml.md](./formats/dbml.md) |

**Quick Selector:**
- **Charts/plots** → Vega-Lite
- **Workflows/processes** → Mermaid
- **Relationships/networks** → GraphViz
- **Data models** → D2 or ERD
- **Database schemas** → ERD or DBML

---

## Quick Start

### Using Kroki Public Service

**Generate diagram via Python:**

```python
import requests
import base64
import zlib

def generate_diagram(diagram_text, diagram_type='mermaid', output_format='svg'):
    """Generate diagram using Kroki public API."""

    # Compress and encode (for GET requests)
    compressed = zlib.compress(diagram_text.encode('utf-8'), 9)
    encoded = base64.urlsafe_b64encode(compressed).decode('ascii')

    # Kroki endpoint
    url = f"https://kroki.io/{diagram_type}/{output_format}/{encoded}"

    response = requests.get(url)
    return response.content

# Example: Simple Mermaid flowchart
diagram = """
graph TD
    A[Raw Data] --> B[Clean Data]
    B --> C[Analysis]
    C --> D[Report]
"""

svg_output = generate_diagram(diagram, 'mermaid', 'svg')

# Save to file
with open('workflow.svg', 'wb') as f:
    f.write(svg_output)
```

### Alternative: POST Request (Simpler)

```python
import requests

def generate_diagram_post(diagram_text, diagram_type='mermaid', output_format='svg'):
    """Generate diagram using POST (no encoding needed)."""

    url = f"https://kroki.io/{diagram_type}/{output_format}"

    response = requests.post(url, data=diagram_text.encode('utf-8'))
    return response.content

# Same example
diagram = """
graph TD
    A[Raw Data] --> B[Clean Data]
    B --> C[Analysis]
    C --> D[Report]
"""

svg_output = generate_diagram_post(diagram, 'mermaid', 'svg')
```

---

## Output Formats

Kroki supports multiple output formats:

| Format | Use Case | File Extension |
|--------|----------|----------------|
| **SVG** | Scalable, embeddable, web-friendly | `.svg` |
| **PNG** | Raster image, universal compatibility | `.png` |
| **PDF** | Print-ready documents | `.pdf` |
| **JPEG** | Photos (not recommended for diagrams) | `.jpg` |
| **TXT** | Text-based output (some formats) | `.txt` |
| **Base64** | Embedded in HTML/JSON | N/A |

**Recommendation:** Use SVG for documentation (scales perfectly), PNG for compatibility.

---

## Kroki API Reference

### Endpoint Structure

```
https://kroki.io/{diagram_type}/{output_format}/{encoded_source}
```

**Parameters:**
- `diagram_type`: mermaid, graphviz, vegalite, d2, erd, dbml, plantuml, etc.
- `output_format`: svg, png, pdf, jpeg, txt, base64
- `encoded_source`: Diagram source (deflate + base64 for GET, or use POST)

### GET Request (URL-Encoded)

```python
import zlib
import base64

# Compress and encode
source = "graph TD; A-->B;"
compressed = zlib.compress(source.encode('utf-8'), 9)
encoded = base64.urlsafe_b64encode(compressed).decode('ascii')

url = f"https://kroki.io/mermaid/svg/{encoded}"
```

### POST Request (Plain Text)

```python
import requests

url = "https://kroki.io/mermaid/svg"
source = "graph TD; A-->B;"

response = requests.post(url, data=source.encode('utf-8'))
svg = response.content
```

### Rate Limits (Public Service)

- **100 requests/minute** per IP
- **4KB URL length** limit (use POST for larger diagrams)
- **8MB body size** limit

**For unlimited usage:** Self-host Kroki via Docker (see Installation section below).

---

## Installation (Self-Hosting)

### Docker Quick Start

```bash
# Run Kroki server
docker run -d -p 8000:8000 yuzutech/kroki

# Test it
curl http://localhost:8000/health
```

### Docker Compose (Production)

```yaml
version: "3"
services:
  kroki:
    image: yuzutech/kroki
    environment:
      - KROKI_MERMAID_HOST=kroki-mermaid
      - KROKI_BPMN_HOST=kroki-bpmn
      - KROKI_EXCALIDRAW_HOST=kroki-excalidraw
    ports:
      - "8000:8000"

  kroki-mermaid:
    image: yuzutech/kroki-mermaid
    ports:
      - "8001:8001"

  kroki-bpmn:
    image: yuzutech/kroki-bpmn
    ports:
      - "8002:8002"

  kroki-excalidraw:
    image: yuzutech/kroki-excalidraw
    ports:
      - "8003:8003"
```

Start services:
```bash
docker-compose up -d
```

---

## Python Helper Class

Reusable class for generating diagrams:

```python
import requests
import zlib
import base64
from pathlib import Path

class KrokiClient:
    """Client for generating diagrams via Kroki API."""

    def __init__(self, base_url="https://kroki.io"):
        self.base_url = base_url

    def generate(self, source, diagram_type, output_format='svg', method='POST'):
        """Generate diagram and return bytes."""

        if method == 'GET':
            # Compress and encode for GET
            compressed = zlib.compress(source.encode('utf-8'), 9)
            encoded = base64.urlsafe_b64encode(compressed).decode('ascii')
            url = f"{self.base_url}/{diagram_type}/{output_format}/{encoded}"
            response = requests.get(url)
        else:
            # POST with plain text
            url = f"{self.base_url}/{diagram_type}/{output_format}"
            response = requests.post(url, data=source.encode('utf-8'))

        response.raise_for_status()
        return response.content

    def save(self, source, diagram_type, output_file, output_format='svg'):
        """Generate and save diagram to file."""

        diagram = self.generate(source, diagram_type, output_format)

        output_path = Path(output_file)
        output_path.write_bytes(diagram)

        return output_path

# Usage
client = KrokiClient()

# Generate and save
mermaid_source = """
graph TD
    A[Start] --> B[Process]
    B --> C[End]
"""

client.save(mermaid_source, 'mermaid', 'flowchart.svg')
```

---

## Best Practices

### 1. Choose the Right Format

- **Simple flowcharts** → Mermaid (easiest syntax)
- **Complex network graphs** → GraphViz (powerful layout algorithms)
- **Statistical charts** → Vega-Lite (data transformation pipeline)
- **Database schemas** → ERD or DBML (standard notation)
- **Modern diagrams** → D2 (clean, readable syntax)

### 2. Use POST for Complex Diagrams

GET requests require URL encoding and have length limits. POST is simpler:

```python
# ✅ Good: POST for complex diagrams
requests.post(url, data=diagram_source.encode('utf-8'))

# ❌ Avoid: GET for complex diagrams (encoding + length limits)
```

### 3. Cache Generated Diagrams

Avoid regenerating the same diagram repeatedly:

```python
from pathlib import Path
import hashlib

def get_or_generate_diagram(source, diagram_type, cache_dir='./diagram_cache'):
    """Generate diagram with caching."""

    # Create cache key from source
    cache_key = hashlib.md5(source.encode()).hexdigest()
    cache_file = Path(cache_dir) / f"{cache_key}.svg"

    if cache_file.exists():
        return cache_file.read_bytes()

    # Generate if not cached
    diagram = generate_diagram_post(source, diagram_type)

    cache_file.parent.mkdir(exist_ok=True)
    cache_file.write_bytes(diagram)

    return diagram
```

### 4. Self-Host for Production

Public service has rate limits. For production:
- Deploy Kroki via Docker
- No rate limits
- Better performance
- Data privacy

### 5. Version Control Diagram Source

Store diagram source in version control, not just images:

```
analysis/
├── diagrams/
│   ├── data-pipeline.mermaid.txt
│   ├── schema.erd.txt
│   └── lineage.dot.txt
└── images/
    ├── data-pipeline.svg
    ├── schema.svg
    └── lineage.svg
```

---

## Integration with DataPeeker

### Pattern: Documenting Data Lineage

```python
from kroki_client import KrokiClient

client = KrokiClient()

# Generate data lineage diagram
lineage = """
digraph G {
    rankdir=LR;

    raw_orders [label="raw_orders\n(CSV)"];
    clean_orders [label="clean_orders\n(SQLite)"];
    revenue_analysis [label="revenue_analysis\n(Markdown)"];

    raw_orders -> clean_orders [label="cleaning"];
    clean_orders -> revenue_analysis [label="analysis"];
}
"""

client.save(lineage, 'graphviz', 'analysis/lineage.svg')
```

### Pattern: Database Schema Documentation

```python
# ERD format
schema = """
[users]
*id {label: "int"}
email {label: "varchar, unique"}
name {label: "varchar"}

[orders]
*id {label: "int"}
+user_id {label: "int, FK"}
order_date {label: "date"}
total {label: "decimal"}

users 1--* orders
"""

client.save(schema, 'erd', 'analysis/schema.svg')
```

---

## Format-Specific Guides

Each format has detailed documentation with examples:

1. **[Vega-Lite](./formats/vega-lite.md)** - Statistical charts and data visualizations
2. **[Mermaid](./formats/mermaid.md)** - Flowcharts, Gantt charts, sequence diagrams
3. **[GraphViz](./formats/graphviz.md)** - Network graphs, hierarchies, data lineage
4. **[D2](./formats/d2.md)** - Modern diagrams, architecture, data models
5. **[ERD](./formats/erd.md)** - Entity-relationship diagrams for databases
6. **[DBML](./formats/dbml.md)** - Complete database documentation

---

## Troubleshooting

### Issue: "URL Too Long" Error

**Solution:** Use POST instead of GET:
```python
# Use POST for diagrams > 4KB
requests.post(url, data=source.encode('utf-8'))
```

### Issue: "Rate Limit Exceeded"

**Solution:** Self-host Kroki or implement request throttling:
```python
import time

def generate_with_retry(source, diagram_type, max_retries=3):
    for attempt in range(max_retries):
        try:
            return generate_diagram_post(source, diagram_type)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Rate limit
                time.sleep(60)  # Wait 1 minute
                continue
            raise
```

### Issue: Syntax Errors in Diagram

**Check format documentation** - Each format has specific syntax rules. See individual format guides.

---

## Additional Resources

**Official Documentation:**
- [Kroki Documentation](https://docs.kroki.io/)
- [Kroki GitHub](https://github.com/yuzutech/kroki)
- [Diagram Examples](https://kroki.io/examples.html)

**Format Documentation:**
- [Vega-Lite Docs](https://vega.github.io/vega-lite/)
- [Mermaid Docs](https://mermaid.js.org/)
- [GraphViz Docs](https://graphviz.org/)
- [D2 Docs](https://d2lang.com/)
- [PlantUML Docs](https://plantuml.com/)

**Complete research documentation:**
- See `KROKI_RESEARCH.md` for comprehensive technical details
