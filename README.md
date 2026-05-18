# Interactive Business Dashboard

## 📊 Task Objective

The objective of this project is to develop an interactive business dashboard using the Global Superstore dataset. The dashboard helps analyze key business metrics such as sales, profit, and customer performance across different regions, categories, and sub-categories.

The main goal is to provide an easy-to-use visual tool for understanding business performance and supporting data-driven decision making.

---

## 🛠️ Approach

The project was developed using Python and Streamlit following these steps:

1. **Data Loading**
   - Imported the Global Superstore dataset using Pandas.

2. **Data Cleaning**
   - Removed duplicate records.
   - Handled missing values.
   - Converted date columns into proper datetime format.

3. **Data Analysis**
   - Calculated total sales and total profit.
   - Identified top 5 customers based on sales.
   - Aggregated data by region, category, and sub-category.

4. **Dashboard Development**
   - Built an interactive dashboard using Streamlit.
   - Added sidebar filters for:
     - Region
     - Category
     - Sub-Category
   - Created visualizations using Plotly:
     - Sales by Category (Bar Chart)
     - Profit by Region (Pie Chart)
     - Top 5 Customers by Sales (Bar Chart)

5. **Interactivity**
   - Filters dynamically update all KPIs and charts in real-time.

---

## 📈 Results and Findings

- **Sales and Profit Overview**
  - The dashboard provides a clear summary of total sales and total profit across selected filters.

- **Top Customers**
  - A small group of customers contributes significantly to total sales, highlighting key revenue drivers.

- **Category Performance**
  - Certain product categories generate higher sales compared to others, helping identify strong business segments.

- **Regional Insights**
  - Profit distribution varies across regions, showing differences in market performance.


This project demonstrates how raw business data can be transformed into an interactive dashboard for meaningful insights and decision-making support.
