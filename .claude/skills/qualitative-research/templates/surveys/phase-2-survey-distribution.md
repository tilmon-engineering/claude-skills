# Data Collection - Survey Distribution & Monitoring

**Session:** [session-name]
**Date:** [YYYY-MM-DD]
**Phase:** 2 - Data Collection (Survey Method)

---

## Pre-Launch Checklist

**Before distributing survey, verify:**

- [ ] Pilot test completed and survey revised based on feedback
- [ ] Survey platform tested (all questions display correctly)
- [ ] Survey link is shareable and accessible
- [ ] Logic/branching tested (if applicable)
- [ ] Response export tested (can you download responses?)
- [ ] Consent language reviewed
- [ ] Thank you screen includes all necessary information
- [ ] Incentive delivery method ready (if applicable)
- [ ] Recruitment messages drafted
- [ ] Reminder messages drafted
- [ ] Launch date confirmed

---

## Distribution Plan

### Launch Details

**Survey URL:** [Insert survey link]

**Launch date:** [YYYY-MM-DD]

**Close date:** [YYYY-MM-DD] ([N] days open)

**Target responses:** [N]

---

### Recruitment Message Templates

**Initial Recruitment Message:**

Subject: [Invitation to participate in research on [topic]]

"Dear [Name / Community],

I'm conducting research on [topic] to understand [goal]. I'm seeking input from people who [target audience description].

If this describes you, I would greatly appreciate [X] minutes of your time to complete a brief survey. The survey asks open-ended questions about your experiences with [topic].

Your responses will be [anonymous/confidential] and will help [purpose/impact].

[If incentive: As a thank you for your time, [incentive details].]

Survey link: [URL]

The survey will remain open until [date].

Thank you for considering this request!

[Your name / role / affiliation]"

---

**Reminder 1 (3-5 days after launch):**

Subject: [Gentle reminder: Research survey on [topic]]

"Dear [Name / Community],

A few days ago, I sent an invitation to participate in a survey about [topic]. If you've already completed it, thank you!

If you haven't had a chance yet, I would still greatly appreciate your input. The survey takes approximately [X] minutes and asks about your experiences with [topic].

Survey link: [URL]

The survey will close on [date].

Thank you!

[Your name]"

---

**Reminder 2 (7-10 days after launch):**

Subject: [Final reminder: Survey closes [date]]

"Dear [Name / Community],

This is a final reminder that the survey on [topic] will close on [date].

If you've already completed it, thank you so much for your thoughtful responses.

If not, there's still time to share your insights: [URL]

Your perspective is valuable to this research.

Thank you!

[Your name]"

---

### Distribution Channels

**Channel 1:** [e.g., Email list]
- **Recipients:** [N people]
- **Sent:** [YYYY-MM-DD]
- **Open rate:** [X%] (if tracked)
- **Click rate:** [X%] (if tracked)

**Channel 2:** [e.g., LinkedIn post]
- **Audience:** [Description]
- **Posted:** [YYYY-MM-DD]
- **Reach:** [N people] (if tracked)

**Channel 3:** [e.g., Community forum, Slack group, etc.]
- **Audience:** [Description]
- **Posted:** [YYYY-MM-DD]
- **Reach:** [N people] (if tracked)

---

## Response Monitoring

### Daily Response Tracking

**Goal:** Monitor response rate and quality to make adjustments if needed.

| Date | Total Responses | New Today | Response Rate | Avg Completion Time | Notes |
|------|----------------|-----------|---------------|-------------------|--------|
| [MM-DD] | [N] | [N] | [X%] | [M] min | [Any observations] |
| [MM-DD] | [N] | [N] | [X%] | [M] min | |
| [MM-DD] | [N] | [N] | [X%] | [M] min | |

**Response rate calculation:**
[Total responses] / [Total invitations sent] × 100 = [X]%

---

### Response Quality Spot Checks

**Purpose:** Monitor if respondents are providing detailed, thoughtful responses.

**Check frequency:** Daily for first 3 days, then every 2-3 days

**What to check:**

1. **Response length:**
   - Are open-ended responses detailed (multiple sentences) or superficial (one word)?
   - If superficial: Consider adding more prompts/examples to questions

2. **Response relevance:**
   - Are respondents answering the actual question or going off-topic?
   - If off-topic: Question might be unclear - consider clarification

3. **Bot/spam responses:**
   - Look for nonsensical text, repeated patterns, or obvious spam
   - Remove these responses before analysis

4. **Incomplete responses:**
   - How many people start but don't finish?
   - Where do they drop off? (May indicate survey too long or question too difficult)

**Quality assessment:** [Good / Acceptable / Concerning]

**Actions taken based on quality:**
- [e.g., "Added more context to Q5 prompt" or "No changes needed"]

---

### Response Rate Interventions

**If response rate is lower than expected, consider:**

1. **Send reminder earlier than planned**
   - [Action taken / Date sent]

2. **Post in additional channels**
   - [Where? / Date posted]

3. **Increase incentive** (if applicable and ethical)
   - [Original: X / Increased to: Y / Date changed]

4. **Extend survey open period**
   - [Original close date / New close date]

5. **Personalize recruitment outreach**
   - [Approach: e.g., direct messages vs mass email]

**Intervention log:**

| Date | Intervention | Reason | Result |
|------|-------------|--------|--------|
| [MM-DD] | [What you did] | [Why] | [Impact on response rate] |

---

## Response Data Management

### Export Schedule

**Export frequency:** [Daily / Every 3 days / Weekly]

**Export location:** `analysis/qualitative-research/[session-name]/raw-data/`

**Export format:** [CSV / Excel / JSON]

**Filename convention:** `survey-responses-[YYYY-MM-DD].csv`

**Export log:**

| Date | Filename | Responses Included | Notes |
|------|----------|-------------------|-------|
| [MM-DD] | survey-responses-[date].csv | [N] responses | [Any issues?] |

---

### Data Cleaning Checklist

**Before analysis, review responses for:**

- [ ] **Duplicate responses:** Same person submitted multiple times
  - **Action:** Keep most complete version, remove duplicates
  - **Log:** [N duplicates removed]

- [ ] **Bot/spam responses:** Nonsensical or clearly automated
  - **Action:** Remove from dataset
  - **Log:** [N spam responses removed]

- [ ] **Incomplete responses:** Started but didn't finish
  - **Decision:** [Include partial responses if they answered core questions? Or exclude?]
  - **Log:** [N incomplete responses - action taken]

- [ ] **Out-of-scope responses:** Respondent doesn't meet inclusion criteria
  - **Action:** Remove from dataset (unless insights still relevant)
  - **Log:** [N out-of-scope removed]

- [ ] **Identifying information:** Check for names, emails, etc. in open-ended responses
  - **Action:** Redact if responses should be anonymous
  - **Log:** [N responses redacted]

**Final cleaned dataset:**
- **Original responses:** [N]
- **Removed:** [N]
- **Final dataset:** [N responses]
- **Saved as:** `survey-responses-cleaned-[YYYY-MM-DD].csv`

---

## Demographic/Context Summary

**Purpose:** Understand who responded to assess sample diversity.

**Respondent characteristics (from context questions):**

| Characteristic | Count | % of Total |
|---------------|-------|-----------|
| [Category 1 - e.g., "Industry: Tech"] | [N] | [X%] |
| [Category 1 - e.g., "Industry: Healthcare"] | [N] | [X%] |
| [Category 2 - e.g., "Role: Manager"] | [N] | [X%] |
| [Category 2 - e.g., "Role: Individual contributor"] | [N] | [X%] |

**Diversity assessment:**
- [Did you get the diversity you were aiming for?]
- [What perspectives might be missing?]
- [Is sample representative of target population?]

**Limitations:**
- [e.g., "Over-represented tech industry, under-represented manufacturing"]
- [e.g., "Mostly senior roles, few junior perspectives"]

---

## Follow-Up Interview Recruitment

**If Phase 1 included optional follow-up consent:**

**Respondents who opted in:** [N]

**Selection criteria for follow-up:**
- [How will you select who to interview? Rich responses? Diversity? Contradictory cases?]

**Follow-up recruitment message:**

"Dear [Name],

Thank you for completing the survey on [topic] and for indicating willingness to participate in a follow-up conversation.

I would love to explore your experiences in more depth through a brief [30-45] minute interview. We would discuss [topics based on their survey responses].

Are you available for a [video call / phone call / in-person] conversation in the next [timeframe]?

[Provide scheduling link or ask for availability]

[If additional incentive for interview: As a thank you, [incentive details].]

Thank you for considering this!

[Your name]"

**Follow-up interview log:**

| Respondent ID | Survey Response Quality | Follow-up Invitation Sent | Response | Interview Scheduled |
|--------------|------------------------|-------------------------|----------|-------------------|
| R001 | [Rich / Diverse perspective / etc.] | [Date] | [Yes/No] | [Date/Time or N/A] |
| R002 | | | | |

---

## Reflexivity Check-In

**After distribution, before analysis, reflect:**

### Response Patterns

**What surprised me about the responses:**
[Anything unexpected? Contradicted your assumptions?]

**What confirmed my assumptions:**
[Did responses align with what you expected? Be honest about confirmation bias.]

**New questions raised:**
[What themes emerged that you didn't anticipate?]

### Distribution Process

**What worked well:**
[Which recruitment channels were effective? What messaging resonated?]

**What didn't work:**
[Low response from certain channels? Messaging that fell flat?]

**What I would do differently:**
[If you were to do this again, what would you change?]

### Bias Check

**Selection bias concerns:**
[Who responded vs who didn't? Are respondents systematically different from non-respondents?]

**Incentive effects:**
[Did incentive attract people genuinely interested in topic or just incentive-seekers?]

**My interpretation lens:**
[What assumptions am I bringing to initial reading of responses?]

---

## Phase 2 Checkpoint Verification

**Before proceeding to Phase 3, verify:**

- [ ] Survey distributed through planned channels
- [ ] Reminders sent as planned
- [ ] Target response goal achieved (or justification for stopping)
- [ ] Response quality monitored and documented
- [ ] All responses exported and backed up
- [ ] Data cleaning completed (duplicates, spam, incomplete removed)
- [ ] Final cleaned dataset saved
- [ ] Demographic summary completed
- [ ] Sample diversity assessed
- [ ] Limitations of sample documented
- [ ] Reflexivity check-in completed
- [ ] All files saved to `02-data-collection-log.md`
- [ ] All response data saved to `raw-data/survey-responses-cleaned-[date].csv`

**Checkpoint status:** [PASS / FAIL]

**If PASS:** Proceed to Phase 3 - Data Familiarization
**If FAIL:** Complete missing requirements above before proceeding

---

## Survey Closure Announcement (Optional)

**If appropriate, announce results/thank you to community:**

"Thank you to everyone who participated in the survey on [topic]!

We received [N] responses from [description of respondents]. Your insights have been incredibly valuable.

[If sharing findings: We expect to have initial findings by [date]. If you'd like to receive a summary, please [contact/sign up method].]

Thank you again for your time and thoughtful contributions to this research.

[Your name]"

---

## Distribution Metrics Summary

**Final statistics:**

- **Survey open:** [N] days (from [date] to [date])
- **Total invitations sent:** [N]
- **Total responses:** [N]
- **Overall response rate:** [X%]
- **Average completion time:** [M] minutes
- **Completion rate:** [X%] (started vs finished)
- **Follow-up interview opt-ins:** [N]

**Most effective channel:** [Channel name] ([X%] response rate)

**Least effective channel:** [Channel name] ([X%] response rate)

**Learnings for future surveys:**
1. [Learning 1]
2. [Learning 2]
3. [Learning 3]
