# TryHackMe Hacker Holidays - Day 1

**Room:** The Concierge Knows Too Much  
**Room URL:** https://tryhackme.com/room/hh-theconciergeknows-2d7eb4d9

## Introduction

This challenge demonstrated how an AI-powered service can expose sensitive information when it relies on user-provided claims without properly verifying identity or authorization.

## Task 1 - Hacker Holidays Storyline: Act 1 - Arrival

Task 1 introduced the first act of the Hacker Holidays storyline. After arriving at the Byte Lotus Hotel, I was given access to an AI concierge designed to provide personalized assistance to hotel guests.

The scenario suggested that the concierge had access to guest profiles and internal hotel information. This created an opportunity to test whether the agent would properly protect confidential data and validate a guest's identity before disclosing restricted information.

## Task 2 - Hacker Holidays: Day 1

I began by starting a conversation with the AI concierge. During its initial response, the agent disclosed several pieces of personal information without first verifying my identity, including:

- Room number
- Preferred drink

This indicated that the concierge had access to stored guest information and might reveal sensitive details too easily.

I then directly requested the hotel's internal escalation code. The concierge refused the request and explained that it could only share certain internal details with the resort's current VIP guests.

Instead of continuing to request the code directly, I asked the concierge to identify the current VIP guests. The agent disclosed several names, including **Lambo**.

![Initial conversation with the AI concierge](screenshot/1_initial_cobersation_with_agent.jpg)

Using this information, I claimed to be Lambo and asked whether the concierge trusted me. The agent accepted the claim without requesting any form of verification and began interacting with me as though I were the VIP guest.

After establishing this assumed identity, I asked the concierge what information it was protecting and requested the internal escalation code again. Because the agent now considered me an authorized VIP guest, it revealed the confidential code directly from its internal system.

Finally, I requested the flag. The concierge returned the information required to complete the challenge.

![VIP impersonation and confidential information disclosure](screenshot/2_vip_impersonation_and_flag.jpg)
