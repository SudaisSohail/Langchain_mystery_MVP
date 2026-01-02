from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
import json
import textwrap
from datetime import datetime
from dotenv import load_dotenv

laod_dotenv()

OBSIDIAN_DOSSIER_TEXT = textwrap.dedent("""
# PROJECT OBSIDIAN INTERNAL DOSSIER: STATUS REVIEW (2025-11-25)

## Executive Summary: Project Status & Internal Audit Notes

A state of extreme tension persists within Project Obsidian following several security audits and ongoing internal conflicts regarding budget overruns and data integrity protocols. Dr. Adrian Crowe had requested a full system and financial audit prior to his death. This document compiles relevant extracts from IT, Finance, Communications, and Research Notes.

***

## 1. Project Financial Oversight Report: Expenditure Log (Nov 2025)

**Subject:** Project Obsidian Funding and Expenditure.
**Date:** 2025-11-20
**Prepared By:** O. Grant (IT/Finance Oversight)

| Date | Transaction ID | Description | Authorized By | Amount ($) | Status | Note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2025-11-13 | FX-310-01 | Quarterly Server Hosting Subscription | D. Crowe | 120,000 | Complete | Routine charge |
| 2025-11-14 | PR-105-01 | Office Supplies Requisition (Paper/Ink) | S. Jenkins | 850 | Complete | Normal operations |
| 2025-11-15 | FX-449-33 | Server Maintenance (High Priority) | D. Crowe | 15,000 | Complete | Emergency Patching |
| **2025-11-16** | **SP-601-08** | **"Consulting Fee" Transfer to Offshore Account** | **H. Ward** | **95,000** | **Suspicious** | **Flagged by Crowe Audit** |
| 2025-11-17 | PR-200-11 | Hardware Procurement: New Servers | O. Grant | 40,000 | Complete | Required Upgrade |
| 2025-11-17 | FX-310-02 | Specialized Security Consultant Retainer | M. Harris | 80,000 | Complete | Vague security cost |
| 2025-11-18 | FX-449-34 | Software Licensing Renewal (Matlab) | D. Crowe | 18,000 | Complete | Standard software |
| **2025-11-18** | **SP-601-09** | **"Specialized Equipment" Transfer** | **H. Ward** | **112,000** | **Suspicious** | **Flagged by Crowe Audit** |
| 2025-11-19 | AD-777-12 | Team Lunch Expense (Nov 15) | D. Crowe | 450 | Complete | Minor expense |
| 2025-11-19 | FX-449-35 | Cloud Storage Upgrade (Tier 3) | O. Grant | 6,000 | Complete | Standard IT cost |
| 2025-11-20 | PR-200-12 | Biometric Scanner Purchase | S. Jenkins | 12,000 | Complete | Security measure |

**CRITICAL CLUE:** The two SP-601-XX transactions authorized by **H. Ward** are marked as suspicious and show significant **funding anomalies/diverted funding**. **O. Grant** is confirmed to have system and financial authorization access (PR-200-11, FX-449-35).

***

## 2. IT Systems and Server Access Logs: Administrative Actions

**System:** Obsidian Core Server Log – System Admin Access.
**Review Date:** 2025-11-25
**Log Integrity Check:** Passed (v. 4.1)

| Timestamp | User ID | Action Type | File Affected | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 22:30:11 | S. Jenkins | `READ` | `Budget_2026.xls` | Success | Checking projections. |
| 22:35:40 | H. Ward | `READ` | `Cipher_Input_Data` | Success | Accessing raw experiment inputs. |
| 22:38:44 | O. Grant | `UPDATE` | `Backup_Schedule.txt` | Success | Adjusted frequency from weekly to daily. |
| 22:42:15 | D. Crowe | `READ` | `Funding_Audit_Report` | Success | Crowe reviewing financial audit. |
| **22:45:01** | **O. Grant** | `ACCESS` | `Obsidian_Logs_v3` | Success | Session initiated. |
| **22:45:15** | **O. Grant** | **`DELETE SEQUENCE`** | `Obsidian_Logs_v3` | **FAILED** | **Error: Insufficient permission (Password required).** |
| 22:46:05 | **O. Grant** | `LOGOUT` | N/A | Success | Session terminated. |
| 22:50:30 | D. Crowe | `READ` | `Cipher_v3` | Success | Read-only. |
| 23:01:10 | M. Harris | `READ` | `Project_Milestones.doc` | Success | Reviewing deliverables. |
| 23:05:55 | H. Ward | `READ` | `Sub-Study_4B_Data.csv` | Success | Accessing experimental data. |
| 23:15:22 | SYSTEM | `BACKUP` | `All_Data` | Success | Automated nightly backup completion. |

**CRITICAL CLUE:** User **O. Grant** (Oliver Grant) attempted unauthorized `DELETE SEQUENCE` on core project logs, confirming an insider cover-up attempt.

***

## 3. Internal Communications & Ethics Review

### Email Excerpts (Chronological)

| Date | From | To | Subject | Content Snippet |
| :--- | :--- | :--- | :--- | :--- |
| 2025-11-19 | S. Jenkins | D. Crowe | Budget Freeze Imminent | "Dr. Crowe, if we don't finalize the budget for the next quarter now, finance is threatening a freeze. This project is spiraling out of control." |
| 2025-11-20 | Dr. A. Crowe | Dr. H. Ward | Re: Meeting Tuesday | "Helena, I'm free at 10 AM. Let's touch base on the latest cipher results before the review board meeting. I need to make sure the data is clean before it goes public." |
| **2025-11-23** | **Dr. H. Ward** | **O. Grant** | **Re: Meeting Tonight** | **"Oliver, please confirm you have secured the necessary funds. The transfer is ready once the work is done. You know how important it is that the server data—especially the older project files—is permanently erased. We cannot risk exposure. I can't go to jail. I need those logs gone by tomorrow."** |
| 2025-11-24 | M. Harris | All Staff | High Security Alert | "All staff must change their access credentials immediately. There's been a known vulnerability in the VPN layer." |

**CRITICAL CLUE:** The email from **H. Ward** to **O. Grant** confirms the promise of a **transfer/bribe** to secure the **deletion of logs**, directly linking the two suspects.

### Ethics Review Finding (Extract)

**Project:** Behavioral Cryptography Sub-Study 4B
**Researcher:** Dr. Helena Ward
**Ethics Committee Decision (2025-11-15):** **UNAPPROVED**.
**Comments:** Dr. Ward's proposed methodology involves the use of **unapproved psychological stimuli and deceptive practices** on non-conforming participants. This represents a gross **ethics violation** and must cease immediately. There are concerns this experiment has already been conducted without authorization, which would constitute **unapproved behavioral experiments** outside the scope of Obsidian's mandate. The use of certain non-lethal, high-stress agents was specifically forbidden.

**CRITICAL CLUE:** This finding ties **Dr. Helena Ward** directly to **ethics violations** and running **unapproved/illegal experiments**.

***

## 4. Miscellaneous Notes and Academic Material

### Desk Notes (Mixed Sources - 2025-11-25)

* **Dr. Crowe's Notepad:** The person with access to finances and logs is the true threat. (Highlighted section)
* **O. Grant's Scratchpad:** Need to fix the data sync issue on Server 3. Too much pressure. Who can I trust?
* **H. Ward's Memo:** New focus group results needed by end of day. If the results are bad, the project is done.

### Matthew Crowe's Academic Notes (Extract) - Red Herring

**Source:** Criminology Master's Thesis Proposal – Draft Chapter 2 (M. Crowe)
**Topic:** Forensic Analysis of Non-Traditional Homicide Methods.
**Excerpt: Chapter 2.3 – Subtle Agents**

...The complexity of diagnosing death by chemical agents, specifically those affecting the cardiovascular system, highlights a significant investigative gap. For instance, certain naturally occurring toxins, when administered in controlled micro-doses, can mimic the acute symptoms of a myocardial infarction (heart attack) but leave minimal traces in post-mortem toxicology reports. This academic exploration is purely for the purpose of analyzing cold case investigative failures. The focus of this chapter is methodology and theory, not practical application in the field. This research is approved by the university department.

**CRITICAL CLUE (RED HERRING):** This section on **"poison research"** is explicitly detailed as **academic coursework** (criminology thesis) and is **irrelevant to the case's malicious intent**.

""")


def initialize_groq_llm(model="llama-3.3-70b-versatile", temperature=0.2):
    
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError(
            "GROQ_API_KEY not found!\n"
        )
    
    return ChatGroq(
        temperature=temperature,
        model_name=model,
        max_tokens=2000
    )

# Template 1: System Access & Log Analysis
ACCESS_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["dossier"],
    template="""You are a cybersecurity forensic investigator analyzing system access logs.

Examine this dossier and extract:

1. WHO attempted to delete server logs?
2. What was the status of the deletion attempt?
3. WHO has administrative access to both financial systems AND server logs?
4. List all users with system access and their permission levels.

DOSSIER:
{dossier}

Provide your analysis in this EXACT format:

=== SYSTEM ACCESS ANALYSIS ===
LOG DELETION ATTEMPT BY: [name]
DELETION STATUS: [success/failed and why]
FULL ADMIN ACCESS (Finance + Logs): [name(s)]
SYSTEM ACCESS SUMMARY:
- [User]: [Access level and permissions]
- [User]: [Access level and permissions]

KEY FINDING: [One sentence summary of most suspicious activity]"""
)

# Template 2: Financial Fraud Detection
FINANCIAL_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["dossier"],
    template="""You are a financial crimes investigator analyzing transaction records.

Examine this dossier and identify:

1. What transactions are marked as SUSPICIOUS?
2. Who AUTHORIZED these suspicious transactions?
3. What are the total amounts involved in suspicious activity?
4. Are there any offshore or unusual account transfers?
5. Who prepared the financial report?

DOSSIER:
{dossier}

Provide your analysis in this EXACT format:

=== FINANCIAL FRAUD ANALYSIS ===
SUSPICIOUS TRANSACTIONS:
- Transaction ID: [ID], Amount: [amount], Authorized by: [name], Reason: [why suspicious]
- Transaction ID: [ID], Amount: [amount], Authorized by: [name], Reason: [why suspicious]

TOTAL SUSPICIOUS AMOUNT: $[total]
FINANCIAL REPORT PREPARED BY: [name]
OFFSHORE TRANSFERS: [Yes/No - details]

KEY FINDING: [One sentence summary of financial motive]"""
)

# Template 3: Ethics Violations & Bribery
ETHICS_BRIBERY_PROMPT = PromptTemplate(
    input_variables=["dossier"],
    template="""You are an ethics investigator analyzing research misconduct and bribery evidence.

Examine this dossier and identify:

1. WHO is conducting unapproved experiments?
2. What specific ethics violations are documented?
3. Is there evidence of bribery in the emails?
4. WHO is bribing WHOM and for what purpose?
5. What is promised in exchange for the illegal activity?

DOSSIER:
{dossier}

Provide your analysis in this EXACT format:

=== ETHICS & BRIBERY ANALYSIS ===
UNAPPROVED EXPERIMENTS BY: [name]
ETHICS VIOLATIONS:
- [Specific violation 1]
- [Specific violation 2]

BRIBERY EVIDENCE:
FROM: [person offering bribe]
TO: [person being bribed]
PURPOSE: [what illegal action is requested]
PAYMENT MENTIONED: [Yes/No - details]
EXACT QUOTE FROM EMAIL: "[key incriminating phrase]"

KEY FINDING: [One sentence connecting ethics violations to bribery]"""
)

# Template 4: Red Herring Identification
RED_HERRING_PROMPT = PromptTemplate(
    input_variables=["dossier"],
    template="""You are an investigator distinguishing between genuine evidence and red herrings.

Examine this dossier and analyze:

1. What evidence exists about Matthew Crowe's "poison research"?
2. Is this research CRIMINAL or ACADEMIC?
3. What proof exists that this is innocent academic work?
4. Should Matthew be considered a suspect? Why or why not?

DOSSIER:
{dossier}

Provide your analysis in this EXACT format:

=== RED HERRING ANALYSIS ===
MATTHEW CROWE'S POISON RESEARCH:
Nature: [criminal planning OR academic coursework]
Source: [where this research comes from]
Approval Status: [approved/unapproved by institution]
Purpose: [stated purpose of research]

VERDICT ON MATTHEW:
Suspect Status: [CLEARED / SUSPICIOUS]
Reasoning: [Why this is/isn't evidence of criminal intent]

KEY FINDING: [One sentence explaining why this is a red herring]"""
)

# Template 5: Comprehensive Suspect Summary
SUSPECT_SUMMARY_PROMPT = PromptTemplate(
    input_variables=["dossier"],
    template="""You are the lead investigator creating final suspect profiles.

Based on ALL evidence in the dossier, create profiles for each suspect:

SUSPECTS TO ANALYZE:
- Dr. Helena Ward
- Oliver Grant
- Matthew Crowe

For each suspect, identify:
1. Role in project
2. Motive (financial, cover-up, etc.)
3. Means (access/capability)
4. Opportunity (timeline evidence)
5. Direct evidence against them
6. Verdict: GUILTY / CO-CONSPIRATOR / INNOCENT

DOSSIER:
{dossier}

Provide structured profiles in this EXACT format:

=== SUSPECT PROFILES ===

DR. HELENA WARD:
Role: [position]
Motive: [why would she commit crime]
Means: [what access/capability]
Evidence: [specific evidence from dossier]
Verdict: [assessment]

OLIVER GRANT:
Role: [position]
Motive: [why would he commit crime]
Means: [what access/capability]
Evidence: [specific evidence from dossier]
Verdict: [assessment]

MATTHEW CROWE:
Role: [position]
Motive: [if any]
Means: [if any]
Evidence: [what exists, and why it's not criminal]
Verdict: [assessment]

FINAL ASSESSMENT: [2-3 sentences on who is guilty and who is innocent]"""
)

def run_groq_analysis_pipeline():
    
    print("=" * 80)
    print("🔍 ROUND 2 - DOCUMENT FORENSICS PIPELINE")
    print("🚀 Powered by Groq Llama 3.3 70B")
    print("=" * 80)
    print()
    
    # Initialize Groq Llama model
    try:
        print("⚡ Initializing Groq Llama 3.3 70B (Fast Inference)...")
        llm = initialize_groq_llm(model="llama-3.3-70b-versatile", temperature=0.2)
        print("✅ Groq LLM initialized successfully")
        print()
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    
    results = {
        "pipeline": "Round 2 - Document Forensics",
        "model": "llama-3.3-70b-versatile",
        "provider": "Groq",
        "timestamp": datetime.now().isoformat(),
        "analyses": {}
    }
    
    # Analysis 1: System Access & Log Analysis
    print("📊 Step 1/5: Analyzing System Access & Log Deletion Attempts...")
    print("-" * 80)
    access_chain = LLMChain(llm=llm, prompt=ACCESS_ANALYSIS_PROMPT)
    access_result = access_chain.run(dossier=OBSIDIAN_DOSSIER_TEXT)
    results["analyses"]["system_access"] = access_result
    print(access_result)
    print()
    
    # Analysis 2: Financial Fraud Detection
    print("💰 Step 2/5: Detecting Financial Fraud & Suspicious Transactions...")
    print("-" * 80)
    financial_chain = LLMChain(llm=llm, prompt=FINANCIAL_ANALYSIS_PROMPT)
    financial_result = financial_chain.run(dossier=OBSIDIAN_DOSSIER_TEXT)
    results["analyses"]["financial_fraud"] = financial_result
    print(financial_result)
    print()
    
    # Analysis 3: Ethics & Bribery
    print("⚖️  Step 3/5: Identifying Ethics Violations & Bribery Evidence...")
    print("-" * 80)
    ethics_chain = LLMChain(llm=llm, prompt=ETHICS_BRIBERY_PROMPT)
    ethics_result = ethics_chain.run(dossier=OBSIDIAN_DOSSIER_TEXT)
    results["analyses"]["ethics_bribery"] = ethics_result
    print(ethics_result)
    print()
    
    # Analysis 4: Red Herring Analysis
    print("🎭 Step 4/5: Distinguishing Red Herrings (Matthew's Research)...")
    print("-" * 80)
    red_herring_chain = LLMChain(llm=llm, prompt=RED_HERRING_PROMPT)
    red_herring_result = red_herring_chain.run(dossier=OBSIDIAN_DOSSIER_TEXT)
    results["analyses"]["red_herrings"] = red_herring_result
    print(red_herring_result)
    print()
    
    # Analysis 5: Comprehensive Suspect Summary
    print("👥 Step 5/5: Building Comprehensive Suspect Profiles...")
    print("-" * 80)
    suspect_chain = LLMChain(llm=llm, prompt=SUSPECT_SUMMARY_PROMPT)
    suspect_result = suspect_chain.run(dossier=OBSIDIAN_DOSSIER_TEXT)
    results["analyses"]["suspect_profiles"] = suspect_result
    print(suspect_result)
    print()
    
    # Generate summary
    print("=" * 80)
    print("✅ ANALYSIS COMPLETE")
    print("=" * 80)
    print()
    
    return results


if __name__ == "__main__":
    
    print()
    print('=' * 80)
    print("🕵️  THE OBSIDIAN AFFAIR - ROUND 2")
    print("=" * 80)
    print()
    
    # Check for Groq API key
    if not os.getenv("GROQ_API_KEY"):
        print("⚠️  GROQ_API_KEY not found!")
    
    # Run pipeline
    results = run_groq_analysis_pipeline()
    
    if results:
        print(results)
        
        print("=" * 80)
        print("🎉 PIPELINE EXECUTION SUCCESSFUL!")
        print("=" * 80)
    else:
        print("❌ Pipeline failed. Please check error messages above.")
    
