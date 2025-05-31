import os, json, logging, openai, asyncio
logger = logging.getLogger("arb_bot")
openai.api_key = os.getenv("OPENAI_API_KEY")

async def ai_risk_check(text: str) -> bool:
    if not openai.api_key:
        return True
    try:
        resp = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":text}],
            temperature=0
        )
        answer = resp.choices[0].message.content.strip().lower()
        return "yes" in answer or "safe" in answer
    except Exception as e:
        logger.error(f"AI risk check error: {e}")
        return False