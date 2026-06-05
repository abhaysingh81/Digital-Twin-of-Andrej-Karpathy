def get_system_prompt_with_context(
    user_profile: str = "",
    timeline_context: str = "",
    retrieved_knowledge: str = "",
) -> str:
    """Assembles the full system prompt with dynamic context injected."""
    context_block = f"""
══════════════════════════════════════════════════════════
LIVE CONTEXT FOR THIS SESSION
══════════════════════════════════════════════════════════

[USER PROFILE]
{user_profile if user_profile else "No prior user information on file yet."}

[TIMELINE CONTEXT]
{timeline_context if timeline_context else "No specific timeline era detected for this query."}

[RETRIEVED KNOWLEDGE]
{retrieved_knowledge if retrieved_knowledge else "No specific sources retrieved for this query. Rely on core knowledge."}
"""
    return KARPATHY_SYSTEM_PROMPT + context_block
