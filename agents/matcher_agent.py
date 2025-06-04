import os
from agents.embedding_agent import EmbeddingAgent
from agents import VectorMatchAgent
from helpers import JsonHelper


class MatcherAgent:

    def __init__(self):
        self.embedding_agent = EmbeddingAgent()
        self.vector_match_agent = VectorMatchAgent()
        partner_metadata_path = os.path.join(
            os.getcwd(), "data/partners/partner_metadata.json"
        )
        id_to_partner_path = os.path.join(
            os.getcwd(), "data/partners/id_to_partner.json"
        )

        self.partner_metadata = JsonHelper.get_json_data(partner_metadata_path)
        """
        0 → Tokyo Beauty Lab  
        1 → Nordic Face Studio  
        2 → Mediterraneo Glow  
        3 → Parisian Porcelaine  
        4 → Ayurvedic Radianceid_to_partner_path
        """
        self.id_to_partner = JsonHelper.get_json_data(id_to_partner_path)

    def match(self, image_pil):
        vector = self.embedding_agent.get_image_embedding(image_pil)
        match_indices = self.vector_match_agent.find_matches(vector)

        results = []
        for idx in match_indices:
            partner_id = self.id_to_partner[str(idx)]
            partner_data = self.partner_metadata[partner_id]
            results.append(
                {
                    "partner_id": partner_id,
                    "name": partner_data["name"],
                    "style": partner_data["style_keywords"],
                    "mood": partner_data["mood"],
                    "category": partner_data["category"],
                    "description": partner_data["description"],
                    "match_reason": f"it is matched by: {', '.join(partner_data['style_keywords'])}, mood: {', '.join(partner_data['mood'])}",
                }
            )

        return results
