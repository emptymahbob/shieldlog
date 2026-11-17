# Reflection (200–300 words)

Copy this into a PDF or DOCX for LMS upload. Edit in your own words before submitting.

---

Building ShieldLog with an agentic workflow worked best when I started from a written plan: entities first (`Finding`), then dashboard counts, then CRUD forms. Keeping `CLAUDE.md` and `docs/DATA_MODEL.md` in the repo gave the agent clear commands and boundaries, which reduced random refactors. The `verify-finding` skill was useful after UI changes because it forced a concrete click-through checklist instead of assuming the form worked.

Things went wrong when prompts were vague—for example, asking to “improve the UI” without saying which page or acceptance criteria. The agent sometimes over-edited CSS or suggested features outside scope (auth, uploads). I fixed that by tightening the request: name the file, describe the expected result, and re-run the verification skill. Seed data also helped; empty screens made it harder to spot broken badges.

Next time I would plan parallel work earlier: one branch for a dashboard status filter and another for mobile polish, then merge once. I would also attach Playwright (or browser MCP) checks from the start so verification is repeatable. Overall, the plan → implement → verify loop was more important than generating lots of code quickly, and the cybersecurity theme stayed appropriately defensive by focusing on finding intake rather than offensive tooling.

---

Word count target: 200–300. Adjust details to match what you personally did (branches, MCP, screenshots).
