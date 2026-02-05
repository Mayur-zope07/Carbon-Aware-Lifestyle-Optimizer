def carbon_level(total):
    if total < 5:
        return "Low 🌱"
    elif total < 12:
        return "Medium ⚠️"
    else:
        return "High 🔥"


def generate_recommendations(result, inputs):
    tips = []

    if result["vehicle"] > result["electricity"]:
        tips.append("🚗 Reduce vehicle usage or switch to public transport / EV")

    if inputs["food_type"] == "non_veg":
        tips.append("🍽 Reduce non-veg meals to lower food emissions")

    if result["electricity"] > 3:
        tips.append("⚡ Use energy-efficient appliances and turn off unused devices")

    if result["waste"] > 2:
        tips.append("♻️ Reduce waste and practice recycling")

    if not tips:
        tips.append("🌿 Great job! Your lifestyle is already eco-friendly")

    return tips
