# Market Phase Reference

## Purpose

Analyze the market landscape to determine potential for scale and growth. This phase defines the Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM) to justify the business opportunity.

## Inputs

**Process Dependencies:**
- **Phase 3: Solution (Mandatory):** ARPU (Pricing) is required for the bottom-up TAM/SAM/SOM calculations.
- **Phase 2: Problem & Opportunity (Mandatory):** The specific target personas and segments must be defined to filter the SAM.

**You MUST synthesize information from ALL previously completed phases before drafting.** 
The business plan is a cumulative pipeline. Your inputs include:
1. **Previous Phase Outputs:** All documents and research logs generated in Phases 1-6.
2. **Existing Workspace Data:** Always check the output directory (`{output_folder}/businessplan-writing/`) for any existing `market/` folder or data from preceding phases. If files already exist from a previous execution, you must incorporate their content to ensure continuity and avoid duplication.
3. **Primary Direct Dependencies:** Phase 1: Research (market trends and industry data) and Phase 3: Solution (business domain and target customer profile).

## Sub-Task Index

| # | Sub-Task | Output File | Description |
|---|---|---|---|
| 1 | Research Market | `market/research-log.md` | Web search for market data, size reports, growth trends, and PESTEL factors |
| 2 | Calculate TAM | `market/tam.md` | Estimate the Total Addressable Market (global demand) |
| 3 | Calculate SAM | `market/sam.md` | Estimate the Serviceable Available Market (reachable segment) |
| 4 | Calculate SOM | `market/som.md` | Estimate the Serviceable Obtainable Market (realistic capture in 1-3 years) |
| 5 | Write Market Characteristics | `market/characteristics.md` | Define market characteristics |
| 6 | Write Market Growth Rate | `market/growth-rate.md` | Analyze market growth rate |
| 7 | Write PESTEL Analysis | `market/pestel-analysis.md` | Conduct PESTEL analysis |
| 8 | Write Five Forces Analysis | `market/five-forces.md` | Conduct Porter's Five Forces analysis |

---

## Detailed Sub-Task Instructions

### 1. Research Market

**Dependencies:**
- **Phase 1: Research:** Use initial market intelligence and industry trends.
- **Phase 2: Problem & Opportunity:** Use target segments to focus the market research.

Use web search tools to gather quantitative and qualitative market data.

**Research objectives:**
- Find industry reports (Gartner, Statista, IDC, Forrester, etc.) for TAM/SAM estimates.
- Search for historical and projected market growth rates (CAGR).
- Identify macro-level trends (Political, Economic, Social, Technological, Environmental, Legal).
- Locate sector-specific regulation updates or trade policies.
- Find data on customer segment buying behaviors and technology adoption.

**Deliverable:**
- `market/research-log.md` containing search queries, URLs visited, and key notes per source.

### 2. Calculate TAM

**Dependencies:**
- **Phase 3: Solution:** Use the ARPU (Annual Revenue Per User) from the pricing tiers.

Estimate the **Total Addressable Market (TAM)** using the `tam-sam-som-calculator` methodology.

- **Definition:** The total market demand for the product or service category if you captured 100% of potential customers with no constraints.
- **Top-Down Approach:** Find total market revenue from reliable industry reports (Gartner, Statista, World Bank, etc.).
- **Bottom-Up Approach:** `TAM = Total number of potential customers in the global market × Average Annual Revenue Per User (ARPU)`.
- **Validation:** Compare top-down and bottom-up figures; explain any significant discrepancies.
- **Citations:** Every data point MUST be backed by a source (URL + Date).
- **Deliverable:** `market/tam.md` containing the population data, ARPU, calculation math, and source citations.

### 3. Calculate SAM

**Dependencies:**
- **Phase 2: Problem & Opportunity:** Filter the TAM by the specific target segments and personas identified.
- **Phase 3: Solution:** Use the finalized product-market fit criteria and pricing tiers.

Estimate the **Serviceable Available Market (SAM)** by applying realistic constraints to the TAM.

- **Definition:** The segment of TAM that your company can realistically target with your current product, geography, and channels.
- **Segmentation Filters:**
    - **Geography:** Specify the target regions (e.g., "US and EU only").
    - **Firmographics/Demographics:** Apply size filters (e.g., "SMBs with 10-50 employees").
    - **Product Fit:** Filter by users who have the specific problem identified in Phase 2.
- **Formula:** `SAM = Total number of potential customers in reachable target segments × ARPU`.
- **Assumptions:** Document key assumptions (e.g., "Assumes 70% of targets prioritize cloud-first solutions").
- **Deliverable:** `market/sam.md` containing the SAM estimate, segmentation logic, and population counts.

### 4. Calculate SOM

**Dependencies:**
- **Phase 9: Go-To-Market:** Use the sales capacity and marketing budget constraints to estimate reachable capture.
- **Phase 8: Competition:** Account for competitor market share in the target segments.
- **Phase 12: Operations (Internal):** Ground projections in current team size and resource availability.

Estimate the **Serviceable Obtainable Market (SOM)** for the short-to-medium term.

- **Definition:** The portion of SAM you can realistically capture in the next 1-3 years, accounting for competitive intensity and GTM capacity.
- **Market Share Logic:** SOM should typically be 1-20% of SAM in Year 1-3. Explain why this share is realistic (e.g., "First-mover advantage in niche segment").
- **GTM Capacity Tracking:**
    - **Sales Capacity:** Max customers reachable per month by the sales team.
    - **Marketing Conversion:** Expected lead-to-customer conversion rates.
    - **Budget Constraints:** Marketing spend required to acquire the SOM population.
- **Year 1-3 Projections:** Provide a table showing expected customer count and revenue for the first three years.
- **Deliverable:** `market/som.md` containing Year 1-3 capture projections, market share assumptions, and GTM capacity math.

**Dependencies:**
- **Sub-task 1 (Market Research):** Use the qualitative gathered data regarding buyer behavior and channels.
- **Phase 1: Research:** Use industry sub-sector context.

Describe the market landscape:
- Industry lifecycle stage (emerging, growth, mature, declining)
- Customer segments and buying behavior
- Distribution channels and value chain
- Seasonality and cyclicality
- Technology adoption curve position
- Key success factors

**Dependencies:**
- **Sub-task 1 (Market Research):** Use CAGR reports and historical data to extract growth drivers.
- **Phase 14: Insight:** Align growth forecasts with identified timing catalysts.

Analyze growth trends:
- Historical growth rate (5–10 year trend)
- Projected growth rate (3–5 year forecast)
- Growth drivers and catalysts
- Growth inhibitors and risks
- Regional variations in growth

### 7. Write PESTEL Analysis

**Dependencies:**
- **Sub-task 1 (Market Research):** Use macro-trend data and regulatory updates.
- **Phase 1: Research:** Use initial sector-specific intelligence.

Analyze macro-environmental factors:

| Factor | Analysis | Impact | Opportunity/Threat |
|---|---|---|---|
| **Political** | Regulations, trade policies, government stability, tax policy | | |
| **Economic** | GDP growth, inflation, exchange rates, interest rates, unemployment | | |
| **Social** | Demographics, cultural trends, education, lifestyle, health consciousness | | |
| **Technological** | Innovation rate, technology spending, automation, digital transformation, AI adoption | | |
| **Environmental** | Climate change, sustainability, carbon footprint, resource scarcity, green policies | | |
| **Legal** | Compliance, IP rights, employment laws, health/safety regulations, consumer protection | | |

**Dependencies:**
- **Sub-task 1 (Market Research):** Use identify supplier and buyer concentrations.
- **Phase 8: Competition:** Incorporate direct/indirect competitor density and product differentiation levels.

Assess industry competitive dynamics:

| Force | Intensity | Key Factors |
|---|---|---|
| **Threat of New Entrants** | Low/Med/High | Barriers to entry, capital requirements, economies of scale, brand loyalty |
| **Bargaining Power of Suppliers** | | Supplier concentration, switching costs, substitute inputs |
| **Bargaining Power of Buyers** | | Buyer concentration, price sensitivity, switching costs, information availability |
| **Threat of Substitutes** | | Substitute availability, relative price-performance, switching costs |
| **Competitive Rivalry** | | Number of competitors, industry growth, product differentiation, exit barriers |

**Overall assessment:** Industry attractiveness rating with strategic implications.

---

## Phase Validation Checklist

- [ ] Market research documented in `market/research-log.md`
- [ ] **TAM estimated with population data and cited sources.**
- [ ] **SAM estimated with segmentation logic and cited sources.**
- [ ] **SOM estimated with Year 1-3 capture projections and GTM assumptions.**
- [ ] Market characteristics and lifecycle stage defined
- [ ] Growth rate projected with drivers and inhibitors
- [ ] PESTEL analysis covers all six dimensions
- [ ] Five forces analysis completed with strategic implications
