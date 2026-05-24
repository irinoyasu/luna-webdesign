# Research Phase Reference

## Inputs

**Process Dependencies:**
- **User Context (Mandatory):** Initial vision, project scope, and company background provided in the chat.
- **Existing Files:** Any pitch decks, whitepapers, or website URLs provided as starting points.

**You MUST synthesize information from initial user requirements and any previously gathered data before drafting.** 
1. **Existing Workspace Data:** Always check the output directory (`{output_folder}/businessplan-writing/`) for any existing research logs or project documents from previous runs. If a project folder already exists, you MUST parse its contents to avoid duplicating research.
2. **User Context:** Incorporate any initial vision, existing pitch decks, or founder background provided by the user.

## Purpose

Research the company context, evaluate the market landscape, and analyze target customers deeply. This phase ensures you enter the problem definition phase with genuine insight — not assumptions. 

**The single most important phase.** Your business plan must demonstrate that you understand the target market and the underlying problems better than anyone else.

## Sub-Task Index

| # | Sub-Task | Output File | Description |
|---|---|---|---|
| 1 | Company & Founding Context | `research/company-context.md` | Clear definition of the founding team, their background, and their core thesis |
| 2 | Customer Deep Search | `research/customer-research.md` | Web-researched deep dive into target customer segments and demographics |
| 3 | Competitive Landscape Deep Search | `research/competitive-landscape.md` | Web-researched competitive intelligence: direct/indirect competitors, positioning, pricing, strengths/weaknesses |

---

## Detailed Sub-Task Instructions

### 1. Company & Founding Context

Before defining external factors, establish the internal baseline. Who are the founders, and what are their unique advantages?

**Instructions:**

1. **Profile the Core Entity:**
   | Field | Detail |
   |---|---|
   | Company name / Project name | |
   | Industry & sub-sector | |
   | Vision / Core Thesis | |
   | Unfair advantages | |

2. **Map the Founding Team:**
   | Role | Background | Unique Experience |
   |---|---|---|
   | CEO / Founder | | |
   | Technical Lead | | |
   | Go-to-Market Lead | | |

**Dependencies:**
- **User Context:** Initial vision, project scope, and company background provided in the chat.
- **Project Scope:** Initial hypothesis on the release timing of product (MVP vs. full launch).

**Outputs:**
- `research/company-context.md` containing the strategic context and team baseline.

---

### 2. Customer Deep Search

**Dependencies:**
- **Sub-task 1 (Context):** Use the core thesis, industry focus, and vision to guide customer research parameters.
- **Process Dependency:** Initial user context regarding target geographies or known customer types.

Do NOT rely on assumptions. Perform active web research to build a fact-based picture of the target buyers and users.

**Instructions:**

1. **Research Target Customer Segments (use active web research):**
   Identify the primary and secondary customer segments.
   | # | Segment Name | Target Demographic / Firmographic | Pain Points | Source URL |
   |---|---|---|---|---|
   | 1 | | | | |

   For each major segment, document:
   | Field | Detail |
   |---|---|
   | Segment name | |
   | Segment size estimating metrics | |
   | Current alternatives they use | |
   | Willingness to pay / Buying power | |

**Outputs:**
- `research/customer-research.md` containing detailed segment profiles with source URLs.

---

### 3. Competitive Landscape Deep Search

**Dependencies:**
- **Sub-task 1 (Context):** Use the core thesis and "unfair advantages" to identify competitors in the same or adjacent spaces.
- **Sub-task 2 (Customer):** Use the identified customer pain points and current alternatives to find both direct and indirect competitors.

Do NOT rely on general knowledge about competitors. Perform active web research to build a fact-based competitive picture. This is essential for crafting differentiated positioning.

**Instructions:**

1. **Identify Competitors (use active web research):**
   Search for companies that the target customer currently uses. Include:
   - **Direct competitors:** Companies offering the exact same product/service.
   - **Indirect competitors / Alternatives:** Different approaches to solve the same problem.

   | Competitor | Type (Direct / Indirect) | Source URL |
   |---|---|---|
   | | | |

2. **Profile Each Competitor (use active web research and URL reading):**
   For each identified competitor, document:
   | Field | Detail |
   |---|---|
   | Company name | |
   | Core product/service offering | |
   | Pricing model | |
   | Target market | |
   | Key strengths | |
   | Key weaknesses / Gaps | |

3. **Competitive Comparison Matrix:**
   Create a side-by-side comparison.
   | Dimension | Us | Competitor A | Competitor B |
   |---|---|---|---|
   | Pricing | | | |
   | Features | | | |
   | Go-to-Market | | | |

**Outputs:**
- `research/competitive-landscape.md` containing competitor profiles, matrix, and web sources.

---

## Phase Validation Checklist

- [ ] Company and founding context documented.
- [ ] **Target customers researched and profiled via web search.**
- [ ] **Competitive landscape researched via web search (not assumed).**
- [ ] **Competitor profiles documented with source URLs.**
- [ ] **Competitive comparison matrix completed.**
- [ ] Phase deliverables stored in `research/` folder.
