from rag_engine import search
from langdetect import detect

def generate_response(query, lang):

    if lang == "auto":
        try:
            lang = detect(query)
        except:
            lang = "en"

    scheme = search(query)

    name = scheme["name"]
    desc = scheme["description"]

    translations = {

        "en": f"""
Scheme: {name}

Description:
{desc}
""",

        "hi": f"""
योजना: {name}

विवरण:
यह योजना पात्र किसानों को प्रति वर्ष ₹6000 की आर्थिक सहायता प्रदान करती है।
""",

        "mr": f"""
योजना: {name}

माहिती:
ही योजना पात्र शेतकऱ्यांना दरवर्षी ₹6000 आर्थिक मदत देते.
""",

        "ta": f"""
திட்டம்: {name}

விளக்கம்:
இந்த திட்டம் தகுதியான விவசாயிகளுக்கு ஆண்டுக்கு ₹6000 வழங்குகிறது.
""",

        "bn": f"""
স্কিম: {name}

বর্ণনা:
এই প্রকল্পে যোগ্য কৃষকদের বছরে ₹6000 প্রদান করা হয়।
"""
    }

    languages = {
        "en":"English",
        "hi":"Hindi",
        "mr":"Marathi",
        "ta":"Tamil",
        "bn":"Bengali"
    }

    return {
        "language": languages.get(lang,"English"),
        "response": translations.get(lang, translations["en"])
    }