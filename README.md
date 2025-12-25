## Volunteer Data Pipeline

This project builds a **shadow source of truth** from noisy, human-generated volunteer data.
It ingests raw CSV data, cleans and normalizes it, enriches member information using AI,
and stores the results in a normalized SQLite database.

---

### Architecture

- **ETL Layer**
  - Ingests raw CSV files
  - Normalizes names and dates
  - Logs invalid or unprocessable records

- **AI Enrichment Layer**
  - Extracts member skills from bio/comments
  - Classifies member persona (Mentor Material, Needs Guidance, Passive)
  - Assigns a confidence score to each classification

- **Truth Layer**
  - Stores normalized data in a SQLite database
  - Maintains relationships between members, skills, and personas
  - Tracks processing status

---

### AI Strategy

A rule-based mock AI is used to simulate LLM behavior for skill extraction and persona classification.
This approach keeps the project free-tier friendly and can be easily replaced with
OpenAI, Gemini, or HuggingFace APIs.

---

### Database Schema

The SQLite database (`volunteer_data.db`) contains the following tables:

- `members`
- `skills`
- `member_skills`
- `persona`

---

### Limitations

- AI confidence scores are heuristic-based
- Persona accuracy depends on the quality of the input bio/comments
- Rule-based enrichment is less flexible than real LLMs

---

### How to Run

```bash
pip install -r requirements.txt
python main.py
