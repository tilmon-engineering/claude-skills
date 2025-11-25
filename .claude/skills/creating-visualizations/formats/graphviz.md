# GraphViz (DOT) Diagrams via Kroki

GraphViz uses the DOT language to create network graphs, hierarchies, and relationship diagrams with powerful automatic layout algorithms. Excellent for data lineage and complex relationships.

---

## When to Use GraphViz

**Best for:**
- Data lineage and provenance
- Complex network relationships
- Hierarchical structures
- Dependency graphs
- System architecture

**Advantages:**
- Powerful automatic layout algorithms
- Handles complex graphs with many nodes
- Fine-grained control over appearance
- Industry-standard DOT language

---

## Quick Start

```python
from kroki_client import KrokiClient

client = KrokiClient()

diagram = """
digraph G {
    rankdir=LR;

    raw_data [label="Raw CSV" shape=cylinder];
    clean_data [label="Clean Data" shape=cylinder];
    analysis [label="Analysis" shape=box];
    report [label="Report" shape=note];

    raw_data -> clean_data [label="cleaning"];
    clean_data -> analysis [label="query"];
    analysis -> report [label="generate"];
}
"""

client.save(diagram, 'graphviz', 'lineage.svg')
```

---

## Graph Types

### 1. Directed Graphs (digraph)

**Use for:** Data flow, dependencies, lineage

```python
lineage = """
digraph DataLineage {
    rankdir=LR;
    node [shape=box, style=rounded];

    // Data sources
    csv1 [label="sales.csv"];
    csv2 [label="customers.csv"];
    csv3 [label="products.csv"];

    // Raw tables
    raw_sales [label="raw_sales"];
    raw_customers [label="raw_customers"];
    raw_products [label="raw_products"];

    // Clean tables
    clean_sales [label="clean_sales"];
    clean_customers [label="clean_customers"];
    clean_products [label="clean_products"];

    // Analysis
    revenue_analysis [label="Revenue Analysis"];

    // Connections
    csv1 -> raw_sales [label="import"];
    csv2 -> raw_customers [label="import"];
    csv3 -> raw_products [label="import"];

    raw_sales -> clean_sales [label="clean"];
    raw_customers -> clean_customers [label="clean"];
    raw_products -> clean_products [label="clean"];

    clean_sales -> revenue_analysis;
    clean_customers -> revenue_analysis;
    clean_products -> revenue_analysis;
}
"""

client.save(lineage, 'graphviz', 'data-lineage.svg')
```

### 2. Undirected Graphs (graph)

**Use for:** Relationships, correlations

```python
correlations = """
graph Correlations {
    node [shape=ellipse];

    Revenue -- CustomerCount [label="r=0.85"];
    Revenue -- AvgOrderValue [label="r=0.72"];
    Revenue -- MarketingSpend [label="r=0.65"];

    CustomerCount -- AvgOrderValue [label="r=0.23"];
    CustomerCount -- MarketingSpend [label="r=0.78"];

    AvgOrderValue -- MarketingSpend [label="r=0.45"];
}
"""

client.save(correlations, 'graphviz', 'correlations.svg')
```

---

## Layout Directions

```python
# Left to Right (best for pipelines)
"digraph { rankdir=LR; A -> B -> C; }"

# Top to Bottom (best for hierarchies)
"digraph { rankdir=TB; A -> B -> C; }"

# Bottom to Top
"digraph { rankdir=BT; A -> B -> C; }"

# Right to Left
"digraph { rankdir=RL; A -> B -> C; }"
```

---

## Node Shapes

```python
shapes = """
digraph Shapes {
    rankdir=LR;

    a [label="Box" shape=box];
    b [label="Rounded" shape=box, style=rounded];
    c [label="Circle" shape=circle];
    d [label="Ellipse" shape=ellipse];
    e [label="Database" shape=cylinder];
    f [label="Document" shape=note];
    g [label="Diamond" shape=diamond];
    h [label="Folder" shape=folder];
    i [label="Component" shape=component];

    a -> b -> c -> d -> e -> f -> g -> h -> i;
}
"""
```

**Common shapes for data visualization:**
- `cylinder` - Databases, data stores
- `box` - Processes, transformations
- `note` - Reports, documents
- `folder` - Directories, collections
- `diamond` - Decisions, conditions

---

## Edge Styles

```python
edges = """
digraph Edges {
    A -> B [label="solid"];
    B -> C [label="dashed", style=dashed];
    C -> D [label="dotted", style=dotted];
    D -> E [label="bold", style=bold];

    E -> F [label="colored", color=red];
    F -> G [label="thick", penwidth=3];

    G -> H [arrowhead=normal];
    H -> I [arrowhead=diamond];
    I -> J [arrowhead=dot];
}
"""
```

---

## Clusters (Subgraphs)

Group related nodes together:

```python
clustered = """
digraph Pipeline {
    rankdir=LR;

    subgraph cluster_ingestion {
        label="Data Ingestion";
        style=filled;
        color=lightgrey;

        csv1 [label="sales.csv"];
        csv2 [label="customers.csv"];
        import [label="Import Process"];

        csv1 -> import;
        csv2 -> import;
    }

    subgraph cluster_storage {
        label="Data Storage";
        style=filled;
        color=lightblue;

        raw [label="raw_* tables"];
        clean [label="clean_* tables"];

        raw -> clean [label="cleaning"];
    }

    subgraph cluster_analysis {
        label="Analysis";
        style=filled;
        color=lightgreen;

        explore [label="Exploratory"];
        stats [label="Statistical"];
        viz [label="Visualization"];

        explore -> stats -> viz;
    }

    import -> raw;
    clean -> explore;
}
"""

client.save(clustered, 'graphviz', 'pipeline-clustered.svg')
```

---

## DataPeeker Examples

### Example 1: Complete Data Pipeline

```python
complete_pipeline = """
digraph CompletePipeline {
    rankdir=TB;
    node [style=rounded];

    // Source layer
    subgraph cluster_sources {
        label="Data Sources";
        style=filled;
        color="#E8F4F8";

        s1 [label="sales_2024.csv" shape=note];
        s2 [label="customers.csv" shape=note];
        s3 [label="products.csv" shape=note];
    }

    // Import layer
    import [label="Import Script\n(Python)" shape=box];

    // Raw storage
    subgraph cluster_raw {
        label="Raw Tables";
        style=filled;
        color="#FFF4E6";

        r1 [label="raw_sales" shape=cylinder];
        r2 [label="raw_customers" shape=cylinder];
        r3 [label="raw_products" shape=cylinder];
    }

    // Quality checks
    quality [label="Quality\nValidation" shape=diamond];
    issues [label="Quality\nReport" shape=note];

    // Clean storage
    subgraph cluster_clean {
        label="Clean Tables";
        style=filled;
        color="#E8F5E9";

        c1 [label="clean_sales" shape=cylinder];
        c2 [label="clean_customers" shape=cylinder];
        c3 [label="clean_products" shape=cylinder];
    }

    // Analysis
    analysis [label="Revenue\nAnalysis" shape=box];
    report [label="Q4 Report" shape=note];

    // Connections
    s1 -> import;
    s2 -> import;
    s3 -> import;

    import -> r1;
    import -> r2;
    import -> r3;

    r1 -> quality;
    r2 -> quality;
    r3 -> quality;

    quality -> issues [label="if issues"];
    quality -> c1 [label="if clean"];
    quality -> c2 [label="if clean"];
    quality -> c3 [label="if clean"];

    c1 -> analysis;
    c2 -> analysis;
    c3 -> analysis;

    analysis -> report;
}
"""

client.save(complete_pipeline, 'graphviz', 'complete-pipeline.svg')
```

### Example 2: Data Lineage with Transformations

```python
lineage_detailed = """
digraph DataLineage {
    rankdir=LR;

    // Style definitions
    node [style=rounded, fontname="Arial"];
    edge [fontname="Arial", fontsize=10];

    // Sources
    raw_orders [label="raw_orders\n(1.2M rows)" shape=cylinder, fillcolor="#FFE4E1", style="rounded,filled"];

    // Transformations
    dedup [label="Remove\nDuplicates\n(-234 rows)" shape=box];
    filter_nulls [label="Filter NULLs\n(-1,456 rows)" shape=box];
    standardize [label="Standardize\nFormats" shape=box];
    validate [label="Validate\nRanges" shape=box];

    // Clean data
    clean_orders [label="clean_orders\n(1,198,310 rows)" shape=cylinder, fillcolor="#90EE90", style="rounded,filled"];

    // Analysis views
    monthly_rev [label="monthly_revenue\n(view)" shape=folder];
    customer_ltv [label="customer_ltv\n(view)" shape=folder];

    // Reports
    report1 [label="Revenue\nReport" shape=note];
    report2 [label="Customer\nAnalysis" shape=note];

    // Flow
    raw_orders -> dedup -> filter_nulls -> standardize -> validate -> clean_orders;

    clean_orders -> monthly_rev -> report1;
    clean_orders -> customer_ltv -> report2;
}
"""

client.save(lineage_detailed, 'graphviz', 'lineage-detailed.svg')
```

### Example 3: Analysis Dependencies

```python
dependencies = """
digraph AnalysisDeps {
    rankdir=TB;

    // Data sources
    node [shape=cylinder, style=filled, fillcolor="#E8F4F8"];
    orders;
    customers;
    products;

    // Analysis scripts
    node [shape=box, style=rounded, fillcolor="#FFF4E6"];
    revenue_calc [label="01_revenue_calc.py"];
    cohort_analysis [label="02_cohort_analysis.py"];
    churn_pred [label="03_churn_prediction.py"];

    // Outputs
    node [shape=note, style=filled, fillcolor="#E8F5E9"];
    revenue_report [label="revenue_report.md"];
    cohort_viz [label="cohort_viz.png"];
    churn_model [label="churn_model.pkl"];

    // Dependencies
    orders -> revenue_calc;
    customers -> revenue_calc;
    products -> revenue_calc;
    revenue_calc -> revenue_report;

    orders -> cohort_analysis;
    customers -> cohort_analysis;
    cohort_analysis -> cohort_viz;

    orders -> churn_pred;
    customers -> churn_pred;
    cohort_analysis -> churn_pred [style=dashed, label="uses"];
    churn_pred -> churn_model;
}
"""

client.save(dependencies, 'graphviz', 'analysis-deps.svg')
```

### Example 4: Database Schema Relationships

```python
schema = """
digraph Schema {
    rankdir=TB;
    node [shape=record, style=rounded];

    users [label="{users|+ id : int\\l+ email : varchar\\l+ name : varchar\\l+ created_at : timestamp\\l}"];

    orders [label="{orders|+ id : int\\l+ user_id : int (FK)\\l+ order_date : date\\l+ total : decimal\\l+ status : varchar\\l}"];

    order_items [label="{order_items|+ id : int\\l+ order_id : int (FK)\\l+ product_id : int (FK)\\l+ quantity : int\\l+ price : decimal\\l}"];

    products [label="{products|+ id : int\\l+ name : varchar\\l+ price : decimal\\l+ category : varchar\\l}"];

    users -> orders [label="1:N"];
    orders -> order_items [label="1:N"];
    products -> order_items [label="1:N"];
}
"""

client.save(schema, 'graphviz', 'schema-graph.svg')
```

---

## Colors and Styling

### Color Schemes

```python
colored = """
digraph Colored {
    rankdir=LR;

    // Color by type
    source [fillcolor="#E8F4F8", style=filled, label="Data Source"];
    process [fillcolor="#FFF4E6", style=filled, label="Processing"];
    storage [fillcolor="#E8F5E9", style=filled, label="Storage"];
    output [fillcolor="#FFE4E1", style=filled, label="Output"];

    source -> process -> storage -> output;
}
"""
```

### Common Color Codes

- `#E8F4F8` - Light blue (sources)
- `#FFF4E6` - Light orange (processing)
- `#E8F5E9` - Light green (success/clean)
- `#FFE4E1` - Light red (issues/outputs)
- `#F3E5F5` - Light purple (analysis)

---

## Best Practices

### 1. Use Meaningful Node IDs

```python
# ✅ Good: Descriptive IDs
"""
digraph {
    raw_sales -> clean_sales -> revenue_analysis;
}
"""

# ❌ Avoid: Generic IDs
"""
digraph {
    n1 -> n2 -> n3;
}
"""
```

### 2. Group Related Nodes with Clusters

```python
# ✅ Good: Organized with clusters
"""
digraph {
    subgraph cluster_sources {
        label="Sources";
        csv1; csv2;
    }
    subgraph cluster_storage {
        label="Storage";
        raw; clean;
    }
}
"""
```

### 3. Use Appropriate Layout Direction

```python
# Pipeline flow: Left to Right
"digraph { rankdir=LR; ... }"

# Hierarchy: Top to Bottom
"digraph { rankdir=TB; ... }"
```

### 4. Add Labels to Edges for Clarity

```python
# ✅ Good: Labeled relationships
"""
digraph {
    A -> B [label="transform"];
    B -> C [label="validate"];
}
"""
```

### 5. Use HTML-Like Labels for Rich Formatting

```python
html_labels = """
digraph {
    node [shape=none];

    table1 [label=<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        <TR><TD BGCOLOR="lightblue"><B>clean_orders</B></TD></TR>
        <TR><TD ALIGN="LEFT">id: int</TD></TR>
        <TR><TD ALIGN="LEFT">user_id: int</TD></TR>
        <TR><TD ALIGN="LEFT">total: decimal</TD></TR>
        </TABLE>
    >];
}
"""
```

---

## Advanced Features

### Rank Constraints

Force nodes to same rank (horizontal alignment):

```python
same_rank = """
digraph {
    rankdir=TB;

    {rank=same; A; B; C;}
    {rank=same; D; E;}

    A -> D;
    B -> E;
    C -> E;
}
"""
```

### Port Connections

Connect to specific sides of nodes:

```python
ports = """
digraph {
    A -> B:n;  // Connect to north (top)
    B:s -> C;  // Connect from south (bottom)
    C:e -> D:w;  // East to west
}
"""
```

---

## Troubleshooting

### Issue: Overlapping Nodes

**Solution:** Use `nodesep` and `ranksep`:

```python
spaced = """
digraph {
    nodesep=1.0;  // Horizontal spacing
    ranksep=1.0;  // Vertical spacing

    A -> B -> C;
}
"""
```

### Issue: Long Edge Crossings

**Solution:** Adjust rank direction or use clusters:

```python
# Try different directions
rankdir=LR  # vs TB, BT, RL
```

### Issue: Text Overflow in Nodes

**Solution:** Use `\\l` for left-aligned multi-line text:

```python
multiline = """
digraph {
    A [label="Line 1\\lLine 2\\lLine 3\\l"];
}
"""
```

---

## References

- [GraphViz Official Docs](https://graphviz.org/)
- [DOT Language Guide](https://graphviz.org/doc/info/lang.html)
- [Node Shapes Gallery](https://graphviz.org/doc/info/shapes.html)
- [Color Names](https://graphviz.org/doc/info/colors.html)
- [Kroki GraphViz Examples](https://kroki.io/examples.html#graphviz)
