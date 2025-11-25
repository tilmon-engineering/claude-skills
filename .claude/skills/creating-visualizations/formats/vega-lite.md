# Vega-Lite Charts via Kroki

Vega-Lite is a high-level grammar for creating statistical visualizations. Perfect for bar charts, line plots, scatter plots, and distributions from data.

---

## When to Use Vega-Lite

**Best for:**
- Statistical charts (bar, line, scatter, histograms)
- Data distributions and aggregations
- Multi-series comparisons
- Interactive visualizations (when exported to HTML)

**Advantages:**
- Declarative JSON specification
- Built-in data transformations
- Statistical aggregations (sum, mean, count, etc.)
- Professional statistical graphics

**Note:** For quick terminal visualizations, use plotext. For embedded reports/presentations, use Vega-Lite via Kroki.

---

## Quick Start

```python
from kroki_client import KrokiClient
import json

client = KrokiClient()

# Vega-Lite uses JSON specification
chart = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "description": "Simple bar chart",
    "data": {
        "values": [
            {"category": "Electronics", "revenue": 345678},
            {"category": "Home & Garden", "revenue": 298432},
            {"category": "Clothing", "revenue": 234567}
        ]
    },
    "mark": "bar",
    "encoding": {
        "x": {"field": "category", "type": "nominal"},
        "y": {"field": "revenue", "type": "quantitative"}
    }
}

# Convert to JSON string
chart_json = json.dumps(chart)

client.save(chart_json, 'vegalite', 'revenue-chart.svg')
```

---

## Chart Types

### 1. Bar Charts

```python
bar_chart = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Q4 Revenue by Category",
    "data": {
        "values": [
            {"category": "Electronics", "revenue": 345678},
            {"category": "Home", "revenue": 298432},
            {"category": "Clothing", "revenue": 234567},
            {"category": "Sports", "revenue": 134234},
            {"category": "Toys", "revenue": 56789}
        ]
    },
    "mark": "bar",
    "encoding": {
        "x": {"field": "category", "type": "nominal", "title": "Category"},
        "y": {"field": "revenue", "type": "quantitative", "title": "Revenue ($)"},
        "color": {"field": "category", "type": "nominal", "legend": None}
    }
}

client.save(json.dumps(bar_chart), 'vegalite', 'bar-chart.svg')
```

**Horizontal bars:**

```python
horizontal = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"values": [...]},
    "mark": "bar",
    "encoding": {
        "y": {"field": "category", "type": "nominal"},  # Swap x/y
        "x": {"field": "revenue", "type": "quantitative"}
    }
}
```

### 2. Line Charts

```python
line_chart = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Monthly Revenue Trend",
    "data": {
        "values": [
            {"month": "2024-01", "revenue": 120000},
            {"month": "2024-02", "revenue": 135000},
            {"month": "2024-03", "revenue": 142000},
            {"month": "2024-04", "revenue": 138000},
            {"month": "2024-05", "revenue": 155000},
            {"month": "2024-06", "revenue": 168000}
        ]
    },
    "mark": {"type": "line", "point": True},
    "encoding": {
        "x": {"field": "month", "type": "temporal", "title": "Month"},
        "y": {"field": "revenue", "type": "quantitative", "title": "Revenue ($)"}
    }
}

client.save(json.dumps(line_chart), 'vegalite', 'line-chart.svg')
```

**Multiple series:**

```python
multi_series = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Revenue Comparison: 2023 vs 2024",
    "data": {
        "values": [
            {"month": "Jan", "year": "2023", "revenue": 120000},
            {"month": "Jan", "year": "2024", "revenue": 140000},
            {"month": "Feb", "year": "2023", "revenue": 130000},
            {"month": "Feb", "year": "2024", "revenue": 155000},
            # ... more months
        ]
    },
    "mark": {"type": "line", "point": True},
    "encoding": {
        "x": {"field": "month", "type": "ordinal"},
        "y": {"field": "revenue", "type": "quantitative"},
        "color": {"field": "year", "type": "nominal"}
    }
}
```

### 3. Scatter Plots

```python
scatter = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Order Value vs Shipping Speed",
    "data": {
        "values": [
            {"shipping_days": 1, "order_value": 245},
            {"shipping_days": 1, "order_value": 312},
            {"shipping_days": 2, "order_value": 156},
            {"shipping_days": 2, "order_value": 198},
            {"shipping_days": 3, "order_value": 89},
            {"shipping_days": 5, "order_value": 45}
            # ... more data points
        ]
    },
    "mark": "point",
    "encoding": {
        "x": {"field": "shipping_days", "type": "quantitative", "title": "Shipping Speed (days)"},
        "y": {"field": "order_value", "type": "quantitative", "title": "Order Value ($)"}
    }
}

client.save(json.dumps(scatter), 'vegalite', 'scatter.svg')
```

### 4. Histograms

```python
histogram = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Order Value Distribution",
    "data": {
        "values": [
            {"order_value": 23}, {"order_value": 45}, {"order_value": 67},
            {"order_value": 89}, {"order_value": 34}, {"order_value": 56},
            # ... many more values
        ]
    },
    "mark": "bar",
    "encoding": {
        "x": {
            "field": "order_value",
            "type": "quantitative",
            "bin": {"maxbins": 10},
            "title": "Order Value ($)"
        },
        "y": {
            "aggregate": "count",
            "type": "quantitative",
            "title": "Frequency"
        }
    }
}

client.save(json.dumps(histogram), 'vegalite', 'histogram.svg')
```

### 5. Grouped Bar Charts

```python
grouped = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Revenue by Category and Quarter",
    "data": {
        "values": [
            {"category": "Electronics", "quarter": "Q1", "revenue": 85000},
            {"category": "Electronics", "quarter": "Q2", "revenue": 92000},
            {"category": "Home", "quarter": "Q1", "revenue": 72000},
            {"category": "Home", "quarter": "Q2", "revenue": 78000},
            # ... more combinations
        ]
    },
    "mark": "bar",
    "encoding": {
        "x": {"field": "category", "type": "nominal"},
        "y": {"field": "revenue", "type": "quantitative"},
        "color": {"field": "quarter", "type": "nominal"},
        "xOffset": {"field": "quarter"}
    }
}
```

---

## Data Transformations

Vega-Lite includes powerful built-in transformations:

### Aggregation

```python
aggregated = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Average Order Value by Category",
    "data": {
        "values": [
            {"category": "Electronics", "order_value": 245},
            {"category": "Electronics", "order_value": 312},
            {"category": "Home", "order_value": 89},
            {"category": "Home", "order_value": 145},
            # ... more orders
        ]
    },
    "mark": "bar",
    "encoding": {
        "x": {"field": "category", "type": "nominal"},
        "y": {"aggregate": "mean", "field": "order_value", "type": "quantitative", "title": "Avg Order Value"}
    }
}
```

**Available aggregations:**
- `count` - Count of records
- `sum` - Sum of values
- `mean` - Average
- `median` - Median value
- `min` / `max` - Min/max values
- `stdev` - Standard deviation

### Filtering

```python
filtered = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"values": [...]},
    "transform": [
        {"filter": "datum.revenue > 100000"}
    ],
    "mark": "bar",
    "encoding": {...}
}
```

### Calculate New Fields

```python
calculated = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"values": [...]},
    "transform": [
        {"calculate": "datum.revenue / datum.orders", "as": "avg_order_value"}
    ],
    "mark": "bar",
    "encoding": {
        "x": {"field": "category"},
        "y": {"field": "avg_order_value"}
    }
}
```

---

## DataPeeker Examples

### Example 1: Revenue Analysis Dashboard

```python
import sqlite3
import json

# Query data from SQLite
conn = sqlite3.connect('analysis.db')
cursor = conn.execute("""
    SELECT
        strftime('%Y-%m', order_date) as month,
        SUM(total) as revenue
    FROM clean_orders
    WHERE order_date >= '2024-01-01'
    GROUP BY month
    ORDER BY month
""")

data = [{"month": row[0], "revenue": row[1]} for row in cursor.fetchall()]

# Create Vega-Lite spec
chart = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "2024 Monthly Revenue",
    "width": 600,
    "height": 400,
    "data": {"values": data},
    "mark": {"type": "line", "point": True, "tooltip": True},
    "encoding": {
        "x": {"field": "month", "type": "temporal", "title": "Month"},
        "y": {"field": "revenue", "type": "quantitative", "title": "Revenue ($)",
              "axis": {"format": "$,.0f"}}
    }
}

client.save(json.dumps(chart), 'vegalite', 'monthly-revenue.svg')
```

### Example 2: Category Performance Comparison

```python
# Query data
cursor = conn.execute("""
    SELECT
        p.category,
        COUNT(DISTINCT o.id) as orders,
        SUM(oi.quantity * oi.price) as revenue
    FROM clean_orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY p.category
    ORDER BY revenue DESC
""")

data = [{"category": row[0], "orders": row[1], "revenue": row[2]} for row in cursor]

# Create layered chart (bars + line)
chart = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Category Performance: Orders vs Revenue",
    "width": 600,
    "height": 400,
    "data": {"values": data},
    "encoding": {"x": {"field": "category", "type": "nominal", "title": "Category"}},
    "layer": [
        {
            "mark": "bar",
            "encoding": {
                "y": {"field": "revenue", "type": "quantitative", "title": "Revenue ($)"},
                "color": {"value": "#4682B4"}
            }
        },
        {
            "mark": {"type": "line", "color": "#FF6347", "point": True},
            "encoding": {
                "y": {"field": "orders", "type": "quantitative", "title": "Orders"},
                "color": {"value": "#FF6347"}
            }
        }
    ],
    "resolve": {"scale": {"y": "independent"}}
}

client.save(json.dumps(chart), 'vegalite', 'category-performance.svg')
```

### Example 3: Customer Segmentation

```python
# Query customer LTV distribution
cursor = conn.execute("""
    SELECT
        customer_id,
        SUM(total) as lifetime_value
    FROM clean_orders
    GROUP BY customer_id
""")

data = [{"ltv": row[1]} for row in cursor]

# Create histogram with annotations
chart = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "title": "Customer Lifetime Value Distribution",
    "width": 600,
    "height": 400,
    "data": {"values": data},
    "layer": [
        {
            "mark": "bar",
            "encoding": {
                "x": {
                    "field": "ltv",
                    "type": "quantitative",
                    "bin": {"maxbins": 20},
                    "title": "Lifetime Value ($)"
                },
                "y": {
                    "aggregate": "count",
                    "type": "quantitative",
                    "title": "Number of Customers"
                }
            }
        },
        {
            "mark": {"type": "rule", "color": "red", "strokeWidth": 2},
            "encoding": {
                "x": {"aggregate": "median", "field": "ltv"}
            }
        }
    ]
}

client.save(json.dumps(chart), 'vegalite', 'ltv-distribution.svg')
```

---

## Best Practices

### 1. Use Appropriate Mark Types

```python
# ✅ Good: Right mark for data type
bar_chart = {"mark": "bar", ...}  # Categorical data
line_chart = {"mark": "line", ...}  # Time series
scatter = {"mark": "point", ...}  # Relationships

# ❌ Avoid: Wrong mark type
# Don't use line chart for categorical data
```

### 2. Add Titles and Axis Labels

```python
# ✅ Good: Clear labels
chart = {
    "title": "Q4 2024 Revenue by Category",
    "encoding": {
        "x": {"field": "category", "title": "Product Category"},
        "y": {"field": "revenue", "title": "Revenue (USD)"}
    }
}
```

### 3. Format Numbers Appropriately

```python
# Add formatting to axis
"y": {
    "field": "revenue",
    "type": "quantitative",
    "axis": {"format": "$,.0f"}  # Currency with commas
}
```

**Format codes:**
- `$,.0f` - Currency: $1,234
- `.2f` - Decimal: 12.34
- `.1%` - Percentage: 45.2%

### 4. Use Data from SQLite

```python
def create_chart_from_query(query, x_field, y_field, title):
    """Generate Vega-Lite chart from SQL query."""

    conn = sqlite3.connect('analysis.db')
    cursor = conn.execute(query)
    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    chart = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "title": title,
        "data": {"values": data},
        "mark": "bar",
        "encoding": {
            "x": {"field": x_field, "type": "nominal"},
            "y": {"field": y_field, "type": "quantitative"}
        }
    }

    return json.dumps(chart)
```

---

## Troubleshooting

### Issue: Data Not Displaying

**Check data format:**
```python
# ✅ Correct: Array of objects
{"values": [{"x": 1, "y": 2}, {"x": 2, "y": 4}]}

# ❌ Wrong: Flat array
{"values": [1, 2, 3, 4]}
```

### Issue: Type Mismatch Errors

**Ensure correct field types:**
- `nominal` - Categories (strings)
- `ordinal` - Ordered categories
- `quantitative` - Numbers
- `temporal` - Dates/times

### Issue: Chart Too Small

**Adjust dimensions:**
```python
chart = {
    "width": 800,
    "height": 600,
    ...
}
```

---

## References

- [Vega-Lite Documentation](https://vega.github.io/vega-lite/)
- [Example Gallery](https://vega.github.io/vega-lite/examples/)
- [Data Transform Reference](https://vega.github.io/vega-lite/docs/transform.html)
- [Mark Types](https://vega.github.io/vega-lite/docs/mark.html)
- [Kroki Vega-Lite Examples](https://kroki.io/examples.html#vegalite)
