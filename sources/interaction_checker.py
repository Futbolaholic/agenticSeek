import httpx
from typing import List, Dict

class InteractionChecker:
    """Check supplement-drug interactions using the RxNav API."""

    RXCUI_URL = "https://rxnav.nlm.nih.gov/REST/approximateTerm.json"
    INTERACTION_URL = "https://rxnav.nlm.nih.gov/REST/interaction/list.json"

    async def _get_rxcui(self, client: httpx.AsyncClient, name: str) -> str | None:
        params = {"term": name}
        resp = await client.get(self.RXCUI_URL, params=params, timeout=10)
        data = resp.json()
        try:
            return data["approximateGroup"]["candidate"][0]["rxcui"]
        except Exception:
            return None

    async def check(self, items: List[str]) -> Dict:
        async with httpx.AsyncClient() as client:
            rxcuis = []
            for name in items:
                rxcui = await self._get_rxcui(client, name)
                if rxcui:
                    rxcuis.append(rxcui)
            if not rxcuis:
                return {"interactions": []}
            params = {"rxcuis": "+".join(rxcuis)}
            resp = await client.get(self.INTERACTION_URL, params=params, timeout=10)
            data = resp.json()
            return data.get("fullInteractionTypeGroup", [])
