class RankingEngine:
    """
    Responsibilities:
    - Restaurant ranking
    - CTR estimation
    - Relevance scoring
    
    Technology: Rule-based scoring initially, XGBoost later. NO LLM.
    """
    
    def calculate_score(self, distance_m: float, rating: float, popularity_score: float, is_open: bool):
        # Initial rule-based heuristic
        if not is_open:
            return 0.0
            
        # Example naive weight distribution
        distance_weight = 0.5
        rating_weight = 0.3
        popularity_weight = 0.2
        
        # Normalize distance (closer is better, assume max interest radius 5km)
        normalized_distance = max(0, (5000 - distance_m) / 5000)
        
        score = (normalized_distance * distance_weight) + \
                ((rating / 5.0) * rating_weight) + \
                (popularity_score * popularity_weight)
                
        return score

ranking_engine = RankingEngine()
