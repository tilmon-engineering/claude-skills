# Mermaid Diagrams via Kroki

Mermaid is a simple text-based diagramming language perfect for flowcharts, sequence diagrams, Gantt charts, and timelines. Great for documenting data workflows and analysis processes.

---

## When to Use Mermaid

**Best for:**
- Data processing workflows
- Analysis pipelines
- Project timelines (Gantt charts)
- Sequence of operations
- State machines

**Advantages:**
- Simple, readable syntax
- Documentation-friendly (looks good as text)
- Wide adoption in markdown tools
- Multiple diagram types in one syntax

---

## Quick Start

```python
from kroki_client import KrokiClient

client = KrokiClient()

diagram = """
graph TD
    A[Raw Data] --> B[Data Cleaning]
    B --> C[Analysis]
    C --> D[Visualization]
    D --> E[Report]
"""

client.save(diagram, 'mermaid', 'workflow.svg')
```

---

## Diagram Types

### 1. Flowcharts (graph)

**Use for:** Data workflows, processing pipelines

```python
workflow = """
graph LR
    A[(Raw CSV)] --> B[Import to SQLite]
    B --> C[Data Cleaning]
    C --> D[Quality Checks]
    D --> E{All Checks Pass?}
    E -->|Yes| F[Analysis]
    E -->|No| G[Manual Review]
    G --> C
    F --> H[Report]
"""

client.save(workflow, 'mermaid', 'data-pipeline.svg')
```

**Syntax:**
- `graph TD` - Top to bottom
- `graph LR` - Left to right
- `graph RL` - Right to left
- `graph BT` - Bottom to top

**Node shapes:**
- `A[Rectangle]` - Standard box
- `B([Rounded])` - Rounded box
- `C[(Database)]` - Cylinder (database)
- `D{Decision}` - Diamond
- `E((Circle))` - Circle
- `F>Flag]` - Flag shape

**Arrows:**
- `-->` - Solid arrow
- `-.->` - Dotted arrow
- `==>` - Thick arrow
- `--text-->` - Arrow with label

### 2. Sequence Diagrams

**Use for:** Data flow between systems, API interactions

```python
sequence = """
sequenceDiagram
    participant User
    participant API
    participant DB
    participant Cache

    User->>API: Request data
    API->>Cache: Check cache
    alt Cache hit
        Cache-->>API: Return cached data
    else Cache miss
        API->>DB: Query database
        DB-->>API: Return results
        API->>Cache: Store in cache
    end
    API-->>User: Return data
"""

client.save(sequence, 'mermaid', 'data-flow.svg')
```

### 3. Gantt Charts

**Use for:** Analysis project timelines, sprint planning

```python
gantt_chart = """
gantt
    title Data Analysis Project Timeline
    dateFormat YYYY-MM-DD

    section Data Collection
    Gather Requirements   :a1, 2024-01-01, 5d
    Import Raw Data       :a2, after a1, 3d

    section Data Prep
    Data Cleaning         :b1, after a2, 7d
    Quality Validation    :b2, after b1, 2d

    section Analysis
    Exploratory Analysis  :c1, after b2, 10d
    Statistical Tests     :c2, after c1, 5d
    Visualization         :c3, after c2, 3d

    section Reporting
    Draft Report          :d1, after c3, 5d
    Review & Revisions    :d2, after d1, 3d
    Final Presentation    :milestone, after d2, 1d
"""

client.save(gantt_chart, 'mermaid', 'timeline.svg')
```

### 4. State Diagrams

**Use for:** Data state transitions, workflow states

```python
state_diagram = """
stateDiagram-v2
    [*] --> Raw
    Raw --> Cleaning: Import
    Cleaning --> Validated: Quality Checks
    Validated --> Analyzed: Analysis
    Analyzed --> Reported: Visualization
    Reported --> [*]

    Cleaning --> Raw: Validation Failed
    Validated --> Cleaning: Issues Found
"""

client.save(state_diagram, 'mermaid', 'data-states.svg')
```

### 5. Entity Relationship Diagrams (Simple)

**Use for:** Basic database schemas

```python
erd = """
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    PRODUCT ||--o{ LINE-ITEM : "ordered in"

    CUSTOMER {
        int id PK
        string email
        string name
    }

    ORDER {
        int id PK
        int customer_id FK
        date order_date
        decimal total
    }

    LINE-ITEM {
        int order_id FK
        int product_id FK
        int quantity
        decimal price
    }

    PRODUCT {
        int id PK
        string name
        decimal price
    }
"""

client.save(erd, 'mermaid', 'schema.svg')
```

**Cardinality notation:**
- `||--||` - One to one
- `||--o{` - One to many
- `}o--o{` - Many to many

---

## DataPeeker Examples

### Example 1: Complete Analysis Workflow

```python
analysis_workflow = """
graph TD
    Start[Start Analysis] --> A1[Load CSV Files]
    A1 --> A2[Import to raw_* tables]

    A2 --> B1{Data Quality OK?}
    B1 -->|No| B2[Manual Cleaning]
    B2 --> A2
    B1 -->|Yes| B3[Create clean_* tables]

    B3 --> C1[Exploratory Analysis]
    C1 --> C2[Hypothesis Formation]
    C2 --> C3[Statistical Testing]

    C3 --> D1{Significant Results?}
    D1 -->|Yes| D2[Create Visualizations]
    D1 -->|No| D3[Adjust Hypothesis]
    D3 --> C2

    D2 --> E1[Draft Report]
    E1 --> E2[Peer Review]
    E2 --> E3[Final Report]
    E3 --> End[Analysis Complete]

    style Start fill:#90EE90
    style End fill:#FFB6C1
    style B1 fill:#FFE4B5
    style D1 fill:#FFE4B5
"""

client.save(analysis_workflow, 'mermaid', 'full-workflow.svg')
```

### Example 2: Data Quality Pipeline

```python
quality_pipeline = """
graph LR
    A[(Raw CSV)] --> B[Profile Data]
    B --> C[Detect Duplicates]
    B --> D[Detect Outliers]
    B --> E[Check NULL %]

    C --> F{Issues Found?}
    D --> F
    E --> F

    F -->|Yes| G[Generate Quality Report]
    F -->|No| H[Mark as Clean]

    G --> I[Manual Review Required]
    H --> J[Ready for Analysis]

    style A fill:#E8F4F8
    style I fill:#FFE4E1
    style J fill:#90EE90
"""

client.save(quality_pipeline, 'mermaid', 'quality-pipeline.svg')
```

### Example 3: Analysis Sprint Timeline

```python
sprint = """
gantt
    title Q4 Revenue Analysis Sprint
    dateFormat YYYY-MM-DD

    section Week 1
    Import sales data       :2024-10-01, 2d
    Import customer data    :2024-10-01, 2d
    Data profiling          :2024-10-03, 2d

    section Week 2
    Data cleaning           :2024-10-07, 3d
    Quality validation      :2024-10-10, 2d

    section Week 3
    Exploratory analysis    :2024-10-14, 5d

    section Week 4
    Statistical analysis    :2024-10-21, 3d
    Visualizations          :2024-10-24, 2d

    section Week 5
    Report draft            :2024-10-28, 3d
    Review                  :2024-10-31, 2d

    section Milestones
    Analysis kickoff        :milestone, 2024-10-01, 0d
    Data ready              :milestone, 2024-10-12, 0d
    Analysis complete       :milestone, 2024-10-26, 0d
    Report final            :milestone, 2024-11-02, 0d
"""

client.save(sprint, 'mermaid', 'sprint-timeline.svg')
```

---

## Styling

### Colors and Themes

```python
styled = """
graph TD
    A[Start] --> B[Process 1]
    B --> C[Process 2]
    C --> D[End]

    style A fill:#90EE90,stroke:#228B22,stroke-width:2px
    style D fill:#FFB6C1,stroke:#C71585,stroke-width:2px
    style B fill:#87CEEB,stroke:#4682B4
    style C fill:#87CEEB,stroke:#4682B4
"""
```

### Class Definitions

```python
with_classes = """
graph TD
    A[Import Data]:::import --> B[Clean Data]:::process
    B --> C[Analyze]:::process
    C --> D[Report]:::output

    classDef import fill:#E8F4F8,stroke:#0077BE
    classDef process fill:#FFF4E6,stroke:#FF8C00
    classDef output fill:#E8F5E9,stroke:#4CAF50
"""
```

---

## Best Practices

### 1. Keep It Simple

Mermaid is best for high-level overviews. For complex diagrams, consider GraphViz.

```python
# ✅ Good: Clear, focused
simple = """
graph TD
    A[Raw Data] --> B[Clean Data]
    B --> C[Analysis]
"""

# ❌ Avoid: Too many nodes
complex = """
graph TD
    A1 --> A2 --> A3 --> A4 --> ...
    # (20+ nodes becomes hard to read)
"""
```

### 2. Use Descriptive Labels

```python
# ✅ Good: Clear purpose
clear = """
graph TD
    A[Import CSV Files] --> B[Validate Schema]
"""

# ❌ Avoid: Cryptic labels
cryptic = """
graph TD
    A[Step1] --> B[Step2]
"""
```

### 3. Direction Matters

Choose direction based on content:

```python
# Process flow: Left to right
process = "graph LR\n    A --> B --> C"

# Hierarchy: Top to bottom
hierarchy = "graph TD\n    A --> B\n    A --> C"
```

### 4. Use Subgraphs for Grouping

```python
grouped = """
graph TD
    subgraph "Data Ingestion"
        A[Load CSV] --> B[Import to DB]
    end

    subgraph "Data Preparation"
        C[Clean Data] --> D[Validate]
    end

    B --> C
    D --> E[Analysis]
"""
```

---

## Troubleshooting

### Issue: Syntax Error

**Common mistakes:**
- Missing quotes around labels with special characters
- Incorrect arrow syntax (`->` instead of `-->`)
- Unclosed brackets

```python
# ❌ Wrong
"A[My Label] -> B"

# ✅ Correct
"A[My Label] --> B"
```

### Issue: Layout Problems

Mermaid auto-layouts diagrams. For fine control, use GraphViz instead.

---

## References

- [Mermaid Official Docs](https://mermaid.js.org/)
- [Mermaid Live Editor](https://mermaid.live/)
- [Syntax Reference](https://mermaid.js.org/intro/syntax-reference.html)
- [Kroki Mermaid Examples](https://kroki.io/examples.html#mermaid)
