"""
SINGLE SOURCE OF TRUTH — Certified Lean Six Sigma White Belt (CLSSWB), C142.

NON-WSQ course: no assessment, no funding/SSG, no TRAQOM, no digital attendance
and no TGS- reference. Mirrored 1:1 from the WSQ counterpart (TGS-2025053210):
the same one-day Six Sigma AWARENESS course, the same DMAIC storyline, the same
five labs (exactly one per DMAIC phase) on the single BrewBean Cafe running
scenario. The 95 minutes previously reserved for the formal evaluation block
are returned to teaching — every lab gets more hands-on time plus a closing
course recap.

Simplification rules (inherited from the White Belt standard):
  * 5 labs, exactly one per DMAIC phase.
  * No sigma-level maths, no DPMO conversion tables, no MSA, no FMEA, no VSM,
    no Kano, no solution-selection matrices, no descriptive statistics.
  * Learners CONTRIBUTE to an improvement team; they do not lead a project.
  * Concepts are explained with plain-language definitions and one worked
    example each, using a single running scenario the whole day.

Content is grounded in "Six Sigma: A Complete Step-by-Step Guide" — The Council
for Six Sigma Certification (CSSC), which defines the White Belt awareness
standard.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Certified Lean Six Sigma White Belt (CLSSWB) Training"
SHORT_TITLE  = "Certified Lean Six Sigma White Belt (CLSSWB) Training"
COURSE_CODE  = "C142"
VERSION      = "v3"
VERSION_DATE = "21 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1
MODE         = "Instructor-led, hands-on Lean Six Sigma labs using the BrewBean Cafe morning rush improvement scenario"

DARK_THEME = False

TRAINER_CERT     = "Certified Lean Six Sigma practitioner — process improvement, quality and data-driven problem solving."
TRAINER_DELIVERS = "Professional short courses on Lean Six Sigma, quality management, data and cloud."

ICE_BREAKER = [
    "Your name and organisation / role.",
    "A process in your work that frustrates you or your customers.",
    "What you want to be able to recognise or improve after this course.",
]

# ------------------------------------------------------------------ outcomes
# Awareness-level verbs (describe / identify / explain / contribute) — NOT the
# practitioner verbs used at Yellow Belt (define / analyse / recommend).
LEARNING_OUTCOMES = [
    "LO1: Describe the core concepts of quality, Lean, Six Sigma and Lean Six Sigma, and the belt roles in an improvement team.",
    "LO2: Explain the five phases of the DMAIC roadmap and what happens in each.",
    "LO3: Identify customer requirements and a clear problem statement in the Define phase.",
    "LO4: Describe how a process is mapped and measured, and identify the eight wastes in the Measure phase.",
    "LO5: Identify likely causes of a problem using 5 Whys and Fishbone analysis in the Analyze phase.",
    "LO6: Describe common improvement and control actions that fix a cause and hold the gain.",
]
LO_TITLES = [
    "Lean Six Sigma Concepts", "The DMAIC Roadmap", "Define the Problem",
    "Measure & the 8 Wastes", "Find the Root Cause", "Improve & Control",
]

# ------------------------------------------------------------------ topics (DMAIC roadmap)
TOPICS = [
    dict(num=1, code="01", title="Lean Six Sigma Foundations", weighting="20%",
         subtitle="Quality · Lean · Six Sigma · Lean Six Sigma · Belt roles · The DMAIC roadmap",
         concepts=[
            ("What is Quality", "Quality is meeting the customer's requirements — not just being free of defects."),
            ("What is Lean", "Lean removes waste so work flows faster to the customer."),
            ("What is Six Sigma", "Six Sigma reduces variation so results become consistent and predictable."),
            ("Lean Six Sigma", "The two combined: faster flow AND fewer defects, decided by data not opinion."),
            ("Belt roles", "White, Yellow, Green, Black and Master Black Belt — who does what on a team."),
            ("The DMAIC roadmap", "Define, Measure, Analyze, Improve, Control — the five-step improvement path."),
         ]),
    dict(num=2, code="02", title="Define — Understand the Problem", weighting="20%",
         subtitle="Voice of the Customer · CTQ · Problem statement · SMART goal · Project charter",
         concepts=[
            ("Voice of the Customer", "Ask customers what they need, and record it in their own words."),
            ("Critical to Quality", "Turn each customer need into something specific you can measure."),
            ("Problem statement", "What is wrong, where, since when, and how big — never the solution."),
            ("SMART goal", "Specific, Measurable, Achievable, Relevant and Time-bound."),
            ("Project charter", "A one-page summary of the problem, goal, scope and team."),
            ("Scope", "Agreeing what is in and out keeps a small project small."),
         ]),
    dict(num=3, code="03", title="Measure — See What Is Really Happening", weighting="20%",
         subtitle="Process mapping · SIPOC · Types of data · Data collection · The eight wastes",
         concepts=[
            ("Process mapping", "Draw the steps as they really happen, not as the manual says."),
            ("SIPOC", "A one-page overview: Suppliers, Inputs, Process, Outputs, Customers."),
            ("Types of data", "Discrete data you count; continuous data you measure on a scale."),
            ("Data collection", "Agree what to record, who records it, and when — before you start."),
            ("Check sheets", "A simple tally form is the easiest reliable way to collect data."),
            ("The eight wastes", "DOWNTIME — Defects, Overproduction, Waiting, Non-utilised talent, Transport, Inventory, Motion, Extra-processing."),
         ]),
    dict(num=4, code="04", title="Analyze — Find the Cause", weighting="20%",
         subtitle="Root cause · 5 Whys · Fishbone diagram · Pareto chart · Variation",
         concepts=[
            ("Symptom vs cause", "Treating the symptom makes the problem come back; treating the cause does not."),
            ("Root cause", "The cause that, once removed, stops the problem recurring."),
            ("5 Whys", "Keep asking 'why?' until you reach something you can actually act on."),
            ("Fishbone diagram", "Sort possible causes into Manpower, Method, Machine, Material and Measurement."),
            ("Pareto chart", "Roughly 80% of the problem usually comes from 20% of the causes."),
            ("Variation", "Some variation is normal in the process; some has a specific assignable cause."),
         ]),
    dict(num=5, code="05", title="Improve — Fix the Cause", weighting="10%",
         subtitle="Generating solutions · 5S · Mistake proofing · Standard work · Piloting",
         concepts=[
            ("Generating solutions", "Brainstorm against the proven cause — never against the symptom."),
            ("Choosing a solution", "Compare ideas on impact, effort and risk before committing."),
            ("5S", "Sort, Set in order, Shine, Standardise, Sustain — a tidy workplace for physical or digital work."),
            ("Mistake proofing", "Poka-Yoke makes the error hard or impossible to make."),
            ("Standard work", "Write the better method down so everyone does it the same way."),
            ("Piloting", "Try the change small first, so mistakes stay cheap."),
         ]),
    dict(num=6, code="06", title="Control — Hold the Gain", weighting="10%",
         subtitle="Control plan · Visual management · SOPs · Team huddles · Handover",
         concepts=[
            ("Why Control matters", "Without Control, processes quietly drift back to the old way."),
            ("Control plan", "What we measure, the target, how often, who owns it, and what to do if it slips."),
            ("Visual management", "Make performance visible so problems are noticed the same day."),
            ("Standard operating procedures", "Written instructions that lock in the improved method."),
            ("Team huddles", "Short regular stand-ups catch problems while they are still small."),
            ("Handover", "Give the improved process back to the people who run it every day."),
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Lean Six Sigma foundations and the full DMAIC roadmap, hands-on",
}

# ------------------------------------------------------------------ schedule
# 480 training minutes (lunch excluded). No assessment blocks — the 95 minutes
# previously reserved for the formal evaluation are returned to teaching: every
# DMAIC lab gets more hands-on time plus a closing course recap.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:30","10:00",30,"admin","Welcome, course introduction and ground rules"),
        ("10:00","11:00",60,"topic","FOUNDATIONS — What is Quality; What is Lean; What is Six Sigma; Lean vs Six Sigma vs Lean Six Sigma; the belt roles and where a White Belt contributes; the DMAIC roadmap"),
        ("11:00","11:15",15,"break","Tea break"),
        ("11:15","12:00",45,"topic","DMAIC · DEFINE — Voice of the Customer; VOC to CTQ translation; problem statements; SMART goals; the project charter and scope"),
        ("12:00","12:40",40,"lab","Hands-on: "+lab_titles([1])),
        ("12:40","13:40",60,"lunch","Lunch break"),
        ("13:40","14:25",45,"topic","DMAIC · MEASURE — process mapping; SIPOC; types of data; data collection plans; check sheets; the eight wastes (DOWNTIME); value-added analysis"),
        ("14:25","15:05",40,"lab","Hands-on: "+lab_titles([2])),
        ("15:05","15:50",45,"topic","DMAIC · ANALYZE — symptom vs root cause; 5 Whys; Fishbone (5M); reading a Pareto chart; common vs special cause variation"),
        ("15:50","16:05",15,"break","Tea break"),
        ("16:05","16:45",40,"lab","Hands-on: "+lab_titles([3])+" using the 5 Whys and Fishbone tools"),
        ("16:45","17:10",25,"topic","DMAIC · IMPROVE — generating solutions; impact/effort screening; 5S; mistake proofing (Poka-Yoke); standard work; piloting"),
        ("17:10","17:35",25,"lab","Hands-on: "+lab_titles([4])),
        ("17:35","17:55",20,"topic","DMAIC · CONTROL — the control plan; visual management; SOPs; team huddles; handover"),
        ("17:55","18:15",20,"lab","Hands-on: "+lab_titles([5])),
        ("18:15","18:30",15,"recap","Course recap and Q&A"),
     ]),
    }

# ------------------------------------------------------------------ deck overview section
COURSE_OVERVIEW = dict(
    section_title="Lean Six Sigma Fundamentals",
    concepts_title="What is Lean Six Sigma?",
    concepts=[
        ("Lean removes waste", "Maximise customer value by eliminating the effort the customer would never pay for."),
        ("Six Sigma reduces variation", "A data-driven method that makes results consistent and predictable."),
        ("Together: fast and accurate", "Lean Six Sigma delivers faster flow AND fewer defects, driven by evidence."),
        ("The White Belt contributes", "You support an improvement team — recognise waste, speak the language, use the basic tools."),
    ],
    framework_title="The DMAIC Roadmap",
    framework=[
        ("Define", "Understand the problem — VOC, CTQ, problem statement, SMART goal and charter."),
        ("Measure", "See what is really happening — process map, SIPOC, check sheets and the eight wastes."),
        ("Analyze", "Find the cause — 5 Whys, Fishbone, Pareto and variation."),
        ("Improve", "Fix the cause — countermeasures, 5S, mistake proofing, standard work and piloting."),
        ("Control", "Hold the gain — control plan, visual management, SOPs, huddles and handover."),
    ],
    statement=dict(
        headline="Improve the process, not the people.",
        body="Every tool in this course points at the process: see what it actually does, find why it does it, and change the system so the improvement holds.",
        kicker="THE LEAN SIX SIGMA MINDSET"),
    pillars_title="One Scenario, One Complete Story",
    pillars=[
        ("Define & Measure", ["BrewBean Cafe morning rush", "VOC → CTQ and problem statement", "Process map and waste tally"]),
        ("Analyze", ["5 Whys chain", "Fishbone (5M) diagram", "Reading a Pareto chart"]),
        ("Improve & Control", ["Impact/effort screening", "Pilot plan and standard work", "Control plan and handover"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Every lab uses one continuous scenario — the BrewBean Cafe morning rush, where customers queue up to 15 minutes.",
        "Exactly one lab per DMAIC phase, so you walk the full roadmap in a single day.",
        "Each lab produces a real artifact: a table, a map, a chart or a plan — using supplied templates.",
        "Each lab ends with a 'Check your work' step so you can verify your own output.",
        "By the end your five outputs form one complete improvement story, from problem to handover.",
    ],
)

LAB_SHOTS = {}

NEXT_STEPS = dict(title="Continuing Your Lean Six Sigma Journey", items=[
    "Spot the eight wastes in your own workplace this week — the DOWNTIME checklist works anywhere.",
    "Contribute to an improvement team using the language and tools from this course.",
    "Progress towards Yellow Belt — deeper data collection, process metrics and analysis tools.",
    "Build the habit: ask 'why?' past the symptom, and check the gain held after any change.",
])

THANK_YOU = dict(
    body="You can now describe the DMAIC roadmap, recognise waste and variation, and contribute to a Lean Six Sigma improvement team.",
    kicker="IMPROVE THE PROCESS")

# ------------------------------------------------------------------ Learner Guide content
LG_INTRO = ("This Learner Guide accompanies the course Certified Lean Six Sigma White Belt (CLSSWB) "
            "Training (C142), conducted by Tertiary Infotech Academy Pte Ltd. This is a one-day Lean "
            "Six Sigma awareness course. It follows the DMAIC roadmap end to end — Define, Measure, "
            "Analyze, Improve, Control — with one hands-on lab in each of the five phases, and "
            "provides step-by-step instructions for every lab.")
LG_INTRO2 = ("The course content is grounded in the body of knowledge published by The Council for Six "
             "Sigma Certification (CSSC) in 'Six Sigma: A Complete Step-by-Step Guide', so what you "
             "learn here matches the recognised White Belt standard. As a White Belt you are being "
             "prepared to CONTRIBUTE to an improvement team — to understand the language, recognise "
             "waste, and support the tools your team uses; the statistical analysis belongs to the "
             "Yellow, Green and Black Belt levels. Every lab uses one continuous scenario — the "
             "BrewBean Cafe morning rush, where customers queue up to 15 minutes and orders are "
             "sometimes made wrong. By the end of the day your five lab outputs form a complete "
             "improvement story: customer requirements and problem statement, process map and waste "
             "tally, root cause analysis, a selected countermeasure with a pilot plan, and a control plan.")

LG_SETUP = dict(
    needs=[
        "A laptop with a spreadsheet application (Microsoft Excel, Google Sheets or LibreOffice Calc), or simply pen and paper.",
        "A web browser for the interactive problem-solving tools listed in labs/tools.md.",
        "Printed or digital copies of this Learner Guide and the lab worksheets.",
        "A work process of your own to think about — the tools apply far better when the example is real.",
    ],
    verify_text=("No software installation is required for this course. Before you begin, confirm you can "
                 "open a blank spreadsheet and reach the browser-based tools listed in labs/tools.md."),
    conventions=[
        "Every lab uses the same BrewBean Cafe scenario, so your outputs accumulate across the day.",
        "Each lab states what you will build; keep every output — later labs depend on earlier ones.",
        "Where a lab uses figures, the data is provided in the lab worksheet — no external data is needed.",
        "Use only process data you are authorised to share if you substitute your own workplace scenario.",
    ],
)
LAB_NOTE = "Use only process data you are authorised to use if you substitute your own workplace scenario."

LG_WRAPUP = dict(
    title="Wrap-Up — The DMAIC Roadmap and Sustaining the Gain",
    intro=("These cross-cutting themes run through every phase of the course. Study this section "
           "alongside the labs so the same approach transfers from the BrewBean Cafe scenario "
           "to a real improvement in your own workplace."),
    sections=[
        dict(title="The DMAIC roadmap at White Belt depth", bullets=[
            "Define — capture the Voice of the Customer, translate it into measurable CTQs, and agree a problem statement with no solution in it.",
            "Measure — map the process as it really happens (SIPOC, process map) and tally the eight wastes with a check sheet.",
            "Analyze — drill past the symptom with 5 Whys and a Fishbone, and read a Pareto chart to see the vital few causes.",
            "Improve — brainstorm against the proven cause, screen ideas on impact vs effort, and pilot the change small first.",
            "Control — lock in the gain with a control plan, visual management, SOPs, team huddles and a proper handover.",
        ]),
        dict(title="Habits that make improvement stick", bullets=[
            "Measure before you change — without a baseline you cannot prove the improvement worked.",
            "Attack the process, not the people — the system produces the result you are seeing.",
            "Never write a solution into the problem statement.",
            "Ask 'why?' past the symptom until you reach something the team can act on.",
            "Standardise the improved method, or the process will drift back within weeks.",
        ]),
    ],
)

LG_NEXT_STEPS = [
    "First pass: complete every lab, following the steps in each lab worksheet.",
    "Second pass: repeat the five phases on a small process from your own workplace.",
    "Keep your improvement story together — the VOC/CTQ table, problem statement, process map, waste tally, root cause, pilot plan and control plan.",
    "Progress towards Yellow Belt for deeper data collection, process metrics and analysis tools.",
]

LG_GLOSSARY = [
    ("Quality", "Meeting the customer's requirements — not just being free of defects."),
    ("Lean", "A method to maximise customer value by systematically removing waste and improving flow."),
    ("Six Sigma", "A data-driven method to reduce variation so results become consistent and predictable."),
    ("DMAIC", "Define, Measure, Analyze, Improve, Control — the five-step Lean Six Sigma improvement roadmap."),
    ("Belt roles", "White, Yellow, Green, Black and Master Black Belt — increasing levels of Lean Six Sigma capability."),
    ("VOC", "Voice of the Customer — customer needs captured in the customer's own words."),
    ("CTQ", "Critical to Quality — a specific, measurable requirement translated from a VOC need."),
    ("Problem statement", "What is wrong, where, since when, and how big — never the solution."),
    ("SMART goal", "Specific, Measurable, Achievable, Relevant and Time-bound."),
    ("Project charter", "A one-page summary of the problem, goal, scope and team."),
    ("SIPOC", "A one-page process overview: Suppliers, Inputs, Process, Outputs, Customers."),
    ("Check sheet", "A simple tally form — the easiest reliable way to collect process data."),
    ("DOWNTIME", "The eight wastes: Defects, Overproduction, Waiting, Non-utilised talent, Transport, Inventory, Motion, Extra-processing."),
    ("Value-added", "An activity the customer would be willing to pay for, done right the first time."),
    ("Root cause", "The cause that, once removed, stops the problem recurring."),
    ("5 Whys", "Asking why repeatedly to drill from a symptom down to an actionable root cause."),
    ("Fishbone diagram", "A cause-and-effect diagram sorting causes into Manpower, Method, Machine, Material and Measurement."),
    ("Pareto chart", "A bar chart showing that roughly 80% of the problem comes from 20% of the causes."),
    ("Variation", "The spread in process output; common cause is inherent, special cause is assignable."),
    ("5S", "Sort, Set in order, Shine, Standardise, Sustain — workplace organisation for physical and digital work."),
    ("Poka-Yoke", "Mistake proofing — making an error difficult or impossible to make."),
    ("Standard work", "The documented best-known method so anyone can repeat it the same way."),
    ("Piloting", "Trying a change small first, so mistakes stay cheap."),
    ("Control plan", "Metric, target, monitoring method, frequency, owner and reaction plan."),
    ("Visual management", "Making performance visible so problems are noticed the same day."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1", "1 July 2026", "Initial release — CLSSWB 1-day lesson plan for the Lean Six Sigma awareness course.", TRAINER),
    ("2", "19 July 2026", "Rebuilt from the single-source content module: DMAIC roadmap end to end within one "
     "8-hour training day, exactly one hands-on lab per DMAIC phase (5 labs) on a single continuous scenario, "
     "content simplified to White Belt awareness depth.", TRAINER),
    ("3", VERSION_DATE,
     "Released under course code C142 as a commercial one-day hands-on course. Schedule restructured so "
     "every DMAIC lab gains additional hands-on time and the day closes with a full course recap and Q&A.",
     TRAINER),
]
