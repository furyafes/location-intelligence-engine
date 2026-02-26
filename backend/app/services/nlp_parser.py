class NLPParser:
    """
    Responsibilities:
    - Translates user query into a structured filter.
    
    Technology: GPT-class LLM (low temperature).
    Input: "5 dakika yürüme mesafesinde açık vegan mekân"
    Output JSON: { "max_distance": 400, "category": "vegan", "open_now": true }
    """
    
    async def parse_query(self, query: str) -> dict:
        # TODO: Call OpenAI API or similar with structured JSON schema output
        return {
            "max_distance": 500,
            "category": "unknown",
            "open_now": True
        }

nlp_parser = NLPParser()
