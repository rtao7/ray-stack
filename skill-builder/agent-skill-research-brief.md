# Agent Skill Research Brief

## FILL THESE IN — everything below this line stays fixed

**SKILL_NAME:** [e.g. "copywriter-superhero"]  
**SKILL_DOMAIN:** [the craft/field this skill covers, in plain words — e.g. "copywriting across UX microcopy, marketing copy, and long-form sales copy"]  
**WHY_GENERAL_PURPOSE_MATTERS:** [state if this must work for ANY use case in the domain, not just your brand/company — e.g. "must work for any product, not just Neue Academy"]  
**KNOWN_ADJACENT_SKILLS:** [name any other skill this one might overlap with, so research can find the boundary — e.g. "landing page builder, brand voice"]

---

## FIXED RESEARCH INSTRUCTIONS — do not edit

I am building an AI agent skill (a Claude/Cursor Agent Skill, following the agentskills.io open specification) called {SKILL_NAME}, covering {SKILL_DOMAIN}. {WHY_GENERAL_PURPOSE_MATTERS}

Do deep research and give me a complete technical build strategy, structured exactly as follows. Do not skip any section — I need this to be genuinely technical, not generic advice.

### 1. TRIAGE AXES

Research and identify the 2-4 core variables that change HOW this skill should behave depending on the specific task thrown at it (for example, in copywriting this is copy type, reader awareness level, and traffic temperature; in debugging it might be symptom type, system layer, and reproducibility). Tell me exactly what axes exist in {SKILL_DOMAIN} and why they matter — cite the actual professional discipline/literature this comes from, don't invent it.

### 2. EXISTING FRAMEWORKS AND RULES — DON'T INVENT, FIND WHAT ALREADY EXISTS

Research the established, named frameworks, methods, or rules that professionals in {SKILL_DOMAIN} actually use (e.g. AIDA/PAS/BAB for copywriting, five-whys/root-cause-tracing for debugging, WCAG for accessibility). Build me a lookup table: framework name → what it's for → which triage condition from step 1 it matches. Cite real sources.

### 3. FAILURE-MODE MAPPING

Research the most common ways an AI or a novice gets this domain WRONG by default — the generic, low-quality output that happens without proper structure. For each failure mode, tell me whether the fix is: (a) a prohibition/rule because the failure is skipping a step under pressure, (b) a positive recipe because the failure is wrong SHAPE of output, (c) a required structural template because the failure is an OMITTED element, or (d) a conditional rule because behavior should change based on context. This determines how the skill instructions should actually be written.

### 4. BOUNDARY AGAINST ADJACENT SKILLS

Given {KNOWN_ADJACENT_SKILLS}, research and tell me exactly where {SKILL_NAME} should stop and hand off to a neighboring skill, so there's no duplicated logic.

### 5. TESTING METHOD

Tell me whether this skill is Discipline-type (a rule that could be skipped under pressure, needs adversarial pressure-testing) or Technique/Pattern-type (a how-to method, needs real application scenarios scored against known-good output). Give me the specific test scenarios I should run before considering this skill "done."

### 6. FOLDER AND FILE STRUCTURE

Based on everything above, tell me exactly what files this skill needs: what goes in the main SKILL.md, what heavy reference material belongs in a separate references/ file (and name each file), whether any scripts/ are needed, and what example outputs I should save.

Give me all six sections in full technical depth, with real citations to where these methods/frameworks/standards come from. This research is the foundation — I will take your output and use it to actually build the skill afterward in Cursor.
