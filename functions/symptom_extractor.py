import re

def extract_symptoms(text: str) -> list[str]:
    symptoms = re.findall(
        r"\b("
        r"headache|fever|nausea|fatigue|pain|stomach pain|breast lump|"
        r"cough|sore throat|shortness of breath|difficulty breathing|"
        r"vomiting|diarrhea|constipation|dizziness|chills|"
        r"muscle pain|body aches|chest pain|abdominal pain|"
        r"back pain|joint pain|rash|itching|"
        r"runny nose|congestion|loss of taste|loss of smell"
        r")\b",
        text.lower(),
    )
    return list(set(symptoms))
