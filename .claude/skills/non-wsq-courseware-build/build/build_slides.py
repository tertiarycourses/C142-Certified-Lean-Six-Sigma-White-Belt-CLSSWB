#!/usr/bin/env python3
"""Build the C142 CLSSWB slide deck — all-white Tertiary house style, DMAIC order.

NON-WSQ mirror of the WSQ counterpart's full-depth deck: the same concept
teaching slides (concepts.py), the same visual components (components.py), the
same labs — with the funded-course layer removed. No digital attendance, no
TRAQOM, no assessment/briefing slides, no TSC slide, no 75% attendance rule;
the "How You'll Learn" flow takes the place of the assessment block.

Structure:
  Cover → Admin (trainers x2, ice-breaker, ground rules, LMS, lesson plan,
  outcomes, course outline, How You'll Learn)
  → Foundations → D → M → A → I → C  (each phase: concept slides then its labs)
  → Wrap-up → Certificate & Support → Thank You

Content comes entirely from course_data.py + data_domainN.py + concepts.py so
the PPT, LP, LG and labs stay 100% aligned.
"""
import os
import re
import sys
import glob as _glob
import importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import course_data as C
from components import (Deck, BLUE, TEAL, AMBER, RED, VIOLET, INK, GREY, LIGHT,
                        WHITE, LINE, DMAIC_COLORS)
import concepts

# Import data_domain1..N dynamically so a course can have ANY number of domains.
ACTIVITIES = []
for f in sorted(_glob.glob(os.path.join(HERE, "data_domain[0-9]*.py")),
                key=lambda p: int(re.search(r"(\d+)", os.path.basename(p)).group(1))):
    n = int(re.search(r"(\d+)", os.path.basename(f)).group(1))
    mod = importlib.import_module(os.path.basename(f)[:-3])
    ACTIVITIES += getattr(mod, f"DOMAIN{n}", [])


def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO = _find_repo(HERE)
ASSETS = os.path.join(REPO, "courseware", "assets")


def asset(name):
    p = os.path.join(ASSETS, name)
    return p if os.path.exists(p) else None


d = Deck(C)

# ============================================================ COVER
d.cover(logo=asset("tertiary-logo.png"))

# ============================================================ ADMIN
d.section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "")

# --- two trainer profile cards ---
d.trainer_slide("YOUR TRAINER · GENERAL", "Your Trainer",
                "General Trainer template —\nto be completed by the trainer",
                [("Name", ""), ("Title / Designation", ""), ("Qualifications", ""),
                 ("Areas of expertise", ""), ("Training & industry experience", ""), ("Contact", "")],
                initials="?", accent=GREY, photo=asset("trainer_template.png"))
d.trainer_slide("YOUR TRAINER", C.TRAINER,
                "Principal Trainer\nTertiary Infotech Academy Pte. Ltd.",
                [("Role", "Principal Trainer, Tertiary Infotech Academy Pte. Ltd."),
                 ("Qualifications", "PhD; Certified Lean Six Sigma practitioner and trainer."),
                 ("Delivers", "Professional courses on Lean Six Sigma, quality management and data analytics."),
                 ("Experience", "Process improvement across manufacturing, service and technology sectors."),
                 ("Founder", "Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
                initials="AA", accent=BLUE, photo=asset("trainer_profile.png"))

d.content("Let's Know Each Other", [
    "Your name, organisation and role.",
    "Your experience with process improvement or quality work (if any).",
    "One process at work that frustrates you — we may use it as your course scenario.",
], kicker="ICE-BREAKER")

d.tile_grid("Ground Rules", [
    "Set your mobile phone to silent mode.",
    "Participate actively — no question is too small.",
    "Mutual respect: agree to disagree.",
    "One conversation at a time.",
    "Be punctual; return from breaks on time.",
    "Ask early — every lab builds on the one before it.",
], kicker="HOUSEKEEPING", cols=2, size=15)

# --- Download course material ---
lms = asset("lms_download.png")
if lms:
    d.image_slide("Download Your Course Material", lms,
                  kicker="COURSE PORTAL · lms-tms.tertiaryinfotech.com",
                  caption="Log in to lms-tms.tertiaryinfotech.com to download the slides, Learner Guide and lab files.")
else:
    d.flow_h("Download Your Course Material", [
        "Go to lms-tms.tertiaryinfotech.com",
        "Sign in with the account details given in class",
        "Open this course from your dashboard",
        "Download the slides, Learner Guide and lab files",
        "Keep them open — the labs use them all day",
    ], kicker="COURSE PORTAL · lms-tms.tertiaryinfotech.com", color=TEAL)

# --- Lesson plan ---
d.two_col("Lesson Plan — 1 Day, 8 Hours",
          [("Morning — Foundations and Define", 0),
           ("Welcome · Introductions · Ground rules", 1),
           ("Foundations: Quality, Lean, Six Sigma, Lean Six Sigma", 1),
           ("Belt roles and the DMAIC roadmap", 1),
           ("DEFINE: VOC, CTQ, problem statement, SMART goal", 1),
           ("Lab 1 — Define: requirements and problem statement", 1),
           ("MEASURE: process mapping, SIPOC, data, the 8 wastes", 1),
           ("Lab 2 — Measure: map the process, spot the waste", 1)],
          [("Afternoon — Analyze, Improve, Control", 0),
           ("ANALYZE: root cause, 5 Whys, Fishbone, Pareto", 1),
           ("Lab 3 — Analyze: find the root cause", 1),
           ("IMPROVE: solutions, 5S, mistake proofing, piloting", 1),
           ("Lab 4 — Improve: choose and pilot a countermeasure", 1),
           ("CONTROL: control plan, visual management, handover", 1),
           ("Lab 5 — Control: hold the gain and hand over", 1),
           ("Course recap and Q&A", 1)],
          kicker="SCHEDULE · 9:30am-6:30pm with a 1-hour lunch",
          lhead="Morning", rhead="Afternoon")

d.tile_grid("Learning Outcomes", [
    ("LO1 — Core concepts", "Describe quality, Lean, Six Sigma and the belt roles in an improvement team."),
    ("LO2 — The DMAIC roadmap", "Explain the five phases of DMAIC and what happens in each."),
    ("LO3 — Define", "Identify customer requirements and a clear problem statement."),
    ("LO4 — Measure", "Describe how a process is mapped and measured, and identify the 8 wastes."),
    ("LO5 — Analyze", "Identify likely causes using 5 Whys and Fishbone analysis."),
    ("LO6 — Improve & Control", "Describe actions that fix a cause and hold the gain."),
], kicker="WHAT YOU'LL ACHIEVE", cols=2, size=14)

d.dmaic_wheel("Course Outline — We Follow DMAIC End to End", [
    ("D", "Define", ["VOC and CTQ", "Problem statement", "SMART goal, charter", "Lab 1"]),
    ("M", "Measure", ["Process mapping, SIPOC", "Types of data", "The 8 wastes", "Lab 2"]),
    ("A", "Analyze", ["Root cause", "5 Whys, Fishbone", "Pareto, variation", "Lab 3"]),
    ("I", "Improve", ["Generating solutions", "5S, mistake proofing", "Standard work, pilot", "Lab 4"]),
    ("C", "Control", ["Control plan", "Visual management", "SOPs and handover", "Lab 5"]),
], kicker="COURSE ROADMAP")

# --- How You'll Learn (in place of the assessment block) ---
d.flow_h("How You'll Learn", [
    "Trainer demonstrates the concept",
    "You apply it in the hands-on lab",
    "Check your work against the lab's verify step",
    "Each lab builds on the one before it",
    "Recap and Q&A close every phase",
], kicker="LEARNING BY DOING", color=TEAL)

# ============================================================ FOUNDATIONS
concepts.foundations(d)

# ============================================================ DMAIC PHASES + LABS
# Topic numbering: 1 = Foundations, 2..6 = Define..Control.
PHASE_FN = {
    2: concepts.define_phase,
    3: concepts.measure_phase,
    4: concepts.analyze_phase,
    5: concepts.improve_phase,
    6: concepts.control_phase,
}
PHASE_NAME = {2: "DEFINE", 3: "MEASURE", 4: "ANALYZE", 5: "IMPROVE", 6: "CONTROL"}
TOPIC_ACTS = {t["num"]: [a for a in ACTIVITIES if a["topic"] == t["num"]] for t in C.TOPICS}


def render_labs(acts, phase_label):
    for a in acts:
        opt = a.get("elective", False)
        tag = f"LAB {a['num']}"
        d.activity_overview(tag, a["title"], a["desc"], a["build"], a["services"],
                            kicker=f"{phase_label} · HANDS-ON", elective=opt)
        steps = a["steps"]
        total = len(steps)
        short = a["title"][:38]
        # Awareness-level course: two steps per slide keeps the one-day deck tight
        # while every step stays on screen for the learner.
        numbered = [(i, instr) for i, (instr, _cmd) in enumerate(steps, 1)]
        for j in range(0, len(numbered), 2):
            d.step_pair_slide(f"LAB {a['num']} · {short}", a["title"],
                              numbered[j:j + 2], total)
        d.test_slide(a["title"], a["test"], kicker=f"LAB {a['num']} · VERIFY")


# Foundations labs (topic 1) come right after the foundations concepts
render_labs(TOPIC_ACTS.get(1, []), "FOUNDATIONS")

for t in C.TOPICS:
    if t["num"] == 1:
        continue
    phase = PHASE_NAME[t["num"]]
    idx = t["num"] - 2
    col = DMAIC_COLORS[idx % len(DMAIC_COLORS)]
    d.section(f"DMAIC · {phase}", t["title"], t["code"], t["subtitle"])
    d.tile_grid(f"Key Concepts — {phase.title()}", t["concepts"],
                kicker=f"{phase} · {t['weighting']} OF THE COURSE", cols=2, size=14, accent=col)
    # teaching content for this phase
    PHASE_FN[t["num"]](d)
    # labs that belong to this phase
    acts = TOPIC_ACTS.get(t["num"], [])
    if acts:
        core = [a for a in acts if not a.get("elective")]
        opts = [a for a in acts if a.get("elective")]
        rows = []
        for a in core:
            rows.append((f"Lab {a['num']} — {a['title'][:46]}", a["build"][:70]))
        for a in opts:
            rows.append((f"Lab {a['num']} (elective) — {a['title'].replace('Elective — ', '')[:40]}",
                         a["build"][:70]))
        d.tile_grid(f"Hands-On Labs — {phase.title()}", rows,
                    kicker="WHAT YOU'LL DO", cols=1, size=14, accent=col)
        render_labs(acts, f"DMAIC · {phase}")
    # phase recap
    d.content(f"Recap — {phase.title()}",
              [c[0] + " — " + c[1] for c in t["concepts"]],
              kicker="PHASE RECAP", size=15)

# ============================================================ WRAP-UP
d.section("WRAP-UP", "Course Summary & Next Steps", "")
d.dmaic_wheel("What You Achieved — The Full DMAIC Journey", [
    ("D", "Define", ["Captured VOC and CTQ", "Wrote the problem statement", "Set a SMART goal", "Agreed the scope"]),
    ("M", "Measure", ["Built the SIPOC", "Mapped the process", "Classified the data", "Tallied the 8 wastes"]),
    ("A", "Analyze", ["Ran the 5 Whys", "Built the Fishbone", "Read the Pareto chart", "Shortlisted the causes"]),
    ("I", "Improve", ["Generated countermeasures", "Screened on impact/effort", "Wrote standard work", "Planned the pilot"]),
    ("C", "Control", ["Built the control plan", "Set visual management", "Wrote the SOP", "Handed over"]),
], kicker="YOUR IMPROVEMENT PACKAGE")

d.tile_grid("Your Integrated Improvement Package", [
    ("VOC and CTQ table", "Customer requirements translated into measurable CTQs."),
    ("Problem statement and goal", "A clear problem statement, a SMART goal and an agreed scope."),
    ("SIPOC and process map", "The BrewBean Cafe process as it really runs, with times against each step."),
    ("Waste tally sheet", "Every observed waste tagged to one of the eight DOWNTIME types."),
    ("5 Whys and Fishbone", "A cause chain and a categorised cause diagram for your problem."),
    ("Countermeasure and pilot plan", "One selected countermeasure with standard work and a one-week pilot."),
    ("Control plan and SOP", "Measure, target, frequency, owner, reaction plan and handover."),
    ("One-page summary", "The complete DMAIC story from problem to handover."),
], kicker="WHAT YOU BUILT", cols=2, size=13)

d.tile_grid("Final Readiness Checklist", [
    "Can you define quality, Lean, Six Sigma and Lean Six Sigma in your own words?",
    "Can you name the five DMAIC phases and say what each one delivers?",
    "Can you describe the belt roles and where the White Belt contributes?",
    "Can you trace a VOC statement through to a measurable CTQ?",
    "Can you write a problem statement that contains no solution?",
    "Can you name the eight wastes and give a workplace example of each?",
    "Can you explain the difference between a symptom and a root cause?",
    "Can you run a 5 Whys chain and sort causes on a Fishbone diagram?",
    "Can you describe what a control plan needs to hold a gain?",
], kicker="SELF-CHECK", cols=1, size=14, accent=TEAL)

d.tile_grid("Continuing Your Lean Six Sigma Journey", [
    ("Apply it at work", "Spot and log the eight wastes in your own area within 30 days."),
    ("Yellow Belt", "The next step — supports DMAIC projects and the data analysis behind them."),
    ("Keep the templates", "Your lab outputs are reusable templates for real improvement work."),
    ("Join the conversation", "Raise improvement ideas in your team; small changes spread by example."),
], kicker="NEXT STEPS", cols=2, size=15, accent=AMBER)

# ============================================================ CLOSE
d.content("Certificate & Support", [
    "A certificate of completion is awarded at the end of the course.",
    "Email: enquiry@tertiaryinfotech.com",
    "Tel / WhatsApp: +65 6100 0613",
], kicker="AFTER THE COURSE")

d.big_statement("Thank You!",
                "Go and spot one waste in your own process this month — that is where every improvement starts.",
                "END OF COURSE", color=BLUE)

# ============================================================ TRANSITIONS + SAVE
d.apply_transitions(kind="fade", dur_ms=700)

out = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
d.prs.save(out)
print(f"✅ {out}")
print(f"   {len(d.prs.slides._sldIdLst)} slides")
