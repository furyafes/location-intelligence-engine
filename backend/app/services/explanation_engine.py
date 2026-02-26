class ExplanationEngine:
    """
    Responsibilities:
    - Generate place explanations
    - Write location directions
    - Summarize highlighted features
    
    Technology: LLM used purely for content generation.
    """
    
    async def generate_explanation(self, place_data: dict, user_query: str) -> str:
        # TODO: Call OpenAI API to generate an explanation matching the user query
        return "This place perfectly matches your request."

explanation_engine = ExplanationEngine()
